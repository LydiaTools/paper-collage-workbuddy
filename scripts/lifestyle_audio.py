"""Original procedural instrumental score and final audio/video assembly."""
import hashlib,json,math,subprocess,wave,shutil
from pathlib import Path
import numpy as np

MOODS={
    'warm-focus':{'bpm':100,'chords':[[57,60,64,71],[53,57,60,64],[48,55,59,64],[55,59,62,64]],'melody':.065,'percussion':.009},
    'calm':{'bpm':82,'chords':[[48,52,55,62],[53,57,60,64],[57,60,64,67],[55,59,62,69]],'melody':.042,'percussion':.003},
    'uplifting':{'bpm':108,'chords':[[48,52,55,59],[55,59,62,67],[57,60,64,67],[53,57,60,64]],'melody':.070,'percussion':.011},
    'reflective':{'bpm':86,'chords':[[57,60,64,67],[53,57,60,64],[50,53,57,60],[52,55,59,62]],'melody':.040,'percussion':.003},
}

def select_mood(cfg):
    requested=cfg.get('audio',{}).get('mood')
    if requested:
        if requested not in MOODS:raise ValueError('未知配乐情绪：'+requested)
        return requested
    text=' '.join(str(s.get('title',''))+' '+str(s.get('subtitle','')) for s in cfg.get('scenes',[]))
    if any(x in text for x in ('专注','消息','工作','效率','忙')):return 'warm-focus'
    if any(x in text for x in ('失落','分离','难过','孤独','遗憾')):return 'reflective'
    if any(x in text for x in ('睡眠','休息','放松','平静','慢下来')):return 'calm'
    if any(x in text for x in ('运动','出发','成长','尝试','行动')):return 'uplifting'
    return 'warm-focus'

def make_score(path,seconds,bpm=None,seed=29,mood='warm-focus'):
    settings=MOODS[mood];bpm=settings['bpm'] if bpm is None else bpm
    if seconds<=0 or not 60<=bpm<=130:raise ValueError('配乐时长须为正数，BPM 范围为 60–130')
    sr=48000;n=round(seconds*sr);audio=np.zeros((n,2),np.float64);rng=np.random.default_rng(seed);beat=60/bpm
    def add(note,start,duration,amp,pan=0,kind='keys'):
        begin=round(start*sr)
        if begin>=n:return
        count=min(round(duration*sr),n-begin);t=np.arange(count)/sr;f=440*2**((note-69)/12)
        if kind=='bass':
            signal=np.sin(2*np.pi*f*t)+.16*np.sin(2*np.pi*2*f*t);env=(1-np.exp(-t*50))*np.exp(-t*2.2)
        else:
            signal=np.sin(2*np.pi*f*t)+.25*np.sin(2*np.pi*f*2.002*t)+.085*np.sin(2*np.pi*f*3.001*t)
            env=(1-np.exp(-t*240))*np.exp(-t*2.5)
        signal=signal*env*amp
        audio[begin:begin+count,0]+=signal*math.sqrt((1-pan)/2)
        audio[begin:begin+count,1]+=signal*math.sqrt((1+pan)/2)
    chords=settings['chords']
    bars=max(1,math.ceil(seconds/(4*beat)))
    for bar in range(bars):
        start=bar*4*beat;chord=chords[bar%4]
        for j,note in enumerate(chord): add(note+12,start+j*.035,2.8,.09,(-.45+j*.3))
        for off in (0,2):add(chord[0]-12,start+off*beat,1.1,.10,0,'bass')
        # Space between melody notes leaves room for narration.
        for j,off in enumerate((.5,1.5,3.0)):
            if start+off*beat<seconds-1.0:add(chord[(j+bar)%4]+24,start+off*beat,.8,settings['melody'],(-.2 if j%2 else .2))
    # Light, filtered percussion rather than sharp click transients.
    for k in range(int(seconds/beat)):
        start=round((k+.5)*beat*sr);count=min(int(.09*sr),n-start)
        if count<=0:continue
        noise=rng.normal(0,1,count);noise=np.convolve(noise,np.ones(5)/5,mode='same')
        tap=noise*np.exp(-np.arange(count)/sr*65)*settings['percussion']
        audio[start:start+count]+=tap[:,None]
    # Gentle stereo reflections; deterministic and locally synthesized, no sampled songs.
    dry=audio.copy()
    for delay,gain in ((.071,.12),(.113,.08),(.197,.045)):
        shift=int(delay*sr)
        if shift<n:audio[shift:]+=dry[:-shift,::-1]*gain
    env=np.minimum(1,np.arange(n)/(sr*.35))*np.minimum(1,np.arange(n)[::-1]/(sr*1.05))
    audio*=env[:,None];peak=max(.001,float(np.max(np.abs(audio))));audio*=.64/peak
    path.parent.mkdir(parents=True,exist_ok=True)
    with wave.open(str(path),'wb') as out:
        out.setnchannels(2);out.setsampwidth(2);out.setframerate(sr);out.writeframes((np.clip(audio,-1,1)*32767).astype('<i2').tobytes())
    return {'method':'original local additive synthesis','bpm':bpm,'mood':mood,'seed':seed,'seconds':seconds,'sample_rate':sr,'channels':2}

