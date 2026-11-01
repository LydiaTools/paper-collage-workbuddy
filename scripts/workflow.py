"""WorkBuddy adaptation of Vox Director beats -> prompts -> local motion -> music.

Uses the upstream style composer under its retained MIT license. Planning is
performed by the host assistant; this script validates and materializes its plan.
"""
from pathlib import Path
import argparse, hashlib, json, os, re, shutil, subprocess
from upstream_styles import compose_collage_prompt, resolve_theme

MOVES = {'static','push_in','pull_out','pan','tilt','parallax','element'}
SIZES = {'EST_WIDE','WIDE','MEDIUM','CLOSE','DETAIL'}

def read(path): return json.loads(path.read_text(encoding='utf-8-sig'))
def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def validate(doc):
    beats=doc.get('beats',[])
    if not beats: raise ValueError('beats cannot be empty; the host assistant must first write a real storyboard')
    language=str(doc.get('language','zh')).lower()
    if language not in ('zh','en'): raise ValueError('language must be zh or en')
    title_key='title_en' if language=='en' else 'title_cn'
    fallback_title='title_cn' if language=='en' else 'title_en'
    renderer=doc.get('renderer','hyperframes')
    if renderer not in ('hyperframes','focus-layered'): raise ValueError('Unknown local renderer')
    seen=set();duration=0;warnings=[]
    for beat in beats:
        if 'id' not in beat or str(beat['id']) in seen: raise ValueError('Every beat needs a unique id')
        seen.add(str(beat['id']))
        if not (beat.get(title_key) or beat.get(fallback_title)) or not beat.get('narration'): raise ValueError(f'Each beat needs {title_key} (or {fallback_title}) and narration')
        shots=beat.get('shots',[])
        if not shots: raise ValueError('Each beat needs actual shots')
        shot_ids=set()
        for shot in shots:
            sid=str(shot.get('id',''))
            if not sid or sid in shot_ids: raise ValueError('Shot ids must be unique within each beat')
            shot_ids.add(sid)
            dur=float(shot.get('dur',0))
            if dur<=0: raise ValueError('Shot durations must be positive')
            if dur>7: warnings.append(f'Beat {beat["id"]}/{sid}: consider splitting a long shot')
            if shot.get('camera_move') not in MOVES: raise ValueError('Use a supported flat-safe camera_move')
            if shot.get('shot_size') not in SIZES: raise ValueError('Use an explicit supported shot_size')
            if not shot.get('scene') or not shot.get('element_motion'): raise ValueError('Every shot needs scene and element_motion')
            duration+=dur
    width=int(doc.get('width',1280));height=int(doc.get('height',720))
    if min(width,height)<240 or width%2 or height%2: raise ValueError('Use positive even dimensions of at least 240px')
    if renderer=='focus-layered':
        if len(beats)!=3 or any(len(b['shots'])!=1 for b in beats): raise ValueError('focus-layered is the three-beat sample; choose hyperframes for other stories')
        if (width,height)!=(1280,720) or any(float(b['shots'][0]['dur'])<4 for b in beats): raise ValueError('focus-layered needs 1280x720 and at least 4s per beat')
    return {'duration':duration,'width':width,'height':height,'renderer':renderer,'warnings':warnings}

