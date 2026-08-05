from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
PROFILE = ROOT / "docs" / "PLATFORM_RELEASE_AND_ASSET_RIGHTS_PROFILE.md"
PLATFORM_AUTHORITY = (
    ROOT
    / "docs"
    / "APPROVED_PC_ANDROID_PLATFORM_RELEASE_AUTHORITY_2026-08-05.md"
)
ASSET_RECORD = ROOT / "docs" / "ASSET_RIGHTS_AND_PROVENANCE_RECORD.md"
RELEASE_PACK = ROOT / "docs" / "GAME_RELEASE_COMPLIANCE_EVIDENCE_PACK.md"
AGENTS = ROOT / "AGENTS.md"

DECISION_ID = "OMW-DEC-20260805-PLATFORM-PC-ANDROID-V1"


class ContractTests(unittest.TestCase):
    def test_required_documents_exist(self):
        for path in (PROFILE, PLATFORM_AUTHORITY, ASSET_RECORD, RELEASE_PACK):
            self.assertTrue(path.is_file(), f"missing: {path}")

    def test_dual_platform_authority_is_explicit_and_staged(self):
        text = PROFILE.read_text(encoding="utf-8")
        for token in (
            DECISION_ID,
            "LOWEST_VIABLE_RATING",
            "AVOID_ADULTS_ONLY",
            "APPROVED_DUAL_PLATFORM",
            "STAGED_CROSS_PLATFORM",
            "SIMULTANEOUS_RELEASE_NOT_COMMITTED",
            "PC: COMMITTED",
            "Steam: COMMITTED_PRIMARY_STORE",
            "STOVE: SECONDARY_RELEASE_CANDIDATE",
            "Android: COMMITTED",
            "Google_Play: COMMITTED_PRIMARY_STORE",
            "iOS: NOT_CURRENT_SCOPE",
            "ALL_OR_12_CANDIDATE",
            "RELEASE_BLOCKED_UNVERIFIED",
            "PLATFORM_SUBMISSION_NOT_RUN",
            "LEGAL_REVIEW_NOT_PERFORMED",
        ):
            self.assertIn(token, text)

    def test_common_pc_and_mobile_gates_are_independent(self):
        text = PLATFORM_AUTHORITY.read_text(encoding="utf-8")
        for token in (
            DECISION_ID,
            "COMMON_PLATFORM_GATE",
            "PC_RELEASE_GATE",
            "MOBILE_RELEASE_GATE",
            "PASS_DOES_NOT_TRANSFER",
            "STOVE_SECONDARY_RELEASE_CANDIDATE",
            "NOT_CURRENT_SCOPE",
            "RELEASE_BLOCKED_UNVERIFIED",
        ):
            self.assertIn(token, text)

    def test_asset_record(self):
        text = ASSET_RECORD.read_text(encoding="utf-8")
        for token in (
            "commercial_use",
            "distribution_in_game_build",
            "raw_source_redistribution",
            "license_version_or_terms_date",
            "reference_brief",
            "forbidden_expression",
            "final_asset_record",
            "reference_similarity_status",
            "secure_original_location",
            "MUSIC_SFX",
            "FONT",
            "CHARACTER_ILLUSTRATION",
            "MODEL_3D_ANIMATION",
            "PLUGIN_ASSET",
            "OPEN_SOURCE_LIBRARY",
            "AI_OUTPUT_MODEL_TERMS",
            "OUTSOURCING_CONTRACT",
            "VOICE_COMPOSER_TRANSLATOR_CONTRACT",
        ):
            self.assertIn(token, text)

    def test_release_pack_and_agents_routing(self):
        release = RELEASE_PACK.read_text(encoding="utf-8")
        agents = AGENTS.read_text(encoding="utf-8")
        for token in (
            DECISION_ID,
            "build_store_questionnaire_consistency",
            "asset_rights_coverage",
            "APPROVED_DUAL_PLATFORM",
            "STAGED_CROSS_PLATFORM",
            "RELEASE_BLOCKED_UNVERIFIED",
        ):
            self.assertIn(token, release)
        for path in (
            "docs/APPROVED_PC_ANDROID_PLATFORM_RELEASE_AUTHORITY_2026-08-05.md",
            "docs/PLATFORM_RELEASE_AND_ASSET_RIGHTS_PROFILE.md",
            "docs/ASSET_RIGHTS_AND_PROVENANCE_RECORD.md",
            "docs/GAME_RELEASE_COMPLIANCE_EVIDENCE_PACK.md",
        ):
            self.assertIn(path, agents)


if __name__ == "__main__":
    unittest.main()
