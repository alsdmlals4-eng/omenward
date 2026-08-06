# [제안] OMENWARD GUT 9.7.1 Vendor Manifest Reconciliation

```yaml
decision_id: OMW-DEC-20260806-TOOLS-GUT-9-7-1-VENDOR-MANIFEST-RECONCILIATION-V1
status: VENDOR_DELTA_CLASSIFIED / ACTIVATION_BLOCKED
counter: NON_COUNTER
base_main: 7588317f294d602cfad5f7f15bfebcf849b8a77b
```

## 결론

Upstream GUT 9.7.1 `addons/gut`와 OMENWARD vendor tree의 경로 집합은 동일하며, blob 차이는 18개다.

- GDScript·CLI·UID sidecar·`plugin.cfg`·라이선스·이미지 및 원본 폰트 blob: 동일
- `.tscn`·`.tres` 17개: upstream보다 각각 13바이트 작음
- 샘플 직접 비교: `load_steps=N` 헤더 제거
- 17개 전체 내용 비교: 아직 미완료이므로 `HEADER_LOAD_STEPS_NORMALIZATION_CANDIDATE`
- `source_code_pro.fnt`: 크기는 같지만 blob이 달라 `UNCLASSIFIED_BINARY_DELTA`

```text
VENDOR_PATH_SET = MATCH
CHANGED_PATHS = 18
CODE_OR_PLUGIN_DELTA = 0
ACTIVATION = BLOCKED
```

## 권위 경계

이 PR은 vendor 파일을 수정하지 않는다. 실제 clean import나 resource 재저장은 HiGodot 저작 권위에서만 수행한다. GUT은 검사·실행·보고 권위이며 vendor 또는 제품 파일을 임의로 수정하지 않는다.

## 다음 Gate

1. 17개 텍스트 파일 전체 내용 diff.
2. `source_code_pro.fnt` binary decode와 origin 확인.
3. exact Godot 4.7 clean import.
4. GUT CLI canary 및 JUnit 생성.
5. 기존 프로젝트 regression.

모든 항목 전까지 GUT 활성화·Ready 전환·병합을 금지한다.
