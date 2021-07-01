# Longest increase subsequence

cards = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]
subseq = []
min_index = 0
minimum = -1

for j in range(0, 5):
    pre_minimum = minimum
    minimum = 999

    for i in range(min_index, len(cards)):
        if pre_minimum < cards[i] and cards[i] < minimum:
            minimum = cards[i]
            min_index = i
        pass

    print(f"({j}周目) minimum={minimum} min_index={min_index}")
