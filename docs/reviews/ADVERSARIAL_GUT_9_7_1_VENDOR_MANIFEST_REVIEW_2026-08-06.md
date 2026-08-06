# [적대적 검토] GUT 9.7.1 Vendor Manifest

```yaml
decision_id: OMW-DEC-20260806-TOOLS-GUT-9-7-1-VENDOR-MANIFEST-RECONCILIATION-V1
status: REVIEWED_WITH_BLOCKERS
```

## Finding

1. Tree SHA 불일치는 코드 포크를 의미하지 않는다. 현재 GDScript·CLI·plugin·license blob은 동일하다.
2. 반대로 17개 파일이 모두 13바이트 작다는 사실만으로 내용 동일성을 확정할 수 없다. 샘플 외 전체 content diff가 필요하다.
3. `source_code_pro.fnt`는 같은 크기의 다른 binary blob이므로 가장 강한 활성화 blocker다.
4. 경로 집합이 같아도 runtime import·CLI·JUnit·regression 증거를 대체하지 않는다.
5. 이 manifest PR에서 vendor 파일을 함께 수정하면 관측과 교정이 섞이므로 금지한다.

## 판정

```text
PATH_SET_RECONCILIATION = PASS
CODE_PROVENANCE = PASS_BY_BLOB_SHA
TEXT_RESOURCE_CLASSIFICATION = CANDIDATE_ONLY
BINARY_RESOURCE_CLASSIFICATION = FAIL_UNCLASSIFIED
GUT_ACTIVATION = FAIL
MERGE_READY = FALSE
```
