from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
DECISION_ID = "OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1"
SPEC = ROOT / "docs/superpowers/specs/2026-08-05-stage-end-merchant-design.md"
AMENDMENT = ROOT / "docs/superpowers/specs/2026-08-05-stage-end-merchant-design-amendment.md"
PLAN = ROOT / "docs/superpowers/plans/2026-08-05-stage-end-merchant.md"
CANON = ROOT / "docs/design/APPROVED_OMENWARD_STAGE_END_MERCHANT_2026-08-05.md"
REVIEW = ROOT / "docs/reviews/ADVERSARIAL_STAGE_END_MERCHANT_ECONOMY_AND_INVENTORY_REVIEW_2026-08-05.md"
LIFECYCLE = ROOT / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md"

CENTRAL_FILES = (
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "docs/PROJECT_CORE.md",
    ROOT / "docs/ACTIVE_CONTEXT.md",
    ROOT / "docs/DOCUMENTATION_MAP.md",
    ROOT / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
    ROOT / "docs/OMENWARD_GDD_CURRENT_CANON.md",
    ROOT / "docs/DECISIONS_PENDING.md",
    ROOT / "docs/OMENWARD_ROADMAP.md",
    ROOT / "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    ROOT / "docs/HANDOFF_CONTEXT.md",
    ROOT / "docs/PROJECT_CANON_DECISION_LEDGER.md",
    ROOT / "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md",
)


def read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


class StageEndMerchantCanonTests(unittest.TestCase):
    def test_authority_files_exist(self) -> None:
        for path in (SPEC, AMENDMENT, PLAN, CANON, REVIEW):
            self.assertTrue(path.is_file(), f"missing authority file: {path.relative_to(ROOT)}")

    def test_visit_window_and_final_stage_exception_are_explicit(self) -> None:
        text = read(CANON)
        for marker in (
            DECISION_ID,
            "MERCHANT_VISIT_STAGES = 1_TO_19",
            "STAGE_20_MERCHANT = FORBIDDEN",
            "STAGE_20_NEXT = MAPRUN_FINAL_SETTLEMENT",
            "ALWAYS_AVAILABLE_HUD_SHOP = FORBIDDEN",
            "COMBAT_REENTRY = FORBIDDEN",
        ):
            self.assertIn(marker, text)

    def test_inventory_has_four_finite_role_slots(self) -> None:
        text = read(CANON)
        for marker in (
            "TOTAL_MERCHANT_SLOTS = 4",
            "SLOT_A = ROULETTE_CONTROL",
            "SLOT_B = RECOVERY_SERVICE",
            "SLOT_C = DEVELOPMENT_SERVICE",
            "SLOT_D = VARIABLE_OPPORTUNITY",
            "VISIT_STOCK = FINITE",
            "INFINITE_PURCHASE = FORBIDDEN",
            "INFINITE_REROLL = FORBIDDEN",
        ):
            self.assertIn(marker, text)

    def test_roulette_control_slot_never_dies_at_ticket_cap(self) -> None:
        text = read(CANON)
        self.assertIn("STORED_MOVE_TICKETS < 3", text)
        self.assertIn("STORED_MOVE_TICKETS = 3", text)
        self.assertIn("NEXT_SPIN_ONE_TIME_GOLD_DISCOUNT", text)
        self.assertIn("DISCOUNT_STACKING = FORBIDDEN", text)
        self.assertIn("UNUSED_DISCOUNT_EXPIRES_AT_NEXT_STAGE_START", text)

    def test_merchant_supplements_but_does_not_bypass_core_systems(self) -> None:
        text = read(CANON)
        for marker in (
            "DIRECT_UNIT_SALE = FORBIDDEN",
            "DIRECT_T3_SALE = FORBIDDEN",
            "DIRECT_TACTICAL_UNLOCK = FORBIDDEN",
            "DIRECT_MANA_SALE = FORBIDDEN",
            "BUILDING_BRANCH_RESELECT = FORBIDDEN",
            "STAGE_INFORMATION_SALE = FORBIDDEN",
            "PURCHASE_CURRENCY = GOLD_ONLY",
        ):
            self.assertIn(marker, text)

    def test_gold_opportunity_cost_and_numeric_gate_are_preserved(self) -> None:
        text = read(CANON)
        for marker in (
            "건설",
            "업그레이드",
            "수리",
            "룰렛 회전",
            "전술 연구",
            "상인 구매",
            "EXACT_PRICES = PENDING_SIMULATION",
            "EXACT_STOCK_COUNTS = PENDING_SIMULATION",
            "EXACT_APPEARANCE_RATES = PENDING_SIMULATION",
        ):
            self.assertIn(marker, text)

    def test_central_authority_routes_decision_six_of_ten(self) -> None:
        for path in CENTRAL_FILES:
            text = read(path)
            self.assertIn(DECISION_ID, text, str(path.relative_to(ROOT)))
            self.assertIn("6_OF_10", text, str(path.relative_to(ROOT)))

    def test_lifecycle_blocks_legacy_shop_authority(self) -> None:
        text = read(LIFECYCLE)
        for marker in (
            "LEGACY_ALWAYS_AVAILABLE_SHOP",
            "LEGACY_INFINITE_MERCHANT_STOCK",
            "LEGACY_DIRECT_CORE_REWARD_SALES",
            "IMPLEMENTATION_INPUT_FORBIDDEN",
            DECISION_ID,
        ):
            self.assertIn(marker, text)

    def test_adversarial_review_closes_known_risks_without_authorizing_product(self) -> None:
        text = read(REVIEW)
        for marker in (
            "OMW-AUD-468",
            "OMW-AUD-491",
            "MERCHANT_MANDATORY_PURCHASE_LOOP",
            "TREASURY_BUYOUT_SNOWBALL",
            "DEAD_GUARANTEED_SLOT",
            "DIRECT_UNLOCK_BYPASS",
            "DUPLICATE_PURCHASE_TRANSACTION",
            "STAGE_20_MERCHANT_REGRESSION",
            "PRODUCT_CODE = UNCHANGED",
            "EXACT_NUMERICS = PENDING_SIMULATION",
        ):
            self.assertIn(marker, text)

    def test_product_boundaries_remain_closed(self) -> None:
        text = read(CANON)
        for marker in (
            "PRODUCT_CODE = UNCHANGED",
            "DATA_MIGRATION = NOT_AUTHORIZED",
            "EXACT_NUMERICS = PENDING_SIMULATION",
            "SIMULATION = NOT_RUN",
            "RUNTIME = NOT_RUN",
            "HUMAN_QA = NOT_RUN",
        ):
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
