# [マージソート](https://ja.wikipedia.org/wiki/%E3%83%9E%E3%83%BC%E3%82%B8%E3%82%BD%E3%83%BC%E3%83%88)


def merge(cards, space, l_begin, mid, r_end):
    """
    cards : str[int]
        全部のカード。並び替えたい
    space : str[int]
        並び替えのために使う一時的なスペース。カードが全部入るだけのサイズがある
    l_begin : int
        左端。左側のスタート地点（＾～＾）
    mid : int
        真ん中。この数を含まない範囲で左から l が寄ってくる（＾～＾）右側のスタート地点でもある（＾～＾）
    r_end : int
        右端。この数を含まない範囲で左から r が寄ってくる（＾～＾）
    """
    l = l_begin
    r = mid

    # スワップ・スペースの配列の添え字
    s = 0

    # l も r も端を超えてなければ
    while l < mid and r < r_end:
        # 右側の方が小さい（か等しい）なら
        if cards[l] <= cards[r]:
            # 右側の方をスワップ・スペースの方へ移す
            space[s] = cards[l]
            l += 1
            s += 1
        else:
            # 左側の方
            space[s] = cards[r]
            r += 1
            s += 1

    if l == mid:  # 左側をスワップ・スペースに移動し尽くしたので、右側も順番にスワップ・スペースに入れていく
        while r < r_end:
            space[s] = cards[r]
            r += 1
            s += 1
    else:
        while l < mid:  # 左側の方
            space[s] = cards[l]
            l += 1
            s += 1

    # スワップ・スペースの内容を cards に戻す
    for s2 in range(0, s):
        cards[l_begin + s2] = space[s2]


def merge_sort(cards, space, l_begin, r_end):
    """左と右をマージ（＾～＾）"""

    # ０～１枚のカードを指してるようなら再帰を停止
    if l_begin == r_end or l_begin == r_end - 1:  # Base case
        return

    # 真ん中
    mid = (l_begin + r_end) // 2  # 小数点以下切り捨て（＾～＾）

    merge_sort(cards, space, l_begin, mid)
    merge_sort(cards, space, mid, r_end)
    merge(cards, space, l_begin, mid, r_end)

    # 途中結果（または最終結果）表示（＾～＾）
    print_all_cards(cards, l_begin, mid, r_end)


def print_all_cards(cards, l_begin, mid, r_end):
    """カードの表示"""
    begin_all = 0
    end_all = len(cards)
    for i in range(begin_all, end_all):
        if i == l_begin:
            print(" [ ", end='')
        elif i == mid:
            print(" | ", end='')
        elif i == r_end:
            print(" ] ", end='')
        print(f"{cards[i]} ", end='')

    if end_all == mid:
        print(" | ", end='')
    if end_all == r_end:
        print(" ] ", end='')

    print("")  # New line


def main():
    # 全部のカード
    cards = ['J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
    # スワップ・スペース。とりあえず配列のサイズを確保しとく
    space = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    l_begin = 0  # 左端
    r_end = len(cards)  # 右端

    # 初期配置表示（＾～＾）
    print_all_cards(cards, l_begin, r_end, r_end)

    merge_sort(cards, space, l_begin, r_end)


main()
