class_name BootstrapCatalog
extends Resource

const StageDefinition = preload("res://scripts/data/stage_definition.gd")

@export var archetypes: Array[UnitArchetypeProfile] = []
@export var tier_profiles: Array[TierProfile] = []
@export var rank_profiles: Array[RankProfile] = []
@export var attack_profiles: Array[AttackProfile] = []
@export var animation_contracts: Array[AnimationContract] = []
@export var faction_visual_profiles: Array[FactionVisualProfile] = []
@export var battlefield_profile: BattlefieldProfile
@export var boss_behavior_packages: Array[BossBehaviorPackage] = []
@export var boss_phase_profiles: Array[BossPhaseProfile] = []
@export var stages: Array[StageDefinition] = []
