# Roulette Agency Synthetic Remediation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 룰렛 사람 검증 Artifact에서 결과 utility 혼합·사후 귀인·비가역 결정 중첩을 제거한다.

**Architecture:** 카드 시나리오만 수정하고 Vertical Slice 정본과 제품 경로는 유지한다. 결과 쌍은 동일 token multiset·동일 연구 utility를 유지한 채 위치·출처 적합도만 바꾸며, 결과 공개 전에 통제·비통제 범위와 예상 결과 범위를 기록한다.

**Tech Stack:** Markdown 연구 계약, Project Core Documentation CI

## Global Constraints

- `SYNTHETIC_RISK_REVIEW`는 `LOOP_PROVEN`이 아니다.
- `human_validation: NOT_RUN`, `vertical_slice_implementation: NOT_STARTED`, `implementation_authority: NONE` 유지.
- 별도 Core PoC·Godot·Scene·Resource·제품 수치 생성 금지.

---

### Task 1: Artifact 교정

**Files:**
- Modify: `docs/superpowers/plans/2026-07-29-roulette-agency-validation-artifact.md`

**Interfaces:**
- Consumes: `docs/research/OMENWARD_ROULETTE_AGENCY_SYNTHETIC_TESTER_REPORT_2026-07-29.md`
- Produces: matched-utility 카드 쌍, pre-result prediction, 단계형 비가역 결정

- [ ] **Step 1:** current main·Base Governance metadata를 갱신한다.
- [ ] **Step 2:** FAVORABLE/UNFAVORABLE 명칭을 제거하고 동일 token multiset의 matched-utility pair로 교체한다.
- [ ] **Step 3:** 결과 공개 전 통제 요소·잔여 RNG·예상 범위를 기록한다.
- [ ] **Step 4:** 시나리오 1은 구조 변경, 2는 영구 이동, 3은 전선 커밋 순으로 비가역 결정을 단계화한다.
- [ ] **Step 5:** TokenSource가 결과 보장이 아니라 가능성 출처임을 카드 문구에 명시한다.

### Task 2: 검증과 병합

**Files:**
- Verify: branch diff
- Verify: Project Core Documentation CI

**Interfaces:**
- Consumes: Task 1 Artifact
- Produces: 정본 보존과 문서 계약 통과 증거

- [ ] **Step 1:** 변경 파일이 계획과 Artifact에 한정되는지 확인한다.
- [ ] **Step 2:** Validate Project Core Documentation 성공을 확인한다.
- [ ] **Step 3:** 미해결 리뷰 스레드가 없는지 확인한다.
- [ ] **Step 4:** 검증된 HEAD를 squash merge한다.
