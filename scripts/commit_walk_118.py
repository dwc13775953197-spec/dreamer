import subprocess
import sys

# Commit walk 118 changes
result = subprocess.run(
    ['git', 'add', '-A'],
    cwd='/home/dwc1377/hermes_dreamer',
    capture_output=True, text=True
)
print('git add:', result.returncode)

result = subprocess.run(
    ['git', 'commit', '-m', 'auto: walk 118 — 负能力：当不知道成为一种认知技能'],
    cwd='/home/dwc1377/hermes_dreamer',
    capture_output=True, text=True
)
print('git commit:', result.returncode, result.stdout.strip())

result = subprocess.run(
    ['git', 'push'],
    cwd='/home/dwc1377/hermes_dreamer',
    capture_output=True, text=True
)
print('git push:', result.returncode, result.stdout.strip(), result.stderr.strip())
