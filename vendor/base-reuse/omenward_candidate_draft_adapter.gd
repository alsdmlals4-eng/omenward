extends RefCounted

const CandidateDraftScript := preload("res://vendor/base-reuse/candidate_draft_weight_engine.gd")
const TOKEN_SOURCE_CANDIDATE_COUNT := 3


func generate_token_source_candidates(pool: Array, candidate_count: int, seed: int, state: Dictionary = {}) -> Dictionary:
	if candidate_count != TOKEN_SOURCE_CANDIDATE_COUNT:
		return {"ok": false, "reason": "OMENWARD_REQUIRES_THREE_TOKEN_SOURCE_CANDIDATES", "candidates": []}

	var seen_ids: Dictionary = {}
	for raw_candidate: Variant in pool:
		if not raw_candidate is Dictionary:
			return {"ok": false, "reason": "CANDIDATE_NOT_DICTIONARY", "candidates": []}
		var candidate: Dictionary = raw_candidate
		var candidate_id := str(candidate.get("id", ""))
		if candidate_id.is_empty():
			return {"ok": false, "reason": "MISSING_CANDIDATE_ID", "candidates": []}
		if seen_ids.has(candidate_id):
			return {"ok": false, "reason": "DUPLICATE_CANDIDATE_ID", "candidates": []}
		seen_ids[candidate_id] = true

		var raw_weight: Variant = candidate.get("weight", 1)
		if not raw_weight is int:
			return {"ok": false, "reason": "FRACTIONAL_WEIGHT_FORBIDDEN", "candidates": []}
		if int(raw_weight) <= 0:
			return {"ok": false, "reason": "NON_POSITIVE_WEIGHT", "candidates": []}

	if seen_ids.size() < TOKEN_SOURCE_CANDIDATE_COUNT:
		return {"ok": false, "reason": "INSUFFICIENT_UNIQUE_CANDIDATES", "candidates": []}

	var result: Dictionary = CandidateDraftScript.new().generate(
		pool,
		TOKEN_SOURCE_CANDIDATE_COUNT,
		seed,
		state,
		CandidateDraftScript.DUPLICATE_FORBID
	)
	if not bool(result.get("ok", false)):
		return result
	if result.get("candidates", []).size() != TOKEN_SOURCE_CANDIDATE_COUNT:
		return {"ok": false, "reason": "INSUFFICIENT_UNIQUE_CANDIDATES", "candidates": []}
	return result
