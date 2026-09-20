#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,pathlib,re,sys
from dataclasses import dataclass
from typing import Iterable
ROOT=pathlib.Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY=ROOT/'skills'/'SKILL_REGISTRY.json'
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
 if registry.get('registry_role')=='omenward-project-local-skill-registry':
  return route_current(request,registry,forced_mode,forced_skills)
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
def load_registry(path):
 value=json.loads(path.read_text(encoding='utf-8'))
 value['_registry_path']=str(path.resolve())
 return value

def route_current(request,registry,forced_mode=None,forced_skills=None):
 """Select available routes, not implicit legacy dependencies or approval grants."""
 root=pathlib.Path(registry['_registry_path']).parent.parent
 if __package__:
  from .validate_skill_system import validate
 else:
  from validate_skill_system import validate
 errors=validate(pathlib.Path(registry['_registry_path']),root)
 if errors:raise ValueError('; '.join(errors))
 adapter=load_registry(root/'skills/PROJECT_BASE_ADAPTER.json')
 snapshot=load_registry(root/'skills/PROJECT_SKILL_SNAPSHOT.json')
 policy=adapter['shared_overrides']['managing-game-project-operating-system']['project_routing']
 known={s['skill_id']:s for s in registry['skills'] if s['status']=='ACTIVE'}
 effective=snapshot['effective_routes']
 mode=forced_mode or infer_mode(request)
 text=normalize(request)
 selected=[]
 # Registry/adapter own availability; triggers only rank candidates.
 for group in policy['trigger_groups']:
  if any((re.search(r'(?<![a-z0-9_])'+re.escape(normalize(term))+r'(?![a-z0-9_])',text)
          if term.isascii() else normalize(term) in text) for term in group['terms']):
   selected.extend(group['routes'])
   if group.get('exclusive'):break
 if not selected:
  selected=[policy['fallback'][mode]]
 selected.extend(forced_skills or [])
 results=[]
 for sid in dict.fromkeys(selected):
  entry=effective.get(sid)
  if not entry or entry['status']!='ACTIVE':raise ValueError(f'Unknown or inactive Skill ID: {sid}')
  if entry['source']=='PROJECT_LOCAL':
   skill=known.get(entry['skill_id'])
   if not skill:raise ValueError(f'Missing local registration: {sid}')
   path=(root/'skills'/skill['path']).resolve()
   if not path.is_relative_to((root/'skills').resolve()) or not path.is_file():
    raise ValueError(f'Invalid local package: {sid}')
   results.append({'id':sid,'path':path.relative_to(root).as_posix(),'source':'PROJECT_LOCAL'})
  else:
   override=adapter['shared_overrides'].get(sid,{}).get('selected_source')
   revision=override['commit'] if override else adapter['base_release']['release_commit']
   path=override['path'] if override else f'skills/{entry["skill_id"]}/SKILL.md'
   results.append({'id':sid,'path':path,'source':'BASE_SHARED','commit':revision,
                   'url':f'https://github.com/{adapter["base_release"]["repository"]}/blob/{revision}/{path}'})
 return {'request':request,'mode':mode,'authority':'skills/PROJECT_BASE_ADAPTER.json',
         'authorization':'READ_ROUTE_ONLY__USE_CURRENT_APPROVED_SCOPE','skills':results}
def main():
 p=argparse.ArgumentParser();p.add_argument('--request',required=True);p.add_argument('--registry',type=pathlib.Path,default=DEFAULT_REGISTRY);p.add_argument('--mode',choices=('PLAN','BUILD','REVIEW'));p.add_argument('--skill',action='append',default=[]);a=p.parse_args()
 try:r=route(a.request,load_registry(a.registry),a.mode,a.skill)
 except (OSError,ValueError,KeyError,TypeError) as e:print(f'ERROR: {e}',file=sys.stderr);return 2
 print(json.dumps(r,ensure_ascii=False,indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
