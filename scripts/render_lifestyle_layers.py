"""Build editable layered life/work animation; render with installed HyperFrames."""
from pathlib import Path
import argparse,json,shutil,subprocess,os,hashlib,html
from lifestyle_audio import finish_with_music

TEXT = {
    'zh': {
        'page_title': '生活职场拼贴动画',
        'task1': '临时会议', 'task2': '补个资料', 'task3': '马上回复',
        'hero_title': '重点任务', 'hero_body': '忙了一天，进度却没动',
        'notice1': '有新消息', 'notice1_small': '这件事也要处理',
        'notice2': '临时开会', 'notice2_small': '手上的工作先暂停',
        'notice3': '再改一下', 'notice3_small': '思路又一次被打断',
        'focus_label': '今天，只先做一件事', 'focus_title': '最重要的那件',
        'focus_body1': '关掉干扰', 'focus_body2': '给它一段完整时间',
        'font_stack': 'Yahei, "Microsoft YaHei", "Noto Sans CJK SC", "PingFang SC", sans-serif',
    },
    'en': {
        'page_title': 'A Paper Collage About Getting Focus Back',
        'task1': 'Quick meeting', 'task2': 'One more file', 'task3': 'Reply now',
        'hero_title': 'Priority task', 'hero_body': 'All day. No progress.',
        'notice1': 'New message', 'notice1_small': 'Handle this too',
        'notice2': 'Quick meeting', 'notice2_small': 'Pause your work',
        'notice3': 'One more edit', 'notice3_small': 'There goes the thought',
        'focus_label': 'Today, just one thing', 'focus_title': 'One priority',
        'focus_body1': 'Mute the noise', 'focus_body2': 'Give it one clear hour',
        'font_stack': 'system-ui, sans-serif',
    },
}

def build(config,output,node,hyperframes,gsap,ffmpeg,render=True):
    cfg=json.loads(config.read_text(encoding='utf-8-sig'))
    language=str(cfg.get('language','zh')).lower()
    if language not in TEXT: raise ValueError('language must be zh or en')
    if output.exists():raise ValueError('Use a new output filename')
    if len(cfg.get('scenes',[]))!=3:raise ValueError('This layered scene needs three beats: overload, interruption, focus')
    if any(float(s['seconds'])<4 for s in cfg['scenes']):raise ValueError('This choreography needs at least four seconds per beat; shorten only after remapping its action windows')
    if (int(cfg.get('width',1280)),int(cfg.get('height',720)))!=(1280,720):raise ValueError('This layered layout is 1280x720; other aspect ratios need a new composition')
    sprite=(config.parent/cfg['character_sheet']).resolve()
    if not sprite.is_file():raise FileNotFoundError(sprite)
    root=output.parent/(output.stem+'-assets');project=root/'editable';assets=project/'assets';assets.mkdir(parents=True,exist_ok=True)
    if (project/'index.html').exists():raise ValueError('Editable output already exists; use a new filename')
    shutil.copy2(sprite,assets/'character.png');shutil.copy2(gsap,assets/'gsap.min.js')
    total=sum(float(s['seconds']) for s in cfg['scenes'])
    source=(Path(__file__).resolve().parents[1]/'assets/layered-focus.html').read_text(encoding='utf-8')
    source=source.replace('__LANG__','zh-CN' if language=='zh' else 'en').replace('__FONT_STACK__',TEXT[language]['font_stack'])
    for key,value in TEXT[language].items():
        if key!='font_stack': source=source.replace('__'+key.upper()+'__',html.escape(value))
    for i,s in enumerate(cfg['scenes'],1):
        source=source.replace(f'__TITLE{i}__',html.escape(s['title'])).replace(f'__SUB{i}__',html.escape(s.get('subtitle','')))
    palette=cfg.get('palette',{})
    for key,default in [('orange','#f17c3b'),('teal','#245d58'),('cream','#fff3df'),('gold','#efb647')]:source=source.replace('__'+key.upper()+'__',palette.get(key,default))
    source=source.replace('__TIMING__',json.dumps([float(s['seconds']) for s in cfg['scenes']])).replace('__DURATION__',str(total))
    (project/'index.html').write_text(source,encoding='utf-8')
    (project/'BRIEF.md').write_text('---\nworkflow: general-video\nflow: autonomous\n---\n# Layered lifestyle animation\nUse supplied original puppet sheet and configurable three-beat script. Render 1280x720 60fps. No production-nature labels. Actual native WorkBuddy use, static/continuous/listening checks and user approval remain separately recorded.\n',encoding='utf-8')
    shutil.copy2(config,root/'story.json')
    (root/'source-sha256.json').write_text(json.dumps({'config':hashlib.sha256(config.read_bytes()).hexdigest(),'character_sheet':hashlib.sha256(sprite.read_bytes()).hexdigest()},indent=2),encoding='utf-8')
    if not render:print(project,flush=True);return project
    env=os.environ.copy();env['PATH']=str(Path(ffmpeg).parent)+os.pathsep+str(Path(node).parent)+os.pathsep+env.get('PATH','')
    picture=root/'picture.mp4'
    subprocess.run([str(node),str(hyperframes),'render',str(project),'-o',str(picture),'-f','60','-w','4','-q','delivery','--video-frame-format','png','--strict','--no-best-effort'],env=env,check=True)
    report=finish_with_music(picture,output,cfg,str(ffmpeg),config.parent)
    report['motion']={'engine':'layered-cut-paper-v1','fps':60,'whole_image_only':False,'independent_objects':['head','body','left-arm','writing-arm','clock-hands','task-paper','notification-cards','phone','progress','drawn-check'],'transitions':'persistent character and desk; paper sweep at story handoffs','continuous_idle_wobble':False,'continuous_visual_review':None,'user_acceptance':None}
    report['editable_project']=str(project)
    (root/'render-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Saved '+str(output),flush=True)
    return project

def main():
    p=argparse.ArgumentParser();p.add_argument('config',type=Path);p.add_argument('output',type=Path);p.add_argument('--node',type=Path,required=True);p.add_argument('--hyperframes',type=Path,required=True);p.add_argument('--gsap',type=Path,required=True);p.add_argument('--ffmpeg',type=Path,required=True);p.add_argument('--build-only',action='store_true');a=p.parse_args()
    build(a.config.resolve(),a.output.resolve(),a.node,a.hyperframes,a.gsap,a.ffmpeg,not a.build_only)
if __name__=='__main__':main()
