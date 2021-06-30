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
    l = leftmost  # 左側のスタートは左端
    r = mid  # 右側のスタートは真ん中

    # スワップ・スペースの配列の添え字
    s = 0

    # l が 真ん中より下で、 j が　右端より左
    while l < mid and r < rightmost_end:
        # 右側の方が小さい（か等しい）なら
        if all_cards[l] <= all_cards[r]:
            # 右側の方をスワップ・スペースの方へ移す
            swap_space[s] = all_cards[l]
            l += 1
            s += 1
        else:
            # 左側の方をスワップ・スペースの方へ移す
            swap_space[s] = all_cards[r]
            r += 1
            s += 1

    if l == mid:  # 左側をスワップ・スペースに移動し尽くしたので、右側も順番にスワップ・スペースに入れていく
        while r < rightmost_end:
            swap_space[s] = all_cards[r]
            r += 1
            s += 1
    else:
        while l < mid:  # 右側をスワップ・スペースに移動し尽くしたので、左側も順番にスワップ・スペースに入れていく
            swap_space[s] = all_cards[l]
            l += 1
            s += 1

    # スワップ・スペースの内容を all_cards に戻す
    for s2 in range(0, s):
        all_cards[leftmost + s2] = swap_space[s2]


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

    # 途中結果（または最終結果）表示（＾～＾）
    print_all_cards(all_cards, leftmost_of_segment, mid, rightmost_of_segment)


def print_all_cards(all_cards, leftmost_of_segment, mid, rightmost_of_segment):
    """カードの表示"""
    leftmost = 0
    rightmost = len(all_cards)
    for i in range(leftmost, rightmost):
        if i == leftmost_of_segment:
            print(" [ ", end='')
        elif i == mid:
            print(" | ", end='')
        elif i == rightmost_of_segment:
            print(" ] ", end='')
        print(f"{all_cards[i]} ", end='')

    if rightmost == mid:
        print(" | ", end='')
    if rightmost == rightmost_of_segment:
        print(" ] ", end='')

    print("")  # New line


def main():
    all_cards = ['J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
    swap_space = [' ', ' ', ' ', ' ', ' ', ' ',
                  ' ', ' ', ' ', ' ']  # とりあえず配列のサイズを確保しとく

    leftmost = 0
    rightmost = len(all_cards)  # カードの総枚数（左端のカードの添え字はこの数を含まないので rightmost-1）

    # 初期配置表示（＾～＾）
    print_all_cards(all_cards, leftmost, rightmost, rightmost)

    merge_sort(all_cards, swap_space, leftmost, rightmost)


main()
