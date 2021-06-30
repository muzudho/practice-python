# [挿入ソート](https://ja.wikipedia.org/wiki/%E6%8C%BF%E5%85%A5%E3%82%BD%E3%83%BC%E3%83%88)
cards = ['E', 'D', 'C', 'B', 'A']

print(f"(S) {cards}")

for i in range(1, len(cards)):
    tmp = cards[i]
    if cards[i-1] > tmp:
        j = i
        while True:
            cards[j] = cards[j-1]
            j -= 1
            # print(f"(2) {cards}")
            if j > 0 and cards[j-1] > tmp:
                pass
            else:
                break
        cards[j] = tmp
    print(f"({i}) {cards}")

# print(f"(E) {cards}")
