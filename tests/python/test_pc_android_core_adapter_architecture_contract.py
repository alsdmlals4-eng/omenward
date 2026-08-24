from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
DECISION_ID = "OMW-DEC-20260806-PC-ANDROID-CORE-ADAPTER-ARCHITECTURE-V1"
AUTHORITY = ROOT / "docs/design/APPROVED_PC_ANDROID_CORE_ADAPTER_ARCHITECTURE_2026-08-06.md"
REVIEW = ROOT / "docs/reviews/ADVERSARIAL_PC_ANDROID_CORE_ADAPTER_ARCHITECTURE_REVIEW_2026-08-06.md"
SPEC = ROOT / "docs/superpowers/specs/2026-08-06-pc-android-core-adapter-architecture-design.md"
PLAN = ROOT / "docs/superpowers/plans/2026-08-06-pc-android-core-adapter-architecture.md"
PLATFORM_AUTHORITY = ROOT / "docs/APPROVED_PC_ANDROID_PLATFORM_RELEASE_AUTHORITY_2026-08-05.md"
AGENTS = ROOT / "AGENTS.md"
STATUS = ROOT / "docs/CURRENT_IMPLEMENTATION_STATUS.md"


def read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


class PcAndroidCoreAdapterArchitectureContractTests(unittest.TestCase):
    def test_authority_files_exist(self) -> None:
        for path in (AUTHORITY, REVIEW, SPEC, PLAN):
            self.assertTrue(path.is_file(), f"missing authority file: {path.relative_to(ROOT)}")

    def test_decision_is_design_authority_not_implementation_claim(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            DECISION_ID,
            "ARCHITECTURE_STATUS = APPROVED_DESIGN_NOT_IMPLEMENTED",
            "PRODUCT_CODE_AUTHORITY = NONE",
            "RUNTIME_VALIDATION = NOT_RUN",
            "COMMON_PLATFORM_GATE = NOT_RUN",
            "PC_RELEASE_GATE = NOT_RUN",
            "MOBILE_RELEASE_GATE = NOT_RUN",
        ):
            self.assertIn(marker, text)

    def test_current_repository_baseline_is_recorded_without_false_export_claims(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            "CURRENT_ENGINE = GODOT_4_7",
            "CURRENT_MAIN_SCENE = res://scenes/main/main.tscn",
            "CURRENT_RENDERER = GL_COMPATIBILITY",
            "CURRENT_EXPORT_PRESETS = ABSENT",
            "CURRENT_PLATFORM_ADAPTER_ROOT = ABSENT",
            "CURRENT_SAVE_ADAPTER = ABSENT",
            "CURRENT_LIFECYCLE_ADAPTER = ABSENT",
            "CURRENT_STORE_ADAPTER = ABSENT",
        ):
            self.assertIn(marker, text)

    def test_common_core_has_strict_platform_neutral_boundary(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            "COMMON_CORE_BOUNDARY = PLATFORM_NEUTRAL_DOMAIN_AND_SIMULATION",
            "COMMON_CORE_GODOT_NODE_DEPENDENCY = FORBIDDEN",
            "COMMON_CORE_SCENE_TREE_LOOKUP = FORBIDDEN",
            "COMMON_CORE_DIRECT_INPUT_API = FORBIDDEN",
            "COMMON_CORE_DIRECT_DISPLAY_API = FORBIDDEN",
            "COMMON_CORE_DIRECT_FILE_API = FORBIDDEN",
            "COMMON_CORE_DIRECT_STORE_SDK = FORBIDDEN",
            "COMMAND_EVENT_BOUNDARY = REQUIRED",
        ):
            self.assertIn(marker, text)

    def test_required_adapter_interfaces_are_explicit(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            "INPUT_ADAPTER_INTERFACE = REQUIRED",
            "DISPLAY_ADAPTER_INTERFACE = REQUIRED",
            "SAVE_ADAPTER_INTERFACE = REQUIRED",
            "LIFECYCLE_ADAPTER_INTERFACE = REQUIRED",
            "PERFORMANCE_ADAPTER_INTERFACE = REQUIRED",
            "STORE_ADAPTER_INTERFACE = REQUIRED",
            "PLATFORM_CAPABILITIES_INTERFACE = REQUIRED",
        ):
            self.assertIn(marker, text)

    def test_pc_and_android_responsibilities_are_independent(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            "PC_INPUT = KEYBOARD_MOUSE_GAMEPAD",
            "PC_DISPLAY = WINDOW_FULLSCREEN_RESOLUTION",
            "PC_STORE_PRIMARY = STEAM",
            "STOVE = SEPARATE_SECONDARY_STORE_ADAPTER",
            "ANDROID_INPUT = TOUCH_BACK_GESTURE_VIRTUAL_KEYBOARD",
            "ANDROID_DISPLAY = SAFE_AREA_ASPECT_DENSITY",
            "ANDROID_LIFECYCLE = PAUSE_BACKGROUND_RESUME",
            "ANDROID_STORE_PRIMARY = GOOGLE_PLAY",
            "GATE_TRANSFER_POLICY = PASS_DOES_NOT_TRANSFER",
        ):
            self.assertIn(marker, text)

    def test_save_contract_uses_one_schema_and_platform_storage_adapters(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            "SAVE_SCHEMA = SHARED_VERSIONED_CANONICAL_SCHEMA",
            "SAVE_MIGRATION = FORWARD_MIGRATION_WITH_ROLLBACK_GUARD",
            "SAVE_WRITE = ATOMIC_TEMP_VALIDATE_REPLACE",
            "SAVE_STORAGE_PATH = ADAPTER_OWNED",
            "ANDROID_BACKGROUND_SAVE = REQUIRED",
            "CLOUD_SAVE = OPTIONAL_SEPARATE_CAPABILITY",
        ):
            self.assertIn(marker, text)

    def test_ui_policy_avoids_duplicate_platform_gameplay_trees(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            "GAMEPLAY_VIEW_MODEL = SHARED",
            "PLATFORM_UI_POLICY = SHARED_SEMANTIC_TREE_WITH_RESPONSIVE_VARIANTS",
            "DUPLICATE_PC_ANDROID_GAMEPLAY_SCENE_TREES = FORBIDDEN",
            "TOUCH_AS_MOUSE_ONLY = FORBIDDEN",
            "MINIMUM_TOUCH_TARGET_POLICY = REQUIRED_BEFORE_MOBILE_GATE",
        ):
            self.assertIn(marker, text)

    def test_adversarial_review_blocks_known_failure_modes(self) -> None:
        text = read(REVIEW)
        for marker in (
            "OMW-AUD-PLAT-001",
            "PLATFORM_API_LEAK_INTO_CORE",
            "SCENE_TREE_COUPLED_SESSION",
            "TOUCH_AS_MOUSE_FALSE_PARITY",
            "SAVE_SCHEMA_FORK",
            "ANDROID_LIFECYCLE_DATA_LOSS",
            "STORE_SDK_DOMAIN_OWNERSHIP",
            "DUPLICATED_UI_DRIFT",
            "EXPORT_PRESET_EQUALS_PLATFORM_READY_FALLACY",
        ):
            self.assertIn(marker, text)

    def test_existing_platform_authority_routes_to_architecture_decision(self) -> None:
        text = read(PLATFORM_AUTHORITY)
        for marker in (
            DECISION_ID,
            "APPROVED_PC_ANDROID_CORE_ADAPTER_ARCHITECTURE_2026-08-06.md",
            "ARCHITECTURE_STATUS = APPROVED_DESIGN_NOT_IMPLEMENTED",
        ):
            self.assertIn(marker, text)

    def test_central_operational_docs_preserve_current_platform_boundary(self) -> None:
        agents = read(AGENTS)
        for marker in (
            "docs/APPROVED_PC_ANDROID_PLATFORM_RELEASE_AUTHORITY_2026-08-05.md",
            "PC / Steam = COMMITTED_PRIMARY",
            "Android / Google Play = COMMITTED_RELEASE_TARGET_DEFERRED_RELEASE_NEAR",
        ):
            self.assertIn(marker, agents, "AGENTS.md")
        for live_gate in (
            "COMMON_PLATFORM_GATE = NOT_RUN",
            "PC_RELEASE_GATE = NOT_RUN",
            "MOBILE_RELEASE_GATE = NOT_RUN",
        ):
            self.assertNotIn(live_gate, agents, "AGENTS.md must stay a thin durable adapter")

        status = read(STATUS)
        for marker in (
            "PC / Steam = PRIMARY_PLANNING_AND_VALIDATION_TARGET",
            "Android / Google Play = COMMITTED_RELEASE_TARGET_EXECUTION_DEFERRED_RELEASE_NEAR",
            "SHARED_SAVE_SCHEMA = NOT_STARTED",
            "EXPORT_PRESETS = ABSENT",
            "RELEASE_READINESS = NOT_PROVEN",
        ):
            self.assertIn(marker, status, "docs/CURRENT_IMPLEMENTATION_STATUS.md")
        self.assertNotIn(DECISION_ID, agents)
        self.assertNotIn(DECISION_ID, status)


if __name__ == "__main__":
    unittest.main()
