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
        #                             1
        # 先手の勝ち基礎点　＝　--------------------
        #                     2 * black_win_rate
        #
        #                               1
        # 後手の勝ち基礎点　＝　--------------------------
        #                     2 * (1 - black_win_rate)
        #
        # ※ 先手と後手の合計が 2 になるように引き延ばす
        # 先手の勝ち点　＝　先手の勝ち基礎点　×　(2 / （先手の勝ち基礎点 ＋ 先手の勝ち基礎点）)
        # 後手の勝ち点　＝　後手の勝ち基礎点　×　(2 / （後手の勝ち基礎点 ＋ 後手の勝ち基礎点）)
        #
        black_win_point_a = 1 / (2*black_win_rate)
        white_win_point_a = 1 / (2*(1-black_win_rate))
        all_win_point_a = black_win_point_a + white_win_point_a
        #
        all_win_point_b = 2.0
        ratio = all_win_point_b / all_win_point_a
        black_win_point_b = black_win_point_a * ratio
        white_win_point_b = white_win_point_a * ratio

        # 順当勝敗ケース
        black_win_point_total = black_win_rounds * black_win_point_b
        white_win_point_total = white_win_rounds * white_win_point_b
        print(f"""\
先手勝率: {black_win_rate} のとき、
    黒の勝ち点: {black_win_point_b:20.16f}
    白の勝ち点: {white_win_point_b:20.16f}
    にすれば、黒の {black_win_rounds} 勝 {white_win_rounds} 敗のケースでの合計点は、
        黒計:{black_win_point_total:20.16f}
        白計:{white_win_point_total:20.16f}
""")

if __name__ == "__main__":
    main()
