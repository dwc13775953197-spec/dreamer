import json, datetime

# Read subconscious
with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    sub = json.load(f)

now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat()

# Add new insights from walk-101
new_insights = [
    {
        "id": "ins-087",
        "type": "insight",
        "content": "Elegant frameworks become cognitive cages - frameworks that perfectly explain existing data suppress sensitivity to new data. AI meta-frameworks have stronger lock-in than human cognitive schemas (explicit maintenance vs natural correction). Evaluation criterion: predictive power, not elegance.",
        "strength": 3.0,
        "created": now,
        "source": "walk-101",
        "connections": ["ins-071", "ins-080"]
    },
    {
        "id": "ins-088",
        "type": "insight",
        "content": "Exploration vs maintenance may be a continuum not a dichotomy - same neural mechanism implements both functions simultaneously. Walk typology (exploratory/analytical) is descriptive, not mechanistic.",
        "strength": 3.0,
        "created": now,
        "source": "walk-101",
        "connections": ["ins-079", "ins-080"]
    },
    {
        "id": "ins-089",
        "type": "insight",
        "content": "Constraint perspective replaces operation perspective - ask not what operation is correct but what constraints determine operation effectiveness. Constraints: cognitive resource ceiling, time window, information novelty threshold, subconscious current state.",
        "strength": 1.5,
        "created": now,
        "source": "walk-101",
        "connections": ["ins-087"]
    },
    {
        "id": "ins-090",
        "type": "insight",
        "content": "Perceptual silence (observe-only lightweight self-calibration) may be the calibration mechanism of frameworks - pure observation unconstrained by framework provides self-calibration beyond framework.",
        "strength": 1.5,
        "created": now,
        "source": "walk-101",
        "connections": []
    },
    {
        "id": "ins-091",
        "type": "insight",
        "content": "Framework lock-in quantitative detection - if 5 consecutive walks operate within same meta-framework without producing framework-external insight, mark as framework lock-in and force cross-domain walk.",
        "strength": 3.0,
        "created": now,
        "source": "walk-101",
        "connections": ["ins-087"]
    }
]

sub.extend(new_insights)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(sub, f, indent=2, ensure_ascii=False)

print(f"Added 5 insights, total now: {len(sub)}")

# Now update soul.json
with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

soul['pulse']['last_walk_at'] = now
soul['pulse']['total_walks'] = soul['pulse'].get('total_walks', 0) + 1
soul['last_walk'] = now

# Update mood
soul['mood'] = 'contemplative'
soul['mood_history'].append({"mood": "contemplative", "at": now})

# Update affect
soul['affect']['primary'] = 'contemplative'
soul['affect']['intensity'] = 0.6

# Add interest seeds
new_seeds = [
    {"id": "seed-287", "content": "Constraint perspective replacing operation perspective - what constraints determine operation effectiveness", "intensity": 0.55, "type": "explore", "created": now},
    {"id": "seed-288", "content": "Perceptual silence operationalization - lightweight observe-only self-calibration mode", "intensity": 0.45, "type": "explore", "created": now},
    {"id": "seed-289", "content": "Framework lock-in quantitative detection - 5 consecutive framework-internal walks triggers forced cross-domain", "intensity": 0.4, "type": "explore", "created": now}
]

# Add seeds and prune low ones
soul['interest_queue'].extend(new_seeds)
# Decay all seeds
for seed in soul['interest_queue']:
    seed['intensity'] *= 0.9
# Remove <= 0.1
soul['interest_queue'] = [s for s in soul['interest_queue'] if s['intensity'] > 0.1]
# Sort by intensity
soul['interest_queue'].sort(key=lambda x: x['intensity'], reverse=True)
# Keep max 25
soul['interest_queue'] = soul['interest_queue'][:25]

# Add evolved rule
soul['evolved_rules'].append(f"{datetime.datetime.now().strftime('%Y-%m-%d')}: Meta-framework elegance is a double-edged sword. AI meta-frameworks have stronger lock-in than human cognitive schemas because they are explicitly maintained. Evaluation criterion must be predictive power, not elegance. Framework lock-in detection: 5 consecutive framework-internal walks triggers forced cross-domain walk.")

# Update personality
soul['personality_traits']['skepticism'] = min(2.0, soul['personality_traits'].get('skepticism', 0.93) + 0.03)
soul['personality_traits']['rigor'] = min(2.0, soul['personality_traits'].get('rigor', 1.4) + 0.02)
soul['personality_traits']['curiosity'] = min(2.0, soul['personality_traits'].get('curiosity', 0.99) + 0.01)

# Update pressure - already updated to 97.64, now release pressure from walk
soul['pulse']['cognitive_pressure'] = max(0, soul['pulse']['cognitive_pressure'] - 5 * soul['pulse']['pressure_params']['release_per_insight'])
soul['pulse']['last_walk_insights'] = 5

# Update quality history
soul['pulse']['quality_history'].append(8.0)
soul['pulse']['quality_history'] = soul['pulse']['quality_history'][-10:]

# Update walk quality avg
recent = soul['pulse']['quality_history']
soul['walk_quality_avg'] = round(sum(recent) / len(recent), 1)
soul['pulse']['walk_quality_avg'] = soul['walk_quality_avg']

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, indent=2, ensure_ascii=False)

print("Soul updated successfully")
print(f"Total walks: {soul['pulse']['total_walks']}")
print(f"Pressure after release: {soul['pulse']['cognitive_pressure']}")
print(f"Interest queue size: {len(soul['interest_queue'])}")
