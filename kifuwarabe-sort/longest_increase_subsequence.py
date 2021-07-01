# Longest increase subsequence

cards = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]
subseq = []
min_index = 0
minimum = -1
count = 1

while True:
    pre_minimum = minimum
    minimum = 999

    for i in range(min_index, len(cards)):
        if pre_minimum < cards[i] and cards[i] < minimum:
            minimum = cards[i]
            min_index = i
        pass

    # 停止条件
    if minimum == 999:
        break

    print(f"({count}周目) minimum={minimum} min_index={min_index}")
    count += 1
