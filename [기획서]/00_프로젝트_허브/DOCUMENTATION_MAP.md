# OMENWARD Documentation Map

## 기본 읽기 순서

`START_HERE.md` → `ACTIVE_CONTEXT.md` → 관련 1개 본책 → 해당 분야 스킬 → 실제 파일과 테스트 → `DEVELOPMENT_GATES.md` → `11_통합검수`.

## 질문별 책임 원본

| 질문 | 먼저 읽을 본책 | 기존 등록 부록 |
|---|---|---|
| 세계관·명칭·벨루 | 01 설정·내러티브 | `../02_게임_디자인/등록_부록/APPROVED_OMENWARD_WORLD_AND_NAMING.md`, `APPROVED_BELLU_MASCOT_AND_GUIDE_CONTRACT.md` |
| 룰렛·전장·병종·경제·튜토리얼 | 02 게임 디자인 | `../02_게임_디자인/02_게임_디자인_본책.md`와 같은 폴더의 등록 부록 |
| HUD·첫 10분·접근성 | 03 UX·UI·접근성 | `APPROVED_UI_ART_AUDIO_POC_BIBLE_V1.md` |
| Godot 구조·데이터·성능 | 04 개발·엔지니어링 | `../04_개발_엔지니어링/등록_부록/GODOT_PROJECT_STRUCTURE.md`, 성능·데이터 PoC |
| 임포트·애니메이션 계약·자산 연결 | 05 테크니컬 아트·콘텐츠 파이프라인 | 비주얼 형식·애니메이션 계약 |
| 아트 방향·승인 이미지 | 06 아트 | 아트 제작 기획서·이미지 인덱스 |
| BGM·SFX·음성 | 07 사운드 | UI·아트·오디오 PoC |
| 자동·수동 테스트 | 08 QA | `../08_QA/등록_부록/PHASE_0_VALIDATION.md`, `../08_QA/등록_부록/VERTICAL_SLICE_VALIDATION.md`, `tests/README.md` |
| 일정·Issue·위험·인수인계 | 09 프로덕션·PM | Roadmap, Handoff, Issue mirror |
| 벤치마킹·플레이어 반응 | 10 분석·유저리서치 | `../10_분석_유저리서치/10_분석_유저리서치_본책.md`와 등록 부록 |
| 릴리스 게이트·보존 대조 | 11 통합검수 | 이 허브의 Registry·보존표·검증 문서 |

`[백업]/`, `[보류]/`의 제안서·과거 work order·과거 issue는 기본 읽기 대상이 아니다. 재개나 이력 추적이 필요할 때만 연다.

## 전역 productivity 경계

`SKILL_REGISTRY.json`의 `global_productivity`는 Base `d2457e75a856260d309203e20262f2a2142d2dd6`와 `Base:skills/PRODUCTIVITY_SOURCE_MANIFEST.json`을 가리킨다. productivity 스킬을 이 저장소에 복사하지 않는다. 프로젝트 상태는 `ACTIVE_CONTEXT.md`와 프로젝트 Handoff, 임시 대화 인수인계는 전역 `handoff`, 이전 세션 재개는 전역 `resume-work`를 사용한다.