def plan(config, destination):
    doc=read(config);summary=validate(doc)
    if destination.exists() and any(destination.iterdir()): raise ValueError('Use an empty planning output directory')
    destination.mkdir(parents=True,exist_ok=True)
    theme=resolve_theme(doc.get('theme','atomic-age')) or {}
    language=str(doc.get('language','zh')).lower()
    if language=='en': table=['# Storyboard and Motion Plan','','|Time|Shot|Narration|Scene|Object motion|','|---|---|---|---|---|']
    else: table=['# 分镜与动作表','','|时间|镜头|正文|场景|独立动作|','|---|---|---|---|---|']
    for beat in doc['beats']:
        for shot in beat['shots']:
            key=f'{beat["id"]}-{shot["id"]}';dur=float(shot['dur'])
            prompt=compose_collage_prompt(shot['scene'],'','',bg=beat.get('bg','cream'),
                aspect=doc.get('aspect',f'{summary["width"]}:{summary["height"]}'),with_title=False,
                style=theme.get('idiom','modern-flat'),palette=doc.get('look',{}).get('palette',theme.get('palette','orange, teal, cream')),
                type_style=theme.get('type_style'),finish=theme.get('finish'))
            prompt+=' Prepare clean separate cut-out pieces for the named motion. Titles are editable overlay text, never baked into the picture. Fixed print grain; no animated random texture.'
            prompts.append({'id':key,'image_prompt':prompt,'assets_needed':shot.get('assets_needed',[]),'asset_status':'needs actual asset preparation unless project already supplies them'})
            motions.append({'id':key,'start':time,'duration':dur,'shot_size':shot['shot_size'],'camera_move':shot['camera_move'],
                'element_motion':shot['element_motion'],'text_stable':True,'continuous_random_wobble':False})
            row=[f'{time:.2f}–{time+dur:.2f}',key,beat['narration'],shot['scene'],shot['element_motion']]
            table.append('|'+ '|'.join(str(x).replace('|','／').replace('\n',' ') for x in row)+'|');time+=dur
    (destination/'storyboard.md').write_text('\n'.join(table)+'\n',encoding='utf-8')
    save(destination/'asset-prompts.json',prompts);save(destination/'motion-plan.json',motions)
    save(destination/'plan-report.json',{**summary,'planning_model':'host assistant; no model API called by this script',
        'source_config_sha256':hashlib.sha256(config.read_bytes()).hexdigest(),'assets_generated':False,'video_rendered':False})
    print(json.dumps({'planning_output':str(destination),**summary},ensure_ascii=False))

def check_narration(doc, root, total, ffmpeg):
    value=doc.get('audio',{}).get('narration')
    if not value:return
    voice=Path(value);voice=voice if voice.is_absolute() else root/voice
    if not voice.is_file():raise FileNotFoundError(voice)
    probe=ffmpeg.with_name('ffprobe.exe' if ffmpeg.suffix.lower()=='.exe' else 'ffprobe')
    data=json.loads(subprocess.check_output([str(probe),'-v','error','-show_entries','format=duration','-of','json',str(voice)]))
    if float(data['format']['duration'])>total+.05:raise ValueError('Narration exceeds picture duration; extend storyboard before rendering, do not truncate approved speech')

