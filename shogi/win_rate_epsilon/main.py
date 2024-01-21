# cd shogi/win_rate_epsilon
# python main.py


def main():
    black_win_rounds = 75

    all_rounds = 100
    white_win_rounds = all_rounds - black_win_rounds

    win_rate = black_win_rounds / all_rounds
    print(f"win_rate:{win_rate}")

    black_win_point = 1 / (2*win_rate)
    print(f"black_win_point:{black_win_point}")

    white_win_point = 1 - black_win_point
    print(f"white_win_point:{white_win_point}")

    # 順当勝敗ケース
    black_win_point_total = black_win_rounds * black_win_point
    white_win_point_total = white_win_rounds * white_win_point
    print(f"黒の {black_win_rounds} 勝 {white_win_rounds} 敗のケースa 黒計:{black_win_point_total} 白計:{white_win_point_total}")

    black_win_point_b = 1 / (2*win_rate)
    print(f"black_win_point_b:{black_win_point_b}")

    white_win_point_b = 1 / (2*(1-win_rate))
    #white_win_point_b = 2 - black_win_point_b
    #divider = 1-(2*win_rate)
    #if 1-(2*win_rate) != 0:
    #    white_win_point_b = -1 * (1 / divider)
    #else:
    #    white_win_point_b = 0

    print(f"white_win_point_b:{white_win_point_b}")

    # 順当勝敗ケース
    black_win_point_total_b = black_win_rounds * black_win_point_b
    white_win_point_total_b = white_win_rounds * white_win_point_b
    print(f"黒の {black_win_rounds} 勝 {white_win_rounds} 敗のケースb 黒計:{black_win_point_total_b} 白計:{white_win_point_total_b}")

if __name__ == "__main__":
    main()
