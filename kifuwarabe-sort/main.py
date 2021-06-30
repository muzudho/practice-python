cards = ['C', 'E', 'A', 'D', 'B']

print(f"(1) {cards}")

# in-placeなスワップ と呼ばれる技
temp = cards[2]
cards[2] = cards[1]
cards[1] = cards[0]
cards[0] = temp

print(f"(2) {cards}")

# in-placeなスワップ
temp = cards[4]
cards[4] = cards[3]
cards[3] = cards[2]
cards[2] = cards[1]
cards[1] = temp

print(f"(3) {cards}")

# in-placeなスワップ
temp = cards[4]
cards[4] = cards[3]
cards[3] = temp

print(f"(4) {cards}")
