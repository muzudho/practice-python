# cd shogi/new_rule
# python simulation.py

import random

def main():
    def get_sente_win_point(sente_win_rate):
        """先手の勝ち点"""
        return 1 / (2 * sente_win_rate)


    def get_gote_win_point(sente_win_rate):
        """後手の勝ち点"""
        return 1 - get_sente_win_point(sente_win_rate)


    # 強さの異なる対局者が10人居るとする
    player_strength = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    ]

    # 将棋の先手勝率
    sente_win_rate = 0.7

    # 先手が勝った時の、先手がもらえる勝ち点
    sente_win_point = get_sente_win_point(sente_win_rate)
    gote_win_point = get_gote_win_point(sente_win_rate)


    # 対局者の強さの配列のインデックス
    matching = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ]


    # 先手の勝ちか？
    def is_sente_win(sente_index, gote_index):
        sente_strength = player_strength[sente_index]
        players_total = sente_strength + player_strength[gote_index]
        rnd = random.randint(0, players_total)

        if rnd < sente_strength:
            return True

        return False


    # 数回対局
    for round in range(0, 10):
        print(f"round {round}. {is_sente_win(3,3)}")


if __name__ == "__main__":
    main()