def finish_with_music(picture,output,cfg,ffmpeg,root=None):
    picture=Path(picture);output=Path(output);build=output.parent/(output.stem+'-assets');build.mkdir(parents=True,exist_ok=True)
    root=Path(root) if root else Path.cwd()
    def media_path(value):
        p=Path(value);p=p if p.is_absolute() else root/p
        if not p.is_file():raise FileNotFoundError('音轨不存在：'+str(p))
        return p.resolve()
    probe=str(Path(ffmpeg).with_name('ffprobe.exe' if str(ffmpeg).lower().endswith('.exe') else 'ffprobe'))
    metadata=json.loads(subprocess.check_output([probe,'-v','error','-show_entries','format=duration','-of','json',str(picture)],text=True))
    duration=float(metadata['format']['duration']);audio=cfg.get('audio',{});mode=audio.get('mode','generated')
    if mode=='none':
        shutil.copyfile(picture,output)
        return {'video':str(output),'duration':duration,'audio':{'mode':'none','requires_explicit_user_request':True}}
    if mode=='track':
        track=media_path(audio['path']);score={'method':'provided track','path':str(track)}
    elif mode=='generated':
        track=build/'bgm-original.wav';score=make_score(track,duration,audio.get('bpm'),int(audio.get('seed',29)),select_mood(cfg))
    else:raise ValueError('audio.mode 只能是 generated、track 或用户明确要求的 none')
    voice=str(media_path(audio['narration'])) if audio.get('narration') else None
    level=float(audio.get('lufs',-23 if voice else -20))
    cmd=[ffmpeg,'-y','-v','error','-i',str(picture),'-stream_loop','-1','-i',str(track)]
    if voice:
        cmd+=['-i',str(voice),'-filter_complex',f'[1:a]atrim=duration={duration},loudnorm=I=-27:TP=-3:LRA=6,afade=t=in:d=0.25,afade=t=out:st={max(0,duration-.8)}:d=0.8[bed];[2:a]apad=whole_dur={duration},atrim=duration={duration},loudnorm=I=-16:TP=-2:LRA=7,asplit=2[control][voice];[bed][control]sidechaincompress=threshold=0.025:ratio=6:attack=15:release=250[duck];[duck][voice]amix=inputs=2:normalize=0,alimiter=limit=0.89[mix]','-map','0:v:0','-map','[mix]']
    else:cmd+=['-map','0:v:0','-map','1:a:0','-af',f'atrim=duration={duration},loudnorm=I={level}:TP=-2:LRA=7,afade=t=in:d=0.25,afade=t=out:st={max(0,duration-.8)}:d=0.8']
    cmd+=['-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-t',str(duration),'-movflags','+faststart',str(output)]
    subprocess.run(cmd,check=True)
    report={'video':str(output),'duration':duration,'audio':score,'narration':voice or None,'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'hearing_review':'not completed by an actual listener'}
    (build/'render-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    return report
