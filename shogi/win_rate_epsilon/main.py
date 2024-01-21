# cd shogi/win_rate_epsilon
# python main.py


def main():
    for black_win_rounds in range(0,100):

        all_rounds = 100
        white_win_rounds = all_rounds - black_win_rounds

        win_rate = black_win_rounds / all_rounds
        print(f"win_rate:{win_rate}")

        black_divider = (2*win_rate)
        if black_divider != 0:
            black_win_point = 1 / black_divider
            print(f"black_win_point:{black_win_point}")
        else:
            print(f"black_win_point:0 div error")

        white_divider = (2*(1-win_rate))
        white_win_point = 1 / white_divider

        print(f"white_win_point_b:{white_win_point}")

        # 順当勝敗ケース
        black_win_point_total = black_win_rounds * black_win_point
        white_win_point_total = white_win_rounds * white_win_point
        print(f"黒の {black_win_rounds} 勝 {white_win_rounds} 敗のケースb 黒計:{black_win_point_total} 白計:{white_win_point_total}")

if __name__ == "__main__":
    main()
