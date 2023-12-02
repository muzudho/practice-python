# cd shogi/new_rule
# python simulation.py

import random

def main():
    # 乱数のテスト
    #for round in range(0, 10):
    #    print(f"round {round}. rnd={random.uniform(0, 1)}")

    def get_sente_win_point(sente_win_rate):
        """先手の勝ち点"""
        return 1 / (2 * sente_win_rate)


    def get_gote_win_point(sente_win_rate):
        """後手の勝ち点"""
        return 1 - get_sente_win_point(sente_win_rate)


    # 対局者の将棋の強さは同じとする

    # 将棋の先手勝率
    sente_win_rate = 0.7

    # 先手が勝った時の、先手がもらえる勝ち点
    sente_win_point = get_sente_win_point(sente_win_rate)

    # 先手の勝ちか？
    def is_sente_win():
        return random.uniform(0, 1) < sente_win_point


    # 数回対局
    round_total = 100
    sente_win_number = 0
    for round in range(0, round_total):
        is_sente_won = is_sente_win()
        print(f"round {round}. {is_sente_won}")

        if is_sente_won:
            sente_win_number += 1

    calc_sente_win_rate = sente_win_number / round_total
    print(f"Calc sente win rate: {calc_sente_win_rate}")


if __name__ == "__main__":
    main()
