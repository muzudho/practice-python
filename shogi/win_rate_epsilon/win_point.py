# cd shogi/black_win_rate_epsilon
# python win_point.py


def main():
    all_rounds = 100

    # 全勝とか、全敗は避ける。0除算で計算できないから
    for black_win_rounds in range(1,99):

        white_win_rounds = all_rounds - black_win_rounds

        # 先手勝率
        black_win_rate = black_win_rounds / all_rounds

        #                          1
        # 黒の勝ち得点　＝　--------------------
        #                 2 * black_win_rate
        #
        #                            1
        # 白の勝ち得点　＝　--------------------------
        #                 2 * (1 - black_win_rate)
        #
        # ※ 0 除算しないように注意
        black_win_point = 1 / (2*black_win_rate)
        white_win_point = 1 / (2*(1-black_win_rate))

        # 順当勝敗ケース
        black_win_point_total = black_win_rounds * black_win_point
        white_win_point_total = white_win_rounds * white_win_point
        print(f"""\
先手勝率: {black_win_rate} のとき、
    黒の勝ち点: {black_win_point:20.16f}
    白の勝ち点: {white_win_point:20.16f}
    にすれば、黒の {black_win_rounds} 勝 {white_win_rounds} 敗のケースでの合計点は、
        黒計:{black_win_point_total:20.16f}
        白計:{white_win_point_total:20.16f}
""")

if __name__ == "__main__":
    main()
