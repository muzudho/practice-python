# cd shogi/win_rate_epsilon
# python win_point_epsilon.py


def main():
    all_rounds = 100

    # 全勝とか、全敗は避ける。0除算で計算できないから
    for black_win_rounds in range(50,all_rounds):

        white_win_rounds = all_rounds - black_win_rounds

        # 先手勝率
        black_win_rate = black_win_rounds / all_rounds

        # イプシロン勝ち点制
        # =================
        #
        # 先手勝率を　x　とする。
        #
        # 先手勝ちのとき
        # 　　先手の　１ ＋ ε　勝、　　... (a)
        # 　　後手の　１ ＋ ε　敗　　　... (b)
        #
        # 後手勝ちのとき
        # 　　後手の　２ － ε　勝、　　...(c)
        # 　　先手の　２ － ε　敗　　　...(d)
        #
        epsilon = black_win_rate ** black_win_rounds
        fomula_a = 1 + epsilon
        fomula_c = 2 - epsilon

        # 順当勝敗ケース
        black_win_point_total = black_win_rounds * fomula_a - white_win_rounds * fomula_c
        white_win_point_total = white_win_rounds * fomula_c - black_win_rounds * fomula_a
        sum_win_point_total = black_win_point_total + white_win_point_total
        # 後手の各々の点はまるでイプシロン（ε＝限りなくゼロに近い数）のようだ
        print(f"""\
先手勝率: {black_win_rate} のとき、
　　ε　　{epsilon}
　　式a　{fomula_a}
　　式c　{fomula_c}
　　先手勝ちなら
　　　　先手の　{fomula_a:20.16f}　勝、
　　　　後手の　{fomula_a:20.16f}　敗
　　後手勝ちなら
　　　　後手の　{fomula_c:20.16f}　勝、
　　　　先手の　{fomula_c:20.16f}　敗
    ここで、先手の {black_win_rounds} 勝 {white_win_rounds} 敗のケースの検算は以下の通り。
        先手計:{black_win_point_total:20.16f}
        後手計:{white_win_point_total:20.16f}
        総　計:{sum_win_point_total:20.16f}
""")

if __name__ == "__main__":
    main()
