#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,pathlib,re
ROOT=pathlib.Path(__file__).resolve().parents[1];DEFAULT_REGISTRY=ROOT/'docs'/'base'/'SKILL_REGISTRY.json'
REQ=('## 사용 조건','## 사용하지 않는 조건','## 고유 책임','## 입력','## 절차','## 출력','## 고유 검수')
def cycles(skills,errors):
 k={s['id']:s for s in skills};p=set();t=set()
 def v(i):
  if i in p:return
  if i in t:errors.append(f'circular dependency involving {i}');return
  t.add(i)
  for d in k[i].get('depends_on',[]):
   if d in k:v(d)
  t.remove(i);p.add(i)
 for i in k:v(i)
def validate(path,root=ROOT):
 e=[];r=json.loads(path.read_text(encoding='utf-8'));skills=r.get('skills',[]);ids=[s.get('id') for s in skills];paths=[s.get('path') for s in skills]
 if r.get('schema_version')!=4:e.append('schema_version must be 4')
 if len(ids)!=len(set(ids)):e.append('duplicate Skill IDs')
 if len(paths)!=len(set(paths)):e.append('duplicate Skill paths')
 active={s['id'] for s in skills if s.get('status','active')=='active'}
 if r.get('routing',{}).get('always_on'):e.append('always_on must be empty; route only by trigger or stage')
 for x in r.get('routing',{}).get('review_stack',[]):
  if x not in active:e.append(f'review_stack references inactive or unknown Skill: {x}')
 for old,new in r.get('aliases',{}).items():
  if old in active:e.append(f'alias shadows active Skill ID: {old}')
  if new not in active:e.append(f'alias target is inactive or unknown: {old} -> {new}')
 for s in skills:
  sid=s['id'];p=root/s['path']
  if not p.is_file():e.append(f'missing package: {s["path"]}');continue
  text=p.read_text(encoding='utf-8')
  if f'`{sid}`' not in text:e.append(f'Skill ID not declared in package: {sid}')
  if s.get('status','active')=='active':
   for sec in REQ:
    if sec not in text:e.append(f'missing section {sec}: {sid}')
   if re.search(r'\b(TODO|TBD|FIXME)\b',text):e.append(f'unfinished marker in {sid}')
   for d in s.get('depends_on',[]):
    if d not in active:e.append(f'active dependency must target active Skill: {d} in {sid}')
 cycles([s for s in skills if s.get('status','active')=='active'],e)
 actual={p.relative_to(root).as_posix() for p in (root/'skills').glob('*/*/SKILL.md')}
 if set(paths)!=actual:e.append(f'registry/package mismatch missing={sorted(set(paths)-actual)} orphan={sorted(actual-set(paths))}')
 return e
def main():
 p=argparse.ArgumentParser();p.add_argument('--registry',type=pathlib.Path,default=DEFAULT_REGISTRY);p.add_argument('--root',type=pathlib.Path,default=ROOT);a=p.parse_args()
 try:e=validate(a.registry,a.root)
 except Exception as x:e=[f'validator could not read contract: {x}']
 if e:
  print('Skill system validation FAILED');[print(f'- {x}') for x in e];return 1
 r=json.loads(a.registry.read_text());active=sum(s.get('status','active')=='active' for s in r['skills']);print(f'Skill system validation PASSED: {active} active / {len(r["skills"])} registered');return 0
if __name__=='__main__':raise SystemExit(main())
