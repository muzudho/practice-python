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


calculate(
        # 対局数
        games = 1000,
        # 持将棋数
        draw_games = 666,
        # 先手勝率
        sente_win_rate = 0.7,
        # 持将棋時の先手勝星
        sente_win_on_draw = 0.4)


calculate(
        # 対局数
        games = 1000,
        # 持将棋数
        draw_games = 100,
        # 先手勝率
        sente_win_rate = 0.7,
        # 持将棋時の先手勝星
        sente_win_on_draw = 0.4)


calculate(
        # 対局数
        games = 1000,
        # 持将棋数
        draw_games = 100,
        # 先手勝率
        sente_win_rate = 0.6,
        # 持将棋時の先手勝星
        sente_win_on_draw = 0.4)
