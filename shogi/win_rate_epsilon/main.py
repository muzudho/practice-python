# cd shogi/win_rate_epsilon
# python main.py


def main():
    #win_rate = 0.5
    win_rate = 0.75
    print(f"win_rate:{win_rate}")

    black_win_point = 1 / (2*win_rate)
    print(f"black_win_point:{black_win_point}")

    white_win_point = 1 - black_win_point
    print(f"white_win_point:{white_win_point}")

    # 黒の25勝75敗のケース
    black_win_point_total = 25 * black_win_point
    white_win_point_total = 75 * white_win_point
    print(f"黒の25勝75敗のケース 黒計:{black_win_point_total} 白計:{white_win_point_total}")

    black_win_point_b = 2 / (2*win_rate)
    print(f"black_win_point_b:{black_win_point_b}")

    white_win_point_b = 2 - black_win_point_b
    print(f"white_win_point_b:{white_win_point_b}")

    # 黒の25勝75敗のケース
    black_win_point_total_b = 25 * black_win_point_b
    white_win_point_total_b = 75 * white_win_point_b
    print(f"黒の25勝75敗のケースb 黒計:{black_win_point_total_b} 白計:{white_win_point_total_b}")

if __name__ == "__main__":
    main()
