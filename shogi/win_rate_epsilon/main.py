# cd shogi/win_rate_epsilon
# python main.py


def main():
    all_rounds = 100
    black_win_rounds = 75
    white_win_rounds = all_rounds - black_win_rounds

    win_rate = black_win_rounds / all_rounds
    print(f"win_rate:{win_rate}")

    black_win_point = 1 / (2*win_rate)
    print(f"black_win_point:{black_win_point}")

    white_win_point = 1 - black_win_point
    print(f"white_win_point:{white_win_point}")

    # 順当勝敗ケース
    black_win_point_total = 75 * black_win_point
    white_win_point_total = 25 * white_win_point
    print(f"黒の {black_win_rounds} 勝 {white_win_rounds} 敗のケースa 黒計:{black_win_point_total} 白計:{white_win_point_total}")

    black_win_point_b = 1 / (2*win_rate)
    print(f"black_win_point_b:{black_win_point_b}")

    white_win_point_b = -1 * (1 / (1-(2*win_rate)))
    print(f"white_win_point_b:{white_win_point_b}")

    # 順当勝敗ケース
    black_win_point_total_b = 75 * black_win_point_b
    white_win_point_total_b = 25 * white_win_point_b
    print(f"黒の {black_win_rounds} 勝 {white_win_rounds} 敗のケースb 黒計:{black_win_point_total_b} 白計:{white_win_point_total_b}")

if __name__ == "__main__":
    main()