def render(config,output,node,hyperframes,gsap,ffmpeg):
    doc=read(config);summary=validate(doc);root=config.parent
    if output.exists():raise ValueError('Use a new output filename')
    check_narration(doc,root,summary['duration'],ffmpeg)
    build=output.parent/(output.stem+'-assets');build.mkdir(parents=True,exist_ok=True)
    if summary['renderer']=='focus-layered':
        from render_lifestyle_layers import build as render_layers
        sprite=(root/doc['character_sheet']).resolve()
        audio=dict(doc.get('audio',{'mode':'generated','mood':'warm-focus','seed':29}))
        for key in ('narration','path'):
            if audio.get(key):audio[key]=str((root/audio[key]).resolve())
        language=str(doc.get('language','zh')).lower()
        title_key='title_en' if language=='en' else 'title_cn'
        subtitle_key='subtitle_en' if language=='en' else 'subtitle_cn'
        local={'width':summary['width'],'height':summary['height'],'smooth_fps':60,'language':language,
            'character_sheet':str(sprite),'palette':doc.get('palette',{}),'audio':audio,
            'scenes':[{'seconds':b['shots'][0]['dur'],'title':b.get(title_key) or b.get('title_cn') or b.get('title_en'),
                'subtitle':b.get(subtitle_key) or b.get('subtitle') or b['narration']} for b in doc['beats']]}
        cfg=build/'resolved-story.json';save(cfg,local)
        project=render_layers(cfg,output,node,hyperframes,gsap,ffmpeg)
    else:
        from lifestyle_audio import finish_with_music
        source=(root/doc['editable_project']).resolve()
        if not (source/'index.html').is_file():raise FileNotFoundError('The host assistant must create editable_project/index.html with real assets and per-shot motion first')
        if source==build or source in build.parents:raise ValueError('Output must be outside the editable source project')
        project=build/'editable'
        if project.exists():raise ValueError('Editable output already exists; use a new output filename')
        allowed={'.html','.js','.css','.json','.svg','.png','.jpg','.jpeg','.webp','.woff','.woff2','.ttf','.otf','.mp4','.wav','.mp3','.m4a'}
        for path in source.rglob('*'):
            rel=path.relative_to(source)
            if path.is_file() and path.suffix.lower() in allowed and not any(p.startswith('.') or p in ('node_modules','__pycache__') for p in rel.parts):
                dest=project/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(path,dest)
        (project/'assets').mkdir(exist_ok=True);shutil.copy2(gsap,project/'assets/gsap.min.js')
        env=os.environ.copy();env['PATH']=str(ffmpeg.parent)+os.pathsep+str(node.parent)+os.pathsep+env.get('PATH','')
        subprocess.run([str(node),str(hyperframes),'check',str(project)],env=env,check=True)
        picture=build/'picture.mp4'
        subprocess.run([str(node),str(hyperframes),'render',str(project),'-o',str(picture),'-f','60','-w','4','-q','delivery','--video-frame-format','png','--strict','--no-best-effort'],env=env,check=True)
        probe=ffmpeg.with_name('ffprobe.exe' if ffmpeg.suffix.lower()=='.exe' else 'ffprobe')
        media=json.loads(subprocess.check_output([str(probe),'-v','error','-show_entries','stream=width,height,r_frame_rate:format=duration','-of','json',str(picture)]))
        v=media['streams'][0]
        if (v['width'],v['height'])!=(summary['width'],summary['height']) or abs(float(media['format']['duration'])-summary['duration'])>.05:raise ValueError('Actual HTML picture dimensions or duration do not match beats.json; fix the project before audio assembly')
        finish_with_music(picture,output,doc,str(ffmpeg),root)
    shutil.copy2(config,build/'beats.json')
    # Keep portable editable configuration beside a single copy of the character.
    if summary['renderer']=='focus-layered':
        portable=read(build/'resolved-story.json');portable['character_sheet']='editable/assets/character.png'
        save(build/'story.json',portable)
    save(build/'workflow-report.json',{**summary,'source_config_sha256':hashlib.sha256(config.read_bytes()).hexdigest(),
        'output_sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'upstream':'Vox Director beats/shots and style composer',
        'default_api_calls':False,'voice_preserved':bool(doc.get('audio',{}).get('narration')),
        'complete_actual_listening':None,'continuous_visual_review':None,'user_acceptance':None})
    print('Saved '+str(output),flush=True)

def main():
    p=argparse.ArgumentParser();sub=p.add_subparsers(dest='command',required=True)
    c=sub.add_parser('check');c.add_argument('config',type=Path)
    a=sub.add_parser('plan');a.add_argument('config',type=Path);a.add_argument('destination',type=Path)
    r=sub.add_parser('render');r.add_argument('config',type=Path);r.add_argument('output',type=Path)
    for flag in ('node','hyperframes','gsap','ffmpeg'):r.add_argument('--'+flag,type=Path,required=True)
    args=p.parse_args();config=args.config.resolve()
    if args.command=='check':print(json.dumps(validate(read(config)),ensure_ascii=False))
    elif args.command=='plan':plan(config,args.destination.resolve())
    else:render(config,args.output.resolve(),args.node.resolve(),args.hyperframes.resolve(),args.gsap.resolve(),args.ffmpeg.resolve())

if __name__=='__main__':main()
