from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

c2_path = ROOT / "tools/validate_c2_battle_objective.py"
c2 = c2_path.read_text(encoding="utf-8")
c2_marker = "    required_doc_states = {"
if "V2_CURRENT_CANON_COMPATIBILITY_C2" not in c2:
    c2_block = '''    # V2_CURRENT_CANON_COMPATIBILITY_C2
    gdd_body = (root / "docs/OMENWARD_GAME_DESIGN.md").read_text(encoding="utf-8")
    version_match = re.search(r"문서 버전:\\s*\\*\\*v(\\d+)\\.(\\d+)", gdd_body)
    current_v2 = version_match is not None and tuple(map(int, version_match.groups())) >= (0, 26)
    if current_v2:
        current_requirements = {
            "README.md": ("V2_SPEC_APPROVED", "LEGACY_C1_C2_C3_PROVEN", "HUMAN_QA_NOT_RUN"),
            "docs/CURRENT_IMPLEMENTATION_STATUS.md": (
                "LEGACY_C2_BATTLE_OBJECTIVE_REMOTE_PROVEN",
                "VERTICAL_SLICE_IMPLEMENTATION_NOT_STARTED",
                "HUMAN_QA_NOT_RUN",
            ),
            "docs/OMENWARD_GAME_DESIGN.md": (
                "문서 버전: **v0.26",
                "LATEST_USER_DESIGN_INTEGRATED",
                "PRODUCT_CODE_NOT_AUTHORIZED",
            ),
            "docs/OMENWARD_ROADMAP.md": (
                "기존 기술 기준선·C1·C2·C3 자동 증거 확보",
                "제품 구현: `NOT_STARTED`",
            ),
        }
        for relative, phrases in current_requirements.items():
            body = (root / relative).read_text(encoding="utf-8")
            for phrase in phrases:
                if phrase not in body:
                    errors.append(f"{relative} missing current V2 C2 boundary: {phrase}")
        audit = (root / "docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md").read_text(encoding="utf-8")
        for evidence in ("C2_BATTLE_OBJECTIVE_REMOTE_PROVEN", C2_AUDIT_HEAD, C2_AUDIT_RUN, "`Validate Core Contracts`"):
            if evidence not in audit:
                errors.append(f"C2 audit missing final proof: {evidence}")
        return errors

'''
    c2 = c2.replace(c2_marker, c2_block + c2_marker)
    c2_path.write_text(c2, encoding="utf-8")

c3_path = ROOT / "tools/validate_c3_core_ux.py"
c3 = c3_path.read_text(encoding="utf-8")
c3_marker = "    canonical_requirements = {"
if "V2_CURRENT_CANON_COMPATIBILITY_C3" not in c3:
    c3_block = '''    # V2_CURRENT_CANON_COMPATIBILITY_C3
    gdd_body = canonical["docs/OMENWARD_GAME_DESIGN.md"]
    version_match = re.search(r"문서 버전:\\s*\\*\\*v(\\d+)\\.(\\d+)", gdd_body)
    current_v2 = version_match is not None and tuple(map(int, version_match.groups())) >= (0, 26)
    if current_v2:
        current_requirements = {
            "README.md": ("V2_SPEC_APPROVED", "LEGACY_C1_C2_C3_PROVEN", "HUMAN_QA_NOT_RUN"),
            "docs/CURRENT_IMPLEMENTATION_STATUS.md": (
                "LEGACY_C3_AUTOMATED_CONTRACTS_PROVEN",
                "VERTICAL_SLICE_IMPLEMENTATION_NOT_STARTED",
                "HUMAN_QA_NOT_RUN",
            ),
            "docs/OMENWARD_GAME_DESIGN.md": (
                "문서 버전: **v0.26",
                "LATEST_USER_DESIGN_INTEGRATED",
                "PRODUCT_CODE_NOT_AUTHORIZED",
            ),
            "docs/OMENWARD_ROADMAP.md": (
                "기존 기술 기준선·C1·C2·C3 자동 증거 확보",
                "제품 구현: `NOT_STARTED`",
            ),
            "docs/C3_CORE_UX_AUDIT_2026-07-23.md": (
                "C3_AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING",
                PROOF_HEAD,
                PROOF_RUN,
            ),
        }
        for relative, terms in current_requirements.items():
            body = canonical[relative]
            require_terms(errors, body, terms, relative)
            validate_links(errors, root, relative, body)
        return errors

'''
    c3 = c3.replace(c3_marker, c3_block + c3_marker)
    c3_path.write_text(c3, encoding="utf-8")

status_path = ROOT / "docs/CURRENT_IMPLEMENTATION_STATUS.md"
status = status_path.read_text(encoding="utf-8")
if "C2 최종 검증 run: `29938742864`" not in status:
    status = status.rstrip() + '''

## Legacy C2 원격 검증 증거

- `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`
- C2 최종 검증 run: `29938742864`
- 이 증거는 legacy C2 전투 목적 루프의 원격 검증이며 V2 전장 구현 완료를 뜻하지 않는다.
'''
    status_path.write_text(status, encoding="utf-8")
