class_name StageEconomy
extends RefCounted

const BASE_INCOME_AMOUNT := 5
const BASE_INCOME_INTERVAL_SECONDS := 20.0
const CONTROL_INCOME_AMOUNT := 4
const CONTROL_INCOME_INTERVAL_SECONDS := 60.0
const OUTPOST_INCOME_AMOUNT := 2
const OUTPOST_INCOME_INTERVAL_SECONDS := 30.0

var gold: int
var food_cap: int
var food_used := 0

var _base_income_elapsed := 0.0
var _control_income_elapsed := 0.0
var _outpost_income_elapsed := 0.0


func _init(manifest: StageManifest) -> void:
	gold = manifest.starting_gold
	food_cap = manifest.starting_food_cap


func advance(delta: float, controlled_clash_count: int, stable_owned_outpost_count: int) -> void:
	var active_delta := maxf(0.0, delta)
	_base_income_elapsed += active_delta
	_control_income_elapsed += active_delta
	_outpost_income_elapsed += active_delta
	while _base_income_elapsed + 0.000001 >= BASE_INCOME_INTERVAL_SECONDS:
		_base_income_elapsed -= BASE_INCOME_INTERVAL_SECONDS
		gold += BASE_INCOME_AMOUNT
	while _control_income_elapsed + 0.000001 >= CONTROL_INCOME_INTERVAL_SECONDS:
		_control_income_elapsed -= CONTROL_INCOME_INTERVAL_SECONDS
		gold += CONTROL_INCOME_AMOUNT * maxi(0, controlled_clash_count)
	while _outpost_income_elapsed + 0.000001 >= OUTPOST_INCOME_INTERVAL_SECONDS:
		_outpost_income_elapsed -= OUTPOST_INCOME_INTERVAL_SECONDS
		gold += OUTPOST_INCOME_AMOUNT * maxi(0, stable_owned_outpost_count)


func try_spend_gold(amount: int) -> bool:
	if amount < 0 or gold < amount:
		return false
	gold -= amount
	return true


func add_gold(amount: int) -> void:
	gold += maxi(0, amount)


func add_food_cap(amount: int) -> void:
	food_cap += maxi(0, amount)


func remove_food_cap(amount: int) -> void:
	food_cap = maxi(0, food_cap - maxi(0, amount))


func try_reserve_food(amount: int) -> bool:
	if amount <= 0 or food_used + amount > food_cap:
		return false
	food_used += amount
	return true
