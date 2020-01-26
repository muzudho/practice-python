participants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
blocks = ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C']
print("participants: {}.".format(participants))
print("blocks: {}.".format(blocks))


def shift_smaller():
    """
    ブロック単位でシフトします。[1,2,3,4]を、[2,3,4,1]にする動きです。
    """

    prev_block = None
    # テーブルID順に並んでいるとします。
    for i in range(0, 10):
        print("i:{}, blocks[i]: {}, prev_block: {}.".format(
            i, blocks[i], prev_block))
        if prev_block == blocks[i]:
            # Swap.
            temp = participants[i-1]
            participants[i-1] = participants[i]
            participants[i] = temp

        prev_block = blocks[i]


def shift_bigger():
    """
    ブロック単位でシフトします。[1,2,3,4]を、[4, 1, 2, 3]にする動きです。
    """

    prev_block = None
    # テーブルID順に並んでいるとします。
    for i in reversed(range(0, 10)):
        print("i:{}, blocks[i]: {}, prev_block: {}.".format(
            i, blocks[i], prev_block))
        if prev_block == blocks[i]:
            # Swap.
            temp = participants[i]
            participants[i] = participants[i+1]
            participants[i+1] = temp

        prev_block = blocks[i]


# shift_smaller()
shift_bigger()

print("participants: {}.".format(participants))
