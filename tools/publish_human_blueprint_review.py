"""Build the review edition from repository-owned narrative and data. No runtime writes."""
from pathlib import Path
import json, hashlib, math, re
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from PIL import Image
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'docs/design/OMENWARD_BLUEPRINT_BUILD_INPUT_20260911.json'
SOURCE = ROOT / 'docs/design/OMENWARD_HUMAN_BLUEPRINT_REVIEW_20260911.md'
OUT = ROOT / 'output/pdf/OMENWARD_HUMAN_BLUEPRINT_REVIEW_20260911_v3.pdf'
ASSETS = ROOT / 'docs/images/candidates/blueprint-20260911'
W,H = 960,640
NAVY, GOLD = colors.HexColor('#20384a'), colors.HexColor('#a78039')
pdfmetrics.registerFont(TTFont('Korean','C:/Windows/Fonts/malgun.ttf'))
pdfmetrics.registerFont(TTFont('KoreanBold','C:/Windows/Fonts/malgunbd.ttf'))
STYLE = ParagraphStyle('body',fontName='Korean',fontSize=12,leading=19,textColor=NAVY,wordWrap='CJK',spaceAfter=14)
SMALL = ParagraphStyle('small',parent=STYLE,fontSize=10,leading=15)
data=json.loads(DATA.read_text(encoding='utf-8'))
OUT.parent.mkdir(parents=True,exist_ok=True)
c=canvas.Canvas(str(OUT),pagesize=(W,H))
c.setTitle('OMENWARD 사람용 블루프린트 · 검토판 2026-09-11')
pages=[]
def page(title, tag='기획 검토판 · 제품 구현 전'):
    if pages:c.showPage()
    pages.append(title)
    c.setFillColor(colors.HexColor('#f6f2e9'));c.rect(0,0,W,H,fill=1,stroke=0)
    c.setFillColor(NAVY);c.rect(0,H-86,W,86,fill=1,stroke=0)
    c.setFillColor(colors.white);c.setFont('KoreanBold',23);c.drawString(38,H-45,title)
    c.setFont('Korean',10);c.drawString(40,H-67,tag)
    c.setStrokeColor(GOLD);c.line(38,40,W-38,40)
    c.setFillColor(NAVY);c.setFont('Korean',9)
    c.drawString(38,24,'OMENWARD | 사용자 확정 방향 + 권장 설계 / 수치·자산·UX 최종 검증 전')
    c.drawRightString(W-38,24,f'{len(pages):02d}')
    return H-110
def para(text,x,y,width=W-80,style=STYLE):
    p=Paragraph(escape(text).replace('\n','<br/>'),style);pw,ph=p.wrap(width,H)
    if y-ph<53:raise ValueError(f'Page overflow: {pages[-1]} {y-ph}')
    p.drawOn(c,x,y-ph);return y-ph-14
def table(rows,y,widths):
    cells=[[Paragraph(escape(str(v)),SMALL) for v in row] for row in rows]
    t=Table(cells,colWidths=widths,hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e2d6bc')),('VALIGN',(0,0),(-1,-1),'TOP'),('BOTTOMPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('LINEBELOW',(0,0),(-1,-1),.4,colors.HexColor('#b8b8ad'))]))
    tw,th=t.wrap(W-80,H)
    if y-th<53:raise ValueError(f'Table overflow: {pages[-1]} {th}')
    t.drawOn(c,40,y-th);return y-th-14
