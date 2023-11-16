# cd shogi
# main.py

def calculate(games, draw_games, sente_win_rate, sente_win_on_draw):
    calc_sente_win = (games - draw_games) * sente_win_rate + draw_games * sente_win_on_draw

    print(f"""\
    対局数：{games}
    持将棋数：{draw_games}
    先手勝率：{sente_win_rate}
    持将棋時の先手勝星：{sente_win_on_draw}
    計算後の先手の勝率：{calc_sente_win}
""")


# 対局数を 1000 固定とする
games = 1000

# ［将棋の真の引分けの数］が増えていくことをシミュレーションする（千日手、上限手数）
for i_draw_games in [0, 250, 333, 500, 666, 750, 1000]:

    # ［将棋の真の先手勝率］の各ケースをシミュレーションする
    for i_sente_win_rate in [0.45, 0.5, 0.55, 0.6, 0.65, 0.7]:

        calculate(
                # 対局数
                games = games,
                # 持将棋数
                draw_games = i_draw_games,
                # 先手勝率
                sente_win_rate = i_sente_win_rate,
                # 持将棋時の先手勝星
                sente_win_on_draw = 0.4)


calculate(
        # 対局数
        games = games,
        # 持将棋数
        draw_games = 666,
        # 先手勝率
        sente_win_rate = 0.7,
        # 持将棋時の先手勝星
        sente_win_on_draw = 0.4)


calculate(
        # 対局数
        games = games,
        # 持将棋数
        draw_games = 100,
        # 先手勝率
        sente_win_rate = 0.7,
        # 持将棋時の先手勝星
        sente_win_on_draw = 0.4)


calculate(
        # 対局数
        games = games,
        # 持将棋数
        draw_games = 100,
        # 先手勝率
        sente_win_rate = 0.6,
        # 持将棋時の先手勝星
        sente_win_on_draw = 0.4)
