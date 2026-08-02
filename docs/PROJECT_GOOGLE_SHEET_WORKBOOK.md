# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-03
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
current_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TIMER-PERSISTENCE-AND-STAGE-BOUNDARY-POLICY-V1
current_pr: 129
current_branch: gpt/omenward-hero-kit-planning-20260802
current_pr_head: RESOLVE_FROM_PR_129
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
status: PROJECT_SHEET_CONFIGURED / SYNC_REQUIRED_TO_PR_HEAD / READBACK_REQUIRED / CI_REQUIRED / COUNTER_9_OF_10
product_code_authority: NONE
```

이 문서는 GitHub 정본과 연결 Google Sheet의 동기화 계약을 소유한다. PR HEAD는 자기참조 commit을 만들지 않도록 GitHub PR #129와 Sheet에서 해석한다.

## 1. 이번 Decision

```text
ACTIVE_COMBAT
→ warmup·cooldown 진행

MAINTENANCE / PREPARATION / ROULETTE / BUILD
→ timer pause
→ READY 유지

NEXT_STAGE_ACTIVE_COMBAT
→ 동일 생존 영웅 인스턴스 상태 재개
```

- Stage·Act 전환 초기화 없음.
- READY·남은 warmup·cooldown carry.
- owner-bound active effect는 전투 종료 시 정리하고 full cooldown.
- 미해결 천공 소거·메테오 commit은 취소, 사용 소비, full cooldown.
- save/load·Retry 재굴림·이중 해결 금지.

## 2. 예정 Sheet 반영 범위

| 목적 | 범위 |
|---|---|
| 프로젝트 Hub·카운터·HEAD | `00_프로젝트_허브!E2:L2` |
| 작업순서 | `01_작업순서!A37:N37` |
| 확정 Decision | `02_현재_확정결정!A45:M45` |
| 벤치마크 근거 | `03_근거_라이브러리!A22:J24` |
| 적대적 감사 | `04_누락_충돌_감사!A182:H190` |
| GDD 상태 요약 | `05_GDD_요약!D8:J8`, `05_GDD_요약!B9:J9` |
| 핵심루프 | `12_핵심루프!A20:J20` |
| 조작·게임 규칙 | `15_조작_게임규칙!A23:J23` |
| 핵심 시스템 | `40_핵심시스템_메인콘텐츠!A23:J23` |
| 성장·경제 경계 | `41_성장_경제!A33:I33` |
| encounter 검증 | `50_메인콘텐츠!A30:J30` |
| UX·접근성 | `60_UX_UI_접근성!A31:J31` |
| 아트·오디오 | `70_아트_오디오_에셋!A14:J14` |
| 변경 이력 | `99_변경이력!A48:H48` |

## 3. 근거 라이브러리

예정 Evidence:

- `OM-EVD-021`: Godot stable `Pausing games and process mode` — 전투 clock과 정비 UI clock 분리 production reference.
- `OM-EVD-022`: Godot stable `Saving games` — timer state·commit payload 명시적 직렬화 production reference.
- `OM-EVD-023`: 내부 timer Stage-boundary 비교 — carry/pause가 reset·maintenance-progress보다 exploit과 상태 복잡도가 낮음.

직접 동일한 상용 사례는 확인하지 못했으므로 `DIRECT_COMPARABLE_NOT_FOUND`를 기록한다.

## 4. 적대적 감사

예정 감사 ID:

```text
OMW-AUD-182 정비시간 무료 cooldown 회복
OMW-AUD-183 Stage 초기화 exploit
OMW-AUD-184 지속효과 다음 Stage 이월
OMW-AUD-185 미해결 commit 새 Stage 재타깃
OMW-AUD-186 짧은 전투에서 스킬 무가치화
OMW-AUD-187 전투 종료 직전 commit 손실
OMW-AUD-188 save/load 이중 해결
OMW-AUD-189 Act 전환 숨은 초기화
OMW-AUD-190 timer pause 이유 UX 불명확
```

## 5. 쓰기·검증 절차

```text
1. 대상 범위 bounded read
2. 기존 서식·검증 확인
3. 같은 Decision ID로 batch update
4. 동일 범위 bounded read-back
5. exact PR HEAD CI 3종 확인
6. latest main compare
7. changed path·review·thread 확인
8. OPEN_P0·OPEN_P1·MERGE_BLOCKER 검색
9. Sheet에 exact HEAD·run 번호 마감
10. PR 설명 갱신
```

## 6. 필수 CI

```text
Validate Project Core Documentation
Validate Omenward GDD Sheet Adoption
Validate Base v9 adoption
```

모두 exact PR HEAD에서 `success`여야 `CI_3_GREEN`으로 기록한다.

## 7. blocker 검색

`04_누락_충돌_감사!A1:H300`에서 다음 문자열의 실제 데이터 행을 검색한다.

```text
OPEN_P0
OPEN_P1
MERGE_BLOCKER
```

헤더 외 일치 행이 없어야 한다.

## 8. 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SHEET_WRITES = PLANNING_DATA_ONLY
EXACT_SECONDS = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 9. 카운터

```text
GRILL_ME_COUNT = 9/10
NEXT_GATE = OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
```

10/10에서 fresh preflight를 실행하고 Green이면 standing user authorization에 따라 문서 PR을 병합한다.
