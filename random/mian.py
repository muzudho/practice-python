import os
import sys
import random

rng = random.SystemRandom()
print(rng.randint(0, sys.maxsize))
for i in range(0, 100):
    print(rng.randrange(0, 2))
