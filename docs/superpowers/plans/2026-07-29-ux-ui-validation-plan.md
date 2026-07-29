# OMENWARD UX/UI Validation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** OMENWARD V2의 위협 예고→릴 설계→배치→전투→복기 UX를 제품 구현 전에 검증 가능한 정보 구조, fixture, 플레이 과제와 통과 기준으로 고정한다.

**Architecture:** 현재 `PLANNING_ONLY_PROFILE`과 V2 구현 미시작 상태를 유지한다. 먼저 3라인 위험 우선순위·릴 비교·비가역 배치·전투 인과의 사람 검증 계약을 작성하고, v6 기획과 사용자 승인이 완료된 뒤 별도 Codex Goal에서 최소 Vertical Slice를 구현한다.

**Tech Stack:** GitHub Markdown/Issues, Godot 4.7.1·GDScript는 후속 승인 단계에서만 사용, PC 1920×1080 및 1280×720 검증 기준.

## Global Constraints

- `docs/HANDOFF_CONTEXT.md`의 `PLAN`, `PLANNING_ONLY_PROFILE`, `PRODUCT_CODE_AUTHORIZED: NO`를 유지한다.
- V2 Godot 제품 구현과 Codex Build를 자동 진행하지 않는다.
- Legacy C1·C2·C3 증거를 V2 검증 통과로 사용하지 않는다.
- UI는 위협 우선순위·시너지·피해·배치 가능성을 재계산하지 않는다.
- 제품 코드·Scene·data·asset과 HTML 기획 대시보드는 변경하지 않는다.
- 미실행 사람 플레이·가독성·저장·성능은 `NOT_RUN` 또는 `HUMAN_QA_NOT_RUN`으로 유지한다.

---

### Task 1: V2 권한과 검증 범위 고정

**Files:**
- Read: `AGENTS.md`
- Read: `docs/HANDOFF_CONTEXT.md`
- Read: `docs/PROJECT_CORE.md`
- Read: `docs/UX_UI_SYSTEM.md`
- Read: `docs/BASE_UX_UI_ADOPTION.md`
- Read: GitHub Issue `#69`

**Interfaces:**
- Consumes: V2 코어, v6 기획 전환, Base UX/UI 패턴.
- Produces: 제품 구현을 포함하지 않는 UX 검증 Issue.

- [ ] **Step 1:** V2 구현 미시작, Legacy 증거의 역사적 지위, 제품 코드 비승인을 기록한다.
- [ ] **Step 2:** 플레이어 약속 `위협을 읽고 릴을 설계해 비가역 배치로 전황을 뒤집는다`를 검증 중심 문장으로 고정한다.
- [ ] **Step 3:** 1080p·720p, 키보드·마우스·게임패드, 3라인을 검증 축으로 기록한다.
- [ ] **Step 4:** Base main SHA와 프로젝트 UX 책임 원본을 명시한다.

### Task 2: 3라인 위협·릴·배치 fixture 정의

**Files:**
- Create after planning approval: `docs/validation/OMENWARD_UX_UI_FIXTURE_CATALOG.md`
- Read: `docs/design/APPROVED_CORE_V2_INTEGRATED_SPEC.md`
- Read: `docs/UX_UI_SYSTEM.md`

**Interfaces:**
- Consumes: V2 위협·릴·배치 계약.
- Produces: 화면·입력·사람 테스트가 공유하는 최소 상태 세트.

- [ ] **Step 1:** 세 라인 중 하나만 즉시 위험한 상태를 정의한다.
- [ ] **Step 2:** 두 라인의 위험 시점이 비슷해 우선순위 비교가 필요한 상태를 정의한다.
- [ ] **Step 3:** 릴 후보 두 개가 비용·제약·기대 효과에서 상충하는 상태를 정의한다.
- [ ] **Step 4:** 자원 부족, 배치 불가, 토큰 충돌 상태를 각각 정의한다.
- [ ] **Step 5:** 실행 전에는 되돌릴 수 있지만 커밋 뒤에는 되돌릴 수 없는 비가역 배치 상태를 정의한다.
- [ ] **Step 6:** 예상과 실제 결과가 달라지는 전투 사건을 정의하고 불확실성 원인을 기록한다.
- [ ] **Step 7:** 긴 한국어·최대 수치·모달·누락 자산 fixture를 정의한다.

