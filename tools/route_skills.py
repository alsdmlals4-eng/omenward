#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,pathlib,re,sys
from dataclasses import dataclass
from typing import Iterable
ROOT=pathlib.Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY=ROOT/'docs'/'base'/'SKILL_REGISTRY.json'
WORDS={'REVIEW':('검토','검수','리뷰','감사','누락','중복','review','validate','audit','pull request'),'BUILD':('구현','수정','고쳐','추가','삭제','리팩터','build','implement','fix','add','remove','refactor'),'PLAN':('기획','계획','제안','설계','분석','plan','proposal','design','analyze')}
@dataclass(frozen=True)
class Match: skill_id:str; score:int; category:str; priority:int
def normalize(text:str)->str:return re.sub(r'\s+',' ',text.casefold()).strip()
def contains_any(text:str,words:Iterable[str])->bool:return any(normalize(w) in text for w in words)
def infer_mode(request:str)->str:
 t=normalize(request);scores={m:sum(1 for w in ws if normalize(w) in t) for m,ws in WORDS.items()}
 return max(('REVIEW','BUILD','PLAN'),key=lambda m:(scores[m],{'REVIEW':2,'BUILD':1,'PLAN':0}[m])) if any(scores.values()) else 'PLAN'
def score_skill(request:str,skill:dict)->int:
 t=normalize(request);score=sum(max(1,len(normalize(x).split())) for x in skill.get('triggers',[]) if normalize(x) in t)
 score-=sum(10 for x in skill.get('not_use_when',[]) if normalize(x) in t)
 return score
def resolve_id(skill_id:str,registry:dict)->str:return registry.get('aliases',{}).get(skill_id,skill_id)
def _dependency_first_order(selected,known):
 out=[];perm=set();temp=set()
 def visit(i):
  if i in perm:return
  if i in temp:raise ValueError(f'Circular Skill dependency: {i}')
  temp.add(i)
  for d in known[i].get('depends_on',[]):
   if d not in known:raise ValueError(f'Unknown dependency {d} in {i}')
   visit(d)
  temp.remove(i);perm.add(i);out.append(i)
 for i in selected:visit(i)
 return out
def route(request,registry,forced_mode=None,forced_skills=None):
 mode=forced_mode or infer_mode(request)
 active=[s for s in registry['skills'] if s.get('status','active')=='active' and mode in s.get('modes',registry['routing']['work_modes'])]
 known={s['id']:s for s in active};selected=[];reasons={}
 def add(raw,reason):
  i=resolve_id(raw,registry)
  if i not in known:raise ValueError(f'Unknown or inactive Skill ID: {raw}')
  if i not in selected:selected.append(i);reasons[i]=reason
 matches=[]
 for s in active:
  sc=score_skill(request,s)
  if sc>0:matches.append(Match(s['id'],sc,s['category'],s['priority']))
 matches.sort(key=lambda m:(-m.score,-m.priority,m.skill_id))
 ds=[m for m in matches if m.category=='disciplines']
 if ds:
  add(ds[0].skill_id,f'primary_discipline score={ds[0].score}')
  for m in ds[1:1+registry['routing']['max_support_disciplines']]:add(m.skill_id,f'support_discipline score={m.score}')
 for m in matches:
  if m.category in ('foundation','specialists'):add(m.skill_id,f'{m.category[:-1]}_trigger score={m.score}')
 if mode=='REVIEW':
  for i in registry['routing']['review_stack']:add(i,'review_stack')
 for i in forced_skills or []:add(i,'manual_override')
 ordered=_dependency_first_order(selected,known)
 for i in ordered:reasons.setdefault(i,'dependency')
 return {'request':request,'mode':mode,'skills':[{'id':i,'reason':reasons[i],'path':known[i]['path']} for i in ordered]}
def load_registry(path):return json.loads(path.read_text(encoding='utf-8'))
def main():
 p=argparse.ArgumentParser();p.add_argument('--request',required=True);p.add_argument('--registry',type=pathlib.Path,default=DEFAULT_REGISTRY);p.add_argument('--mode',choices=('PLAN','BUILD','REVIEW'));p.add_argument('--skill',action='append',default=[]);a=p.parse_args()
 try:r=route(a.request,load_registry(a.registry),a.mode,a.skill)
 except (OSError,ValueError,json.JSONDecodeError) as e:print(f'ERROR: {e}',file=sys.stderr);return 2
 print(json.dumps(r,ensure_ascii=False,indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
