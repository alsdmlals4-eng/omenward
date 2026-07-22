from __future__ import annotations

import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def write(relative: str, text: str) -> None:
    (ROOT / relative).write_text(text, encoding="utf-8", newline="\n")


def replace_once(relative: str, old: str, new: str) -> None:
    text = read(relative)
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{relative}: expected one match, found {count}: {old[:100]!r}")
    write(relative, text.replace(old, new, 1))


def replace_regex(relative: str, pattern: str, replacement: str) -> None:
    text = read(relative)
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"{relative}: expected one regex match, found {count}: {pattern!r}")
    write(relative, updated)


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


replace_once("docs/PROJECT_CORE.md", "- 상태: `EXISTING_CORE_IDENTIFIED`", "- 상태: `CORE_CONFIRMED`")
replace_once("docs/PROJECT_CORE.md", "- 잠금 상태: `CORE_LOCK_PENDING_USER_CONFIRMATION`", "- 잠금 상태: `CORE_LOCKED`")
replace_once(
    "docs/PROJECT_CORE.md",
    "`CORE_LOCK_PENDING_USER_CONFIRMATION`은 코어를 새로 발명했다는 뜻이 아니다. 기존 코어를 식별해 기록했으며, 문구를 변경 불가 상태로 잠그는 행위만 사용자의 명시적 확인을 기다린다는 뜻이다.",
    "사용자는 2026-07-22 대화에서 `코어확정`을 명시했다. 따라서 정체성 한 문장, 세 가지 플레이어 책임, 프로젝트 코어 분류, 불변 조건과 제거·대체 스트레스 테스트를 `CORE_CONFIRMED`·`CORE_LOCKED`로 확정한다.",
)
replace_once(
    "docs/PROJECT_CORE.md",
    "- `CORE_CONFIRMED`와 `CORE_LOCKED` 전환은 사용자의 명시적 확인 뒤 별도 기록한다.\n- 잠금 전에도 현재 작업의 우선순위와 수직 슬라이스 검증 기준은 이 문서를 따른다.",
    "- `CORE_CONFIRMED`·`CORE_LOCKED`는 2026-07-22 사용자의 `코어확정` 지시로 적용됐다.\n- 잠금된 코어의 변경은 사용자 명시적 승인, 제거 테스트, 대안과 영향 범위 기록을 모두 요구한다.\n- 후속 구현은 이 문서의 우선순위와 C1~C5 검증 게이트를 따른다.",
)

replace_regex(
    "docs/DECISIONS_PENDING.md",
    r"### A\. 프로젝트 코어 문구 잠금\n.*?(?=### B\.)",
    """### A. 프로젝트 코어 확정·잠금 — 완료

- [x] 정체성 한 문장과 `예측 → 확률 설계 → 전선 커밋` 세 기둥을 `CORE_CONFIRMED`로 확정.
- [x] 제거 테스트와 불변 조건을 `CORE_LOCKED`로 확정.
- 확인 근거: 2026-07-22 사용자의 `코어확정` 지시.
- 후속 변경은 사용자 명시적 승인, 제거 테스트, 대안과 영향 범위 기록을 요구한다.

""",
)
replace_once(
    "docs/DECISIONS_PENDING.md",
    "1. 정본·프로젝트 코어 복구 PR 검토\n2. 프로젝트 코어 문구 잠금 여부 사용자 확인\n3. 승인 룰렛 계약 복구 Plan\n4. 룰렛 계약 구현·자동 검증\n5. 전투 목적 루프 연결\n6. 승인 코어 UX 6종\n7. 10~15분 사람 플레이와 1080p·720p QA\n8. 밸런스 안정화\n9. 콘텐츠·아트 확장",
    "1. 프로젝트 코어 확정·잠금과 정본 복구 PR 병합\n2. 승인 룰렛 계약 복구 Plan\n3. 룰렛 계약 구현·자동 검증\n4. 전투 목적 루프 연결\n5. 승인 코어 UX 6종\n6. 10~15분 사람 플레이와 1080p·720p QA\n7. 밸런스 안정화\n8. 콘텐츠·아트 확장",
)

replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "- 현재 상태: **기술 기준선 구현 / 핵심 수직 슬라이스 부분 구현 / C0 정본·프로젝트 코어 복구 진행**",
    "- 현재 상태: **C0 정본·프로젝트 코어 확정·잠금 완료 / C1 승인 룰렛 계약 복구 착수**",
)
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "→ [현재] 정본·프로젝트 코어 복구\n→ 승인 룰렛 계약 복구",
    "→ 정본·프로젝트 코어 확정·잠금 완료\n→ [현재] 승인 룰렛 계약 복구",
)
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "| C0 정본·코어 복구 | 프로젝트 코어·상태·로드맵 일치 | **진행 중** | 사용자 코어 문구 확인·문서 PR |\n| C1 룰렛 계약 복구 | 중앙 판정 줄·완성선·등급·단일 보상 | 미시작 | 승인 계약 테스트 PASS |",
    "| C0 정본·코어 복구 | 프로젝트 코어·상태·로드맵 일치 | **완료 / CORE_LOCKED** | 정본 PR 병합 |\n| C1 룰렛 계약 복구 | 중앙 판정 줄·완성선·등급·단일 보상 | **현재** | 승인 계약 테스트 PASS |",
)
replace_regex(
    "docs/OMENWARD_ROADMAP.md",
    r"## 15\. 지금 실행할 단 하나의 작업\n.*\Z",
    """## 15. 지금 실행할 단 하나의 작업

```text
프로젝트 코어 확정·잠금 반영과 정본 PR 병합
→ 최신 main에서 승인 룰렛 책임 원본·구현·테스트 전수 감사
→ 룰렛 계약 복구 Plan
→ Build
→ Adversarial Review·Validation Review·Integration Review
```

다음 기능 변경은 승인 룰렛 계약 복구로 제한한다. 전투 목적 루프·코어 UX·신규 콘텐츠는 같은 PR에 섞지 않는다.
""",
)

replace_once("docs/ACTIVE_CONTEXT.md", "- 프로젝트 코어: `docs/PROJECT_CORE.md`", "- 프로젝트 코어: `docs/PROJECT_CORE.md` (`CORE_CONFIRMED` / `CORE_LOCKED`)")
replace_once("docs/HANDOFF_CONTEXT.md", "- 프로젝트 코어: `docs/PROJECT_CORE.md`", "- 프로젝트 코어: `docs/PROJECT_CORE.md` (`CORE_CONFIRMED` / `CORE_LOCKED`)")
replace_once("docs/OMENWARD_GAME_DESIGN.md", "- 엔진: Godot + GDScript", "- 엔진: Godot + GDScript\n- 프로젝트 코어: **CORE_CONFIRMED / CORE_LOCKED** (2026-07-22 사용자 확인)")
replace_once("README.md", "> 현재 상태: **기술·데이터 그레이박스 수직 슬라이스 존재 / 코어 루프 미완결 / 사람 플레이 검증 대기**", "> 현재 상태: **기술·데이터 그레이박스 수직 슬라이스 존재 / 코어 루프 미완결 / 사람 플레이 검증 대기**\n> 프로젝트 코어: **CORE_CONFIRMED / CORE_LOCKED**")

replace_once("docs/CURRENT_IMPLEMENTATION_STATUS.md", "- 판정:\n  - `TECHNICAL_BASELINE_IMPLEMENTED`", "- 프로젝트 코어: `CORE_CONFIRMED` / `CORE_LOCKED`\n- 판정:\n  - `TECHNICAL_BASELINE_IMPLEMENTED`")
replace_once(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "1. 정본·프로젝트 코어 복구\n2. 승인 룰렛 계약 복구\n3. 전투 → 거점·성문·승패 목적 루프 연결\n4. 승인 코어 UX 6종 최소 구현\n5. 10~15분 코어 플레이테스트\n6. 밸런스 안정화와 콘텐츠·아트 확장",
    "1. 승인 룰렛 계약 복구\n2. 전투 → 거점·성문·승패 목적 루프 연결\n3. 승인 코어 UX 6종 최소 구현\n4. 10~15분 코어 플레이테스트\n5. 밸런스 안정화와 콘텐츠·아트 확장",
)
replace_once("docs/CURRENT_IMPLEMENTATION_STATUS.md", "정본 복구 완료 조건:", "C0 정본·프로젝트 코어 복구 완료 판정:")
replace_once("docs/CURRENT_IMPLEMENTATION_STATUS.md", "- 다음 변경은 게임 코드 전체가 아니라 승인 룰렛 계약 복구로 한정한다.", "- 프로젝트 코어는 2026-07-22 사용자 확인으로 `CORE_CONFIRMED`·`CORE_LOCKED`다.\n- 다음 변경은 게임 코드 전체가 아니라 승인 룰렛 계약 복구로 한정한다.")

replace_once(
    "docs/CORE_RECOVERY_AUDIT_2026-07-22.md",
    "- 코어 상태는 `EXISTING_CORE_IDENTIFIED`로 기록하고 잠금은 사용자 확인을 기다린다.",
    "- 코어 상태는 최초 식별 상태로 기록했고, 2026-07-22 사용자의 `코어확정` 지시 뒤 `CORE_CONFIRMED`·`CORE_LOCKED`로 전환했다.",
)
replace_once(
    "docs/CORE_RECOVERY_AUDIT_2026-07-22.md",
    "1. 이 문서 전용 Draft PR 검토.\n2. 사용자가 프로젝트 코어 문구 잠금 여부를 확인.\n3. 승인 룰렛 계약 복구를 별도 Plan·Build·Review PR로 수행.\n4. 전투 목적 루프, 코어 UX, 사람 플레이 순으로 분리 진행.",
    "1. 사용자가 프로젝트 코어를 `코어확정`으로 확인.\n2. 정본 PR에서 `CORE_CONFIRMED`·`CORE_LOCKED` 전환과 검증.\n3. 승인 룰렛 계약 복구를 별도 Plan·Build·Review PR로 수행.\n4. 전투 목적 루프, 코어 UX, 사람 플레이 순으로 분리 진행.",
)
replace_once("docs/CORE_RECOVERY_AUDIT_2026-07-22.md", "- 코어 잠금: `PENDING_USER_CONFIRMATION`", "- 코어 잠금: `CORE_CONFIRMED_AND_LOCKED`")

