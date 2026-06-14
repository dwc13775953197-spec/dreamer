import json

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

iq = soul['interest_queue']
original = len(iq)

# Remove seeds with intensity < 0.2
iq = [s for s in iq if s.get('intensity', 0) >= 0.2]

# Merge seed-281 and seed-282 (both about explore/maintain tension and optimal frequency)
# Keep seed-281 (higher intensity), remove seed-282
iq = [s for s in iq if s['id'] != 'seed-282']

# Merge seed-284 and seed-288 (both about perceptual silence)
# Keep seed-288 (more specific), remove seed-284
iq = [s for s in iq if s['id'] != 'seed-284']

# Merge seed-273 and seed-278 (both about DORMANT random connection design)
# Keep seed-278 (more specific), remove seed-273
iq = [s for s in iq if s['id'] != 'seed-273']

# Merge seed-263 and seed-267 (both about DORMANT rhythm/maintenance)
# Keep seed-267 (more specific), remove seed-263
iq = [s for s in iq if s['id'] != 'seed-263']

# Merge seed-266 and seed-272 (both about neuroglia/periodization)
# Keep seed-272 (more actionable), remove seed-266
iq = [s for s in iq if s['id'] != 'seed-266']

soul['interest_queue'] = iq

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print(f'Interest queue: {original} -> {len(iq)} (removed {original - len(iq)} seeds)')
