# cd shogi
# main.py

def calculate(jishogi_rate, sente_win_rate, sente_win_on_draw):
    calc_sente_win = (1.0 - jishogi_rate) * sente_win_rate + jishogi_rate * sente_win_on_draw

    print(f"""\
    将棋の真の持将棋率：{jishogi_rate}
    将棋の真の先手勝率：{sente_win_rate}
    持将棋時の先手勝星：{sente_win_on_draw}
    計算後の先手の勝率：{calc_sente_win}
""")


# ［将棋の真の引分けの数］が増えていくことをシミュレーションする（千日手、上限手数）
for i_jishogi_rate in [0.0, 0.25, 0.333, 0.5, 0.666, 0.75, 1.0]:

    # ［将棋の真の先手勝率］の各ケースをシミュレーションする
    for i_sente_win_rate in [0.45, 0.5, 0.55, 0.6, 0.65, 0.7]:

        calculate(
                # 将棋の真の持将棋率
                jishogi_rate = i_jishogi_rate,
                # 先手勝率
                sente_win_rate = i_sente_win_rate,
                # 持将棋時の先手勝星
                sente_win_on_draw = 0.4)


calculate(
        # 将棋の真の持将棋率
        jishogi_rate = i_jishogi_rate,
        # 先手勝率
        sente_win_rate = 0.7,
        # 持将棋時の先手勝星
        sente_win_on_draw = 0.4)


calculate(
        # 将棋の真の持将棋率
        jishogi_rate = i_jishogi_rate,
        # 先手勝率
        sente_win_rate = 0.7,
        # 持将棋時の先手勝星
        sente_win_on_draw = 0.4)


calculate(
        # 将棋の真の持将棋率
        jishogi_rate = i_jishogi_rate,
        # 先手勝率
        sente_win_rate = 0.6,
        # 持将棋時の先手勝星
        sente_win_on_draw = 0.4)
