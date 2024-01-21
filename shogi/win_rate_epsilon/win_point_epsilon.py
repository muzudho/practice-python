# cd shogi/black_win_rate_epsilon
# python win_point_epsilon.py


def main():
    all_rounds = 100

    # 全勝とか、全敗は避ける。0除算で計算できないから
    for black_win_rounds in range(1,all_rounds):

        white_win_rounds = all_rounds - black_win_rounds

        # 先手勝率
        black_win_rate = black_win_rounds / all_rounds

        # ※ 以下、 0 除算しないために、先手勝率は 0 より大きく 1 より小さいものとする
        #
        #                              1
        # 先手の１勝の値打ち　＝　--------------------
        #                       2 * black_win_rate
        #
        #                                 1
        # 後手の１勝の値打ち　＝　--------------------------
        #                       2 * (1 - black_win_rate)
        #
        # 先手の１勝時の点の交通量　＝　先手の１勝の値打ち　×　(2 / （先手の１勝の値打ち ＋ 後手の１勝の値打ち）)
        # 後手の１勝時の点の交通量　＝　後手の１勝の値打ち　×　(2 / （先手の１勝の値打ち ＋ 後手の１勝の値打ち）)
        #
        # ※ 先手と後手の合計が 2勝 になるように引き延ばす
        # 先手の１勝の加点　＝　先手の１勝時の点の交通量 / 2
        # 後手の１敗の減点　＝　－（先手の１勝時の点の交通量 / 2）
        #
        # 後手の１勝の加点　＝　後手の１勝時の点の交通量 / 2
        # 先手の１敗の減点　＝　－（後手の１勝時の点の交通量 / 2）
        #
        black_win_point_a = 1 / (2*black_win_rate)
        white_win_point_a = 1 / (2*(1-black_win_rate))
        all_win_point_a = black_win_point_a + white_win_point_a
        #
        all_win_point_b = 2.0
        ratio = all_win_point_b / all_win_point_a
        black_win_moving_point = black_win_point_a * ratio   # 先手の１勝時の点の交通量
        white_win_moving_point = white_win_point_a * ratio   # 後手の１勝時の点の交通量
        black_win_point_b = black_win_moving_point / 2
        white_lose_point_b = - black_win_moving_point / 2
        white_win_point_b = white_win_moving_point / 2
        black_lose_point_b = - white_win_moving_point / 2

        # 順当勝敗ケース
        black_win_point_total = black_win_rounds * black_win_point_b + white_win_rounds * black_lose_point_b
        white_win_point_total = white_win_rounds * white_win_point_b + black_win_rounds * white_lose_point_b
        sum_win_point_total = black_win_point_total + white_win_point_total
        print(f"""\
先手勝率: {black_win_rate} のとき、
    先手の１勝の値打ち　　　: {black_win_point_a:20.16f}
    後手の１勝の値打ち　　　: {white_win_point_b:20.16f}
    先手の１勝時の点の交通量: {black_win_moving_point:20.16f}
    後手の１勝時の点の交通量: {white_win_moving_point:20.16f}
    先手の１勝の加点　　　　: {black_win_point_b:20.16f}
    後手の１敗の減点　　　　: {white_lose_point_b:20.16f}
    後手の１勝の加点　　　　: {white_win_point_b:20.16f}
    先手の１敗の減点　　　　: {black_lose_point_b:20.16f}
    にすれば、ゼロ・サムを保つ。　ここで、黒の {black_win_rounds} 勝 {white_win_rounds} 敗のケースで先手、後手の各々の点はまるでイプシロン（ε＝限りなくゼロに近い数）のようだ
        黒計:{black_win_point_total:20.16f}
        白計:{white_win_point_total:20.16f}
        総計:{sum_win_point_total:20.16f}
""")

if __name__ == "__main__":
    main()
