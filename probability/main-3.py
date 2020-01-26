import os
import sys
import random


def is_hit():
    rng = random.SystemRandom()
    lottery = rng.randrange(0, 100)
    return lottery == 0


person = [0] * 100

for _challenge in range(0, 100):
    for i in range(0, 100):
        if is_hit():
            person[i] += 1

distribution = {}

print("""
+
| Lottery
+
""")
for i in range(0, 100):
    hits = person[i]
    print("[{}] {}".format(i, hits))

    if not hits in distribution:
        distribution[hits] = 1
    else:
        distribution[hits] += 1

print("""
+
| Distribution
+
""")
for k, v in distribution.items():
    print("[{}] {}".format(k, v))
