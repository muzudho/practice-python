# [マージソート](https://ja.wikipedia.org/wiki/%E3%83%9E%E3%83%BC%E3%82%B8%E3%82%BD%E3%83%BC%E3%83%88)


def merge(all_cards, swap_space, leftmost, mid, rightmost_end):
    """
    all_cards : str[int]
        全部のカード。並び替えたい
    swap_space : str[int]
        並び替えのために使う一時的なスペース。カードが全部入るだけのサイズがある
    leftmost : int
        左端。i のスタート地点（＾～＾）
    mid : int
        真ん中。この数を含まない範囲で左から i が寄ってくる（＾～＾）j のスタート地点でもある（＾～＾）
    rightmost_end : int
        右端。この数を含まない範囲で左から j が寄ってくる（＾～＾）
    """
    i = leftmost
    j = mid

    # スワップ・スペースの配列の添え字
    k = 0
    # l

    # i が 真ん中より下で、 j が　右端より左
    while i < mid and j < rightmost_end:
        # i側の方が小さい（か等しい）なら
        if all_cards[i] <= all_cards[j]:
            # i側の方をソート済みの方へ移す
            swap_space[k] = all_cards[i]
            i += 1
            k += 1
        else:
            # j側の方をソート済みの方へ移す
            swap_space[k] = all_cards[j]
            j += 1
            k += 1

    if i == mid:  # i側のAをBに移動し尽くしたので、j側も順番にBに入れていく
        while j < rightmost_end:
            swap_space[k] = all_cards[j]
            j += 1
            k += 1
    else:
        while i < mid:  # j側のAをBに移動し尽くしたので、i側も順番にBに入れていく
            swap_space[k] = all_cards[i]
            i += 1
            k += 1

    # B の内容を A に戻す
    for l in range(0, k):
        all_cards[leftmost + l] = swap_space[l]


def merge_sort(all_cards, swap_space, leftmost_of_segment, rightmost_of_segment):
    """左と右をマージ（＾～＾）
    all_cards: str[int]
        All cards
    swap_space: str[int]
        Swap space
    leftmost_of_segment: int
        区間の左端
    rightmost_of_segment: int
        区間の右端
    """

    print(
        f"leftmost={leftmost_of_segment} rightmost_of_segment={rightmost_of_segment}")

    # `leftmost_of_segment == rightmost_of_segment` - １枚のカードを指してるようなら再帰を停止
    # `leftmost_of_segment == rightmost_of_segment - 1` - もカードを指してないようなら再帰を停止
    if leftmost_of_segment == rightmost_of_segment or leftmost_of_segment == rightmost_of_segment - 1:  # Base case
        return

    # 真ん中
    mid = (leftmost_of_segment + rightmost_of_segment) // 2  # 小数点以下切り捨て（＾～＾）

    #
    merge_sort(all_cards, swap_space, leftmost_of_segment, mid)
    merge_sort(all_cards, swap_space, mid, rightmost_of_segment)

    # マージする
    merge(all_cards, swap_space, leftmost_of_segment, mid, rightmost_of_segment)


def main():
    all_cards = ['J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
    swap_space = [' ', ' ', ' ', ' ', ' ', ' ',
                  ' ', ' ', ' ', ' ']  # とりあえず配列のサイズを確保しとく

    leftmost = 0
    rightmost = len(all_cards)  # カードの総枚数（左端のカードの添え字はこの数を含まないので rightmost-1）
    merge_sort(all_cards, swap_space, leftmost, rightmost)

    # 表示（＾～＾）
    for i in range(leftmost, rightmost):
        print(f"{all_cards[i]} ", end='')
    print("")  # New line


main()