def picture(path,x,y,w,h):c.drawImage(str(path),x,y,width=w,height=h,preserveAspectRatio=True,anchor='c',mask='auto')
def tile(filename,index,cols,rows,x,y,size):
    # PDF viewport only: source PNG is never cropped or modified.
    c.saveState();p=c.beginPath();p.rect(x,y,size,size);c.clipPath(p,stroke=0)
    c.drawImage(str(ASSETS/filename),x-(index%cols)*size,y-(rows-1-index//cols)*size,width=size*cols,height=size*rows)
    c.restoreState()

y=page('01 · 화면 아틀라스','6개 주요 화면의 정보 구조 · 실제 실행 캡처가 아닌 편집 가능한 와이어프레임')
screens=[('메인','새 원정 / 이어하기 / 설정'),('맵 선택','5개 순차 맵 / 라운드 / 해금'),('룰렛','공급 풀 / 3×3 결과 / 이동 / 확정'),('내정','6+점령지 슬롯 / 생산 / 치료'),('전선','상단 한 줄 맵 / 공세 / 단일 전투'),('결과·재정비','손실 / 보상 / 다음 공세 / 시작')]
for i,(title,desc) in enumerate(screens):
    x=40+(i%3)*298; yy=302-(i//3)*232
    c.setFillColor(colors.white);c.roundRect(x,yy,282,214,8,fill=1,stroke=0)
    if i in [0,4]: picture(ASSETS/'battlefield-layer.png',x+8,yy+62,266,135)
    else:
        c.setFillColor(colors.HexColor('#ede5d5'));c.rect(x+8,yy+62,266,135,fill=1,stroke=0)
    c.setFont('Korean',8)
    labels = [['새 원정','이어하기','설정'],['성채','전진','접전','장막','베일'],['방패','궁병','빈칸','궁병','마법','방패','빈칸','방패','궁병'],['병영','사격장','빈 슬롯','빈 슬롯','빈 슬롯','빈 슬롯','잠금','잠금'],['성채 → 전진 → 접전 → 장막 → 베일'],['생존 승리','손실 2 / 생존 6','보급 +15','다음 라운드']][i]
    for j,label in enumerate(labels):
        cols=3 if i==2 else (2 if i==3 else 1)
        bx=x+18+(j%cols)*(80 if i==2 else 124);by=yy+145-(j//cols)*(20 if i==1 else 24)
        bw=72 if i==2 else (116 if i==3 else 244)
        c.setFillColor(colors.HexColor('#d9c89f'));c.roundRect(bx,by,bw,20,3,fill=1,stroke=0)
        c.setFillColor(NAVY);c.drawString(bx+5,by+6,label)
    c.setFillColor(NAVY);c.rect(x+8,yy+174,266,23,fill=1,stroke=0)
    c.setFillColor(colors.white);c.setFont('KoreanBold',12);c.drawString(x+16,yy+180,title)
    para(desc,x+12,yy+52,258,SMALL)
    c.setFillColor(GOLD);c.rect(x+12,yy+14,92,17,fill=1,stroke=0)
    c.setFillColor(NAVY);c.setFont('Korean',9);c.drawString(x+16,yy+19,'주요 행동 / 상태')

sections=re.split(r'^## ',SOURCE.read_text(encoding='utf-8'),flags=re.M)[1:]
for section in sections:
    title,body=section.split('\n',1);y=page(title)
    for block in body.strip().split('\n\n'):
        p=Paragraph(escape(block),STYLE);_,height=p.wrap(W-80,H)
        if y-height<58:y=page(title+' · 계속')
        y=para(block,40,y)

y=page('시스템 연결 · 누가 무엇을 소비하는가')
y=table([['원인 / 입력','책임 서비스 후보','결과 / 소비처'],['공세 표·고정 tick','RoundDirector / WaveScheduler','BattleSimulator · 상단 예고'],['건물·점령 소유권','BuildingService / SupplyPool','생산 대기열 · 룰렛 풀 snapshot'],['룰렛 결과·조작','RouletteResolver / RewardTransaction','확정 병력 · 슬롯/골드 원장'],['병종 능력·표적','TargetPolicy / EffectResolver','피해·치료·점령 · 모션 event'],['phase·모든 잔여 상태','RunSnapshot / SaveRepository','이어하기 · 맵 재도전'],['실제 사건 로그','ReviewPresenter','손실·기여·다음 준비 정보'] ],y,[230,310,340])
para('기존 클래스명에 그대로 기능이 있다는 뜻이 아니다. 승인 후 실제 consumer에 맞춰 책임을 이관한다. UI 애니메이션이 피해·보상 판정을 다시 발생시키지 않는다.',40,y)

for idx,u in enumerate(data['units']):
    page('병종 도감 · '+u[1]+' / '+u[3],'일반 진영 / 베일 · 도감 카드용 후보 · 전투 모션/투명 sprite 아님')
    if idx<8:
        tile('ward-roster.png',idx,4,2,70,165,340)
        tile('veil-roster.png',idx,4,2,540,165,340)
    else:
        tile('special-roster-additions.png',idx-8,2,2,70,165,340)
        tile('special-roster-additions.png',idx-6,2,2,540,165,340)
    para('아군: '+u[1],70,145,340)
    para('베일: '+u[3],540,145,340)
    para('동일 역할을 무기와 괴물 기관으로 구분한다. 시트 경계의 무기 여백은 개별 납품 전에 재검수한다.',40,95,style=SMALL)
    y=page('병종 명세 · '+u[1], '권장 초기 데이터 · 아군/베일 대응 역할 · 이미지 상태군 미완료')
    family='일반병종' if u[0] in data['unit_families']['general'] else '특수병종'
    y=para(f'{family} | 역할: {u[2]} | 베일 대응: {u[3]} | 식별자: {u[0]}',40,y)
    y=table([['HP','공격','물리 방어','마법 저항','이동','사거리','주기','출전비용','충원 기준가'],u[4:13]],y,[98]*8+[96])
    y=para('고유 처리: '+u[13],40,y);y=para('약점: '+u[14],40,y)
    y=para('상태군: idle / move / attack 또는 cast / hit / death. 준비 → 타격 event → 회복으로 연결하고, 사망 이후 예약 타격은 취소한다. 투사체는 발사 시점의 진영과 발사자 ID를 유지한다.',40,y)
    pr=next(v for v in data['unit_progression'] if v[0]==u[0])
    y=table([['해금 / 등급','스킬'],['최초 T'+str(pr[1])+' / 일반',pr[2]],['숙련: 2라운드 생존',pr[3]],['정예: 5라운드 생존',pr[4]],['베일 대응',pr[5]]],y,[210,670])

bn={b[0]:b[3] for b in data['building_tree']}
un={u[0]:u[1] for u in data['units']}
un['random_special']='특수병 5종 고정 추첨'
for root,title in [('barracks','일반병 병영'),('special_barracks','특수병 병영')]:
    y=page('별도 계열 · '+title)
    nodes=[b for b in data['building_tree'] if b[0]==root or b[1]==root]
    y=table([['티어 / 시설','필요 부모','공급 병종','추가 G','생산 초']]+[[f'T{b[2]} {b[3]}',bn.get(b[1],'신규 건설'),un[b[4]],b[5],next(v[5] for v in data['buildings'] if v[0]==b[0])] for b in nodes],y,[240,190,210,100,140])
    para('두 계열 사이 업그레이드 전환은 없다. T2 선택 후 T3는 동일 병종 심화 하나로 이어진다. 가격과 특수병 T1 추첨/토큰 규칙은 추천안이다. 슬롯 상실 시 건물과 레벨은 보존한다.',40,y)
y=page('T3 심화 · T2 병종 정체성을 유지')
y=table([['T2 병종','T3 명칭','추가 효과']]+[[un[row[0]],row[1],row[2]] for row in data['capstones']],y,[130,190,560])
para('T3 비용 ceil(T2 전문화 비용 × 1.25). 새 생산부터 적용하며 기존 병력은 소급 승급하지 않는다.',40,y,style=SMALL)
building_art={'barracks':0,'spear_hall':1,'range':2,'academy':3,'chapel':4,'blade_hall':5,'stable':6,'siege':7}
for i,b in enumerate(data['building_tree']):
    if b[0] not in building_art:continue
    y=page('건물 도감 · '+b[3], '내정 목록 카드 전용 · 전장 건설 노드로 사용하지 않음')
    tile('building-tree.png',building_art[b[0]],4,2,45,100,410)
    y=para(f'T{b[2]} / 부모: '+bn.get(b[1],'없음')+'\n공급: '+un[b[4]]+f'\n추가 비용: {b[5]}G',485,y,425)
    y=para('변경 예고 → 비용/활성 슬롯 검사 → 건물·공급 풀 동시 갱신 → 생산 진행 초기화. 기존 병력·확정 보상은 유지한다.',485,y,425)
    para('이미지는 목록용 원화 후보다. 건물 선택/잠금/비활성 상태는 UI가 표시한다. 군수소 별도 이미지와 소규모 표시 가독성은 후속 작업이다.',485,y,425)
for i,h in enumerate(data['heroes']):
    y=page('영웅 후보 · '+h[1], '원정당 1명 선택 권장안 · 이름/능력/수치는 최종 확정 전')
    tile('heroes.png',i,3,1,40,100,400)
    y=para(h[2]+f' | HP {h[5]} / 공격 {h[6]} / 사거리 {h[7]}',465,y,445)
    y=para('패시브: '+h[3],465,y,445)
    y=para('능동기: '+h[4],465,y,445)
    para('도감용 신체 비율이 일반 SD 병사보다 길다. 전투용은 별도 SD 제작·모션 검수가 필요하다. 현재 코드는 고유 영웅 시스템을 구현하지 않았다.',465,y,445)

name={u[0]:u[1] for u in data['units']}; fixtures=[]
for m in data['maps']:
    y=page('맵 공세 데이터 · '+m['name'],f"{m['rounds']}라운드 / 각 60초 / 공세 5·22·40초 / 압박계수 {m['pressure']}")
    rows=[['라운드','5초','22초','40초']]
    for r in range(m['rounds']):
        waves=[]
        for j in range(3):
            code=data['wave_cycle'][(r+j)%len(data['wave_cycle'])]
            entries=[[uid,math.ceil(n*m['pressure']*(1+.03*r))] for uid,n in data['wave_templates'][code]]
            fixtures.append({'map':m['id'],'round':r+1,'second':[5,22,40][j],'units':entries})
            waves.append(' / '.join(name[uid]+str(n) for uid,n in entries))
        rows.append([r+1]+waves)
    y=table(rows,y,[70,270,270,270]);para(m['theme']+' · 학습 목표: '+m['lesson'],40,y,style=SMALL)

y=page('자산 아틀라스 · 전투 배경 레이어','GENERATED_CANDIDATE · 제품 미적용 · 최종 승인 전')
picture(ASSETS/'battlefield-layer.png',40,150,880,380)
para('소비처 후보: 전선 화면의 배경 Sprite2D/TextureRect. 이동로를 가로막는 전경 오브젝트는 별도 제작한다. 이 한 장이 다섯 맵 전체를 대체하지 않는다. 배경에 병력·텍스트·건설 UI를 굽지 않는다.',40,135)
y=page('자산 아틀라스 · UI 아이콘 16종','불투명 정사각 타일 · 자유 배치 투명 소품과 구별')
picture(ASSETS/'ui-icons.png',40,73,460,460)
para('1행 방패 / 궁병 / 마법 / 지원\n2행 창 / 대검 / 기병 / 공성\n3행 병영 / 사격장 / 학당 / 성소\n4행 골드 / 점령 / 잠금 / 룰렛\n\nGodot AtlasTexture.region으로 분할한다. 1254px는 4로 나누어떨어지지 않으므로 경계 floor(i×1254/4)를 쓴다. filter_clip을 켜고 축소 시 인접 셀 유입을 확인한다. 런타임 미검증.',525,510,390)
y=page('자산 준비도 · 빈칸을 완성으로 표시하지 않는다')
table([['자산','현재 상태','다음 게이트'],['전투 배경 1장','후보 PNG','맵별 5종 · 이음새 · 배치 검수'],['UI 아이콘 16종','불투명 atlas 후보','상태/축소 가독성 · user approval'],['아군/베일 각 8역할','불투명 도감 시트 후보','개별 경계 · 투명 전투 원화'],['건물 8종/영웅 3명','목록/선택 카드 후보','군수소 · 영웅 SD 비율'],['양 진영 모션','전체 상태군 미완료','발 피벗/타격 시각/SpriteFrames'],['방어탑·분리 소품','미제작','이동로 밖 배치 · 점령 색'],['실제 Godot 화면','새 설계 NOT_RUN','최종 기획 승인 후 구현·촬영']],y,[190,300,390])

for offset in range(0,len(data['sources']),7):
    y=page('조사 출처 · 채택 / 변형 / 제외', '공식 설명 기반 벤치마킹 · 직접 플레이 실험이나 인터뷰 아님')
    for title,url,decision in data['sources'][offset:offset+7]:
        y=para(title+' — '+decision+'\n'+url,40,y,style=SMALL)

c.save()
manifest=[]
for filename in ['battlefield-layer.png','ui-icons.png','ward-roster.png','veil-roster.png','building-tree.png','heroes.png','special-roster-additions.png']:
    p=ASSETS/filename
    with Image.open(p) as im: size=list(im.size);mode=im.mode
    manifest.append({'path':p.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'size':size,'mode':mode,'state':'GENERATED_CANDIDATE','runtime':'NOT_RUN','tool':'image_gen','approval':'PENDING'})
reader=PdfReader(OUT); assert len(reader.pages)==len(pages)
assert len(fixtures)==159 and sum(m['rounds'] for m in data['maps'])==53
assert len(data['unit_progression'])==len(data['units'])==10
assert len(data['heroes'])==3
assert len({b[0] for b in data['building_tree']})==12
for b in data['building_tree']:
    assert b[4] in un
    assert b[1] is None or any(p[0]==b[1] and p[2]==b[2]-1 for p in data['building_tree'])
assert [b[4] for b in data['building_tree'] if b[2]==1]==['shield_guard','random_special']
assert 4*max(u[11] for u in data['units'])<=data['economy']['queue_capacity']
assert all(p.extract_text().strip() for p in reader.pages)
receipt={'status':'REVIEW_EDITION','pages':pages,'page_count':len(pages),'pdf_sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),'sources':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in [SOURCE,DATA]},'assets':manifest,'rounds':53,'waves':159,'static_layout':'PASS','runtime':'NOT_RUN','human':'NOT_RUN','visual_review':'PENDING'}
OUT.with_suffix('.receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'pdf':str(OUT),'pages':len(pages),'waves':len(fixtures)},ensure_ascii=False))