replace_once("tools/validate_project_core_docs.py", '    "EXISTING_CORE_IDENTIFIED",\n    "CORE_LOCK_PENDING_USER_CONFIRMATION",', '    "CORE_CONFIRMED",\n    "CORE_LOCKED",')
replace_once(
    "tools/validate_project_core_docs.py",
    '    if re.search(r"(?m)^- (?:상태|잠금 상태): `(?:CORE_CONFIRMED|CORE_LOCKED)`$", core):\n        errors.append("project core may not claim confirmed/locked without explicit user approval")',
    '''    required_lock_lines = (\n        "- 상태: `CORE_CONFIRMED`",\n        "- 잠금 상태: `CORE_LOCKED`",\n        "2026-07-22 대화에서 `코어확정`",\n    )\n    for missing in _contains_all(core, required_lock_lines):\n        errors.append(f"PROJECT_CORE missing confirmed lock evidence: {missing}")\n\n    pending_core_terms = (\n        "EXISTING_CORE_IDENTIFIED",\n        "CORE_LOCK_PENDING_USER_CONFIRMATION",\n        "PENDING_USER_CONFIRMATION",\n    )\n    for relative in (\n        "docs/PROJECT_CORE.md",\n        "docs/CORE_RECOVERY_AUDIT_2026-07-22.md",\n        "docs/DECISIONS_PENDING.md",\n        "docs/OMENWARD_ROADMAP.md",\n    ):\n        text = _read(root, relative)\n        for term in pending_core_terms:\n            if term in text:\n                errors.append(f"{relative} retains stale project-core lock state: {term}")''',
)
replace_once("tools/validate_project_core_docs.py", '        "정본·프로젝트 코어 복구",', '        "정본·프로젝트 코어 확정·잠금 완료",')
replace_once(
    "tools/validate_project_core_docs.py",
    '    if "승인 룰렛 계약 복구" not in decisions:\n        errors.append("DECISIONS_PENDING does not point to the next decision gate")',
    '    if "승인 룰렛 계약 복구" not in decisions:\n        errors.append("DECISIONS_PENDING does not point to the next decision gate")\n    if "프로젝트 코어 확정·잠금 — 완료" not in decisions:\n        errors.append("DECISIONS_PENDING does not record the resolved project-core lock")',
)

replace_once(
    "tests/python/test_project_core_docs.py",
    "    def test_roadmap_phase_history_loss_is_rejected(self) -> None:",
    '''    def test_pending_core_lock_state_is_rejected(self) -> None:\n        with tempfile.TemporaryDirectory() as directory:\n            temp_root = pathlib.Path(directory)\n            self._copy_contract_files(temp_root)\n            core = temp_root / "docs" / "PROJECT_CORE.md"\n            core.write_text(\n                core.read_text(encoding="utf-8")\n                .replace("- 상태: `CORE_CONFIRMED`", "- 상태: `EXISTING_CORE_IDENTIFIED`")\n                .replace("- 잠금 상태: `CORE_LOCKED`", "- 잠금 상태: `CORE_LOCK_PENDING_USER_CONFIRMATION`"),\n                encoding="utf-8",\n            )\n            errors = validate(temp_root)\n            self.assertTrue(any("stale project-core lock state" in error for error in errors))\n\n    def test_roadmap_phase_history_loss_is_rejected(self) -> None:''',
)

for relative in (
    "tools/_confirm_project_core_once.py",
    ".github/workflows/confirm-project-core-once.yml",
    "docs/_CORE_CONFIRM_FAILURE.log",
):
    path = ROOT / relative
    if path.exists():
        path.unlink()

run("python", "-m", "py_compile", "tools/validate_project_core_docs.py", "tests/python/test_project_core_docs.py")
run("python", "tools/validate_project_core_docs.py")
run("python", "-m", "unittest", "discover", "-s", "tests/python", "-v")
run("python", "tools/validate_skill_system.py")
run("git", "diff", "--check")
run("git", "config", "user.name", "github-actions[bot]")
run("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
run("git", "add", "-A")
run("git", "commit", "-m", "confirm and lock Omenward project core")
run("git", "push", "origin", "HEAD:agent/project-core-canon-recovery")
