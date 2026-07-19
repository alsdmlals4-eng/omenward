# GitHub Issue Markdown Mirror

`docs/issues/0001.md` 형식의 파일은 GitHub Issue의 제목, 본문, 상태, 라벨, 담당자와 갱신 시각을 저장소에 추적하는 읽기 가능한 미러다.

- 모든 열린·닫힌 Issue를 포함한다.
- 댓글과 첨부는 GitHub에만 남기며 이 디렉터리에 복제하지 않는다.
- 승인 기획의 책임 원본은 계속 `docs/design/`, Goal, Work Order다. Issue 미러가 이 문서를 대체하지 않는다.
- GitHub에서 변경된 Issue는 자동화가 동기화 PR로 제안한다. `main`에 직접 반영하지 않는다.
- 이 디렉터리의 Markdown이 `main`에 병합되면 동일 Issue의 제목·본문·상태를 GitHub에 반영한다.
- 마지막 동기화 이후 로컬 Markdown과 GitHub 본문이 모두 달라지면 자동 갱신을 중단하고 사람이 책임 원본을 기준으로 해결한다.

표준 로컬 클론에서는 `tools/sync_repo.ps1`을 실행해 GitHub `main`의 Issue 미러와 프로젝트 파일을 fast-forward 방식으로 갱신한다.
