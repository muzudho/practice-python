import os
import sys
import random


def get_distribution():

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

    for i in range(0, 100):
        hits = person[i]
        if not hits in distribution:
            distribution[hits] = 1
        else:
            distribution[hits] += 1

    return distribution


distribution_of_dist = {}

for i in range(0, 100):
    dist = get_distribution()
    for k, v in dist.items():
        if not k in distribution_of_dist:
            distribution_of_dist[k] = v
        else:
            distribution_of_dist[k] += v

    print("""
    +
    | Distribution of distribution
    +
    """)
    for k, v in distribution_of_dist.items():
        print("[{}] {}".format(k, v))