### Task 3: Vertical Slice UX 과제 정의

**Files:**
- Create after planning approval: `docs/validation/OMENWARD_UX_UI_VALIDATION_PACKET.md`
- Read: `docs/UX_UI_SYSTEM.md`
- Read: `docs/HANDOFF_CONTEXT.md`

**Interfaces:**
- Consumes: Task 2 fixture.
- Produces: 위협→릴→배치→전투→복기 완주 과제.

- [ ] **Step 1:** 플레이어가 가장 임박한 위협과 그 근거를 설명하게 한다.
- [ ] **Step 2:** 릴 후보의 비용·제약·기대 효과를 같은 축으로 비교하게 한다.
- [ ] **Step 3:** 유효 위치·영향 범위·취소 경로를 확인하고 병력을 배치하게 한다.
- [ ] **Step 4:** 실행 전 전체 계획에서 확정·불확실 정보를 구분하게 한다.
- [ ] **Step 5:** 전투 중 가장 중요한 충돌과 전선 변화 원인을 추적하게 한다.
- [ ] **Step 6:** 결과 화면에서 위협→릴→배치→충돌→결과 인과를 설명하고 다음 설계 변경을 선택하게 한다.

### Task 4: 사람 테스트와 입력·가독성 기준 정의

**Files:**
- Create after planning approval: `docs/validation/OMENWARD_UX_UI_VALIDATION_PACKET.md`
- Update after execution: `docs/UX_UI_SYSTEM.md`

**Interfaces:**
- Consumes: Task 2~3.
- Produces: V2 Core Loop UX 판정.

- [ ] **Step 1:** 신규 플레이어 5명에게 10~15분 과제를 제공한다.
- [ ] **Step 2:** 5명 중 4명 이상이 최우선 위협과 선택 비용을 도움 없이 설명해야 통과하도록 정한다.
- [ ] **Step 3:** 5명 중 4명 이상이 배치 취소 가능 시점과 비가역 시점을 구분해야 통과하도록 정한다.
- [ ] **Step 4:** 5명 중 4명 이상이 패배 원인과 다음 릴·배치 변경을 연결해야 통과하도록 정한다.
- [ ] **Step 5:** 1920×1080과 1280×720에서 핵심 위험·비용·입력 상태가 겹치거나 잘리지 않아야 통과하도록 정한다.
- [ ] **Step 6:** 키보드·마우스·게임패드 각각 준비→배치→실행→복기를 완주하고 모달 종료 뒤 의미 위치로 포커스가 돌아와야 통과하도록 정한다.

### Task 5: V2 구현 진입 Gate 정의

**Files:**
- Update after user approval: `docs/HANDOFF_CONTEXT.md`
- Update after user approval: `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- Create after user approval: 별도 Codex Goal Issue

**Interfaces:**
- Consumes: v6 기획 승인과 Task 2~4 검증 계약.
- Produces: V2 최소 제품 구현 범위.

- [ ] **Step 1:** 사용자 승인 전 `PRODUCT_CODE_AUTHORIZED: NO`를 유지한다.
- [ ] **Step 2:** 승인 후 실제 HUD·릴·배치 Scene과 View Data·Signal 소유자를 읽기 전용으로 조사한다.
- [ ] **Step 3:** 최소 구현 범위를 위협 예고, 릴 비교, 배치, 실행 전 검토, 전투 인과, 복기로 제한한다.
- [ ] **Step 4:** Legacy 서비스 전환·경제·저장·전체 10병종은 별도 구현 패키지로 분리한다.
- [ ] **Step 5:** 자동 계약, Godot 런타임, 입력·가독성, 사람 플레이를 독립 증거로 보고한다.

## Verification Commands

현재 계획 PR은 저장소 문서·Skill 검증만 실행한다.

```bash
python tools/validate_project_core_docs.py
python -m unittest tests.test_skill_system -v
```

V2 런타임과 사람 검증은 사용자 승인 뒤 별도 Issue에서만 실행한다.
