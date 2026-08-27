# OMENWARD Battlefield Backdrop V1

```yaml
asset_id: OMW-IMG-20260828-BATTLEFIELD-BACKDROP-V1
status: LEGACY_RUNTIME_ASSET__CURRENT_BUILD_CONSUMER_ACTIVE
created_at: 2026-08-28
decision: OMW-VISUAL-20260828-BATTLEFIELD-MAP-ROULETTE-PICKER-01__PARTIALLY_SUPERSEDED
local_path: assets/art/battlefield/ward_veil_three_lane_backdrop_v1.png
dimensions: 1672x941
sha256: DB80778C1EA0A7905EA938B902F94C06DC472EB00740C93E07A38CE6E4C86525
format: PNG_RGBA_OPAQUE
consumer: scenes/battle/battlefield.tscn::Backdrop
notion_record: 02_Visual_Bible__2026-08-28_runtime_backdrop_section__SERVER_READBACK_PASS
notion_attachment: file-upload://3c91b237-eb1c-810b-9b15-00b2440ee848
runtime_readability: PARTIAL_TECHNICAL_HERA_CAPTURE__HUMAN_NOT_RUN
runtime_evidence: HERA_960x540_PREPARE_AND_STOPPED_3X3_CAPTURED
human_evidence: NOT_RUN
```

## Current boundary

`OMW-VISUAL-20260828-STORYBOOK-SD-THREE-FRONT-STRATEGIC-MAP-01`이 주 전장 표현을 세 전선 동시 전략 지도 UI로 변경했다. 이 파일은 현 빌드의 실제 consumer를 설명하는 **legacy runtime asset record**다. 삭제·교체·새 방향의 runtime PASS를 의미하지 않는다.

## Intent

본진 전체가 아닌 **본진 앞 넓은 전장**을 보여준다. 상·중·하 세 전선마다 아군 전진기지와 중앙 접전지가 보이며, 숲·하천·교량을 따라 주 전선과 구별되는 우회 경로를 둔다. 실제 전투 병력과 전선 상태는 runtime `BattlefieldView`가 소유한다.

## Generation brief

- Original storybook watercolor SD tactical fantasy illustration; supplied references were used only for broad composition and artistic tone.
- Navy/ivory/gold Ward defenders vs. restrained purple Veil pressure.
- No copied character, title, UI, logo, label, grid, border, or gameplay state encoding.
- Three large horizontal routes, three friendly forward bases, three central clash groups, two visibly distinct bypass routes, and terrain readable behind translucent front-state UI.

## Provenance and storage

- Local canonical runtime input: `assets/art/battlefield/ward_veil_three_lane_backdrop_v1.png`.
- Notion human-facing record: `02 · 비주얼 바이블` — “2026-08-28 · Runtime Battlefield Backdrop” section, including a Notion-owned inline PNG attachment and this asset ID/hash. Destination readback: `PASS`.
- Generation runtime: OpenAI image generation, 2026-08-28. The asset has no third-party source image or copied protected expression.

## Evidence boundary

- `HERA_TECHNICAL_SMOKE = PASS`: PREPARE and STOPPED 3×3 visual captures at 960×540, zero runtime diagnostics errors/warnings.
- `HUMAN_PLAYER_EXPERIENCE = NOT_RUN`: this technical capture does not establish player readability, balance, or final visual approval beyond the user-authorized image-production policy.
