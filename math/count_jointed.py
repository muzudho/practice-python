genre_code_list = ['green', 'green', 'blue', 'red', 'red',
                   'blue', 'yellow', 'black', 'black', 'black']
block_list = ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C']


def count_joined_genre_code():
    """
    TODO 同じブロック内での、連続するジャンルコードの数。
    """

    count = 0
    result_dict = {}
    prev_block = None
    prev_genre_code = None
    for idx in range(0, len(block_list)):
        block = block_list[idx]
        genre_code = genre_code_list[idx]
        if prev_block != block or prev_genre_code != genre_code:
            if prev_block not in result_dict:
                result_dict[prev_block] = []

            result_dict[prev_block].append(count)
            count = 1
        else:
            count += 1

        prev_block = block
        prev_genre_code = genre_code

    # last
    if prev_block not in result_dict:
        result_dict[prev_block] = []
    result_dict[prev_block].append(count)

    return result_dict


result_dict = count_joined_genre_code()
print("result_dict: {}.".format(result_dict))
