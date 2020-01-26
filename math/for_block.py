participants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
blocks = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B']
print("participants: {}.".format(participants))
print("blocks: {}.".format(blocks))


def for_block_asc(callback_head_block, callback_same_block):
    """
    ブロックの切れ目が分かるループです。昇順。
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


def for_block_desc(callback_tail_block, callback_same_block):
    """
    ブロックの切れ目が分かるループです。降順。
    """
    # テーブルID順に並んでいるとします。
    prev_block = None
    for i in reversed(range(0, len(blocks))):
        if prev_block == blocks[i]:
            callback_same_block(i, blocks[i])
        else:
            callback_tail_block(i, blocks[i])
        prev_block = blocks[i]
    return


print("Info    : for_block_asc.")
for_block_asc(
    lambda i, block:
        print("Head: i={}, block={}.".format(i, block)),
    lambda i, block:
        print("Same: i={}, block={}.".format(i, block))
)

print("Info    : for_block_desc.")
for_block_desc(
    lambda i, block:
        print("Tail: i={}, block={}.".format(i, block)),
    lambda i, block:
        print("Same: i={}, block={}.".format(i, block))
)

print("Info    : Finished.")
