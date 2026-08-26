#!/usr/bin/env python3
"""Export approved HUD resource masters as compact transparent icons."""
import argparse, hashlib, json
from pathlib import Path
from PIL import Image

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--project-root',type=Path,required=True); parser.add_argument('--manifest',type=Path,required=True); parser.add_argument('--report',type=Path,required=True); args=parser.parse_args()
    root=args.project_root.resolve(); manifest=json.loads(args.manifest.read_text(encoding='utf-8')); results=[]
    for entry in manifest['entries']:
        source=root/entry['source']; output=root/entry['output']
        if output.exists(): raise FileExistsError(output)
        image=Image.open(source).convert('RGBA'); bounds=image.getchannel('A').getbbox()
        if bounds is None: raise ValueError(source)
        crop=image.crop(bounds); scale=min(48/crop.width,48/crop.height); scaled=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.NEAREST)
        canvas=Image.new('RGBA',(64,64),(0,0,0,0)); offset=((64-scaled.width)//2,(64-scaled.height)//2); canvas.alpha_composite(scaled,offset); output.parent.mkdir(parents=True,exist_ok=True); canvas.save(output)
        if any(a not in (0,255) for a in canvas.getchannel('A').get_flattened_data()): raise ValueError('partial alpha')
        results.append({'id':entry['id'],'source':entry['source'],'source_sha256':digest(source),'output':entry['output'],'output_sha256':digest(output),'source_alpha_bounds':list(bounds),'canvas_size':[64,64],'scaled_size':list(scaled.size)})
    args.report.write_text(json.dumps({'record_id':manifest['record_id'],'entries':results},indent=2)+'\n',encoding='utf-8')
if __name__=='__main__': main()
