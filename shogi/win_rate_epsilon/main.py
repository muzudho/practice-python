# cd shogi/black_win_rate_epsilon
# python main.py


def main():
    # 全勝とか、全敗は避ける。0除算で計算できないから
    for black_win_rounds in range(1,99):

        all_rounds = 100
        white_win_rounds = all_rounds - black_win_rounds

        # 先手勝率
        black_win_rate = black_win_rounds / all_rounds
        print(f"black_win_rate:{black_win_rate}")

        black_divider = (2*black_win_rate)
        if black_divider != 0:
            black_win_point = 1 / black_divider
            print(f"black_win_point:{black_win_point:20.16f}")
        else:
            black_win_point = 0
            print(f"black_win_point:0 div error")

        white_divider = (2*(1-black_win_rate))
        if white_divider != 0:
            white_win_point = 1 / white_divider
            print(f"white_win_point:{white_win_point:20.16f}")
        else:
            white_win_point = 0
            print(f"white_win_point:0 div error")


        # 順当勝敗ケース
        black_win_point_total = black_win_rounds * black_win_point
        white_win_point_total = white_win_rounds * white_win_point
        print(f"黒の {black_win_rounds} 勝 {white_win_rounds} 敗のケース")
        print(f"    黒計:{black_win_point_total:20.16f}")
        print(f"    白計:{white_win_point_total:20.16f}")

if __name__ == "__main__":
    main()
