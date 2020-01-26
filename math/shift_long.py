participants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
blocks = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B']
print("participants: {}.".format(participants))
print("blocks: {}.".format(blocks))


def for_block_asc(callback_head_block, callback_same_block):
    """
    指定のブロックのところだけ callback を呼び出します。
    """
    # テーブルID順に並んでいるとします。
    prev_block = None
    for i in range(0, len(blocks)):
        if prev_block == blocks[i]:
            callback_same_block(i, blocks[i])
        else:
            callback_head_block(i, blocks[i])
        prev_block = blocks[i]
    return


for_block_asc(
    lambda i, block:
        print("Head: i={}, block={}.".format(i, block)),
    lambda i, block:
        print("Same: i={}, block={}.".format(i, block))
)

'''
def shift_long_smaller(block, count):
    """
    ブロック単位でシフトします。
    count が 3 の場合、 [1,2,3,4,5] を、 [4,5,1,2,3] にする動きです。
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

    return
'''
