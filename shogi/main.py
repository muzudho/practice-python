# cd shogi
# main.py

def calculate(jishogi_rate, sente_win_rate):
    normal_game_rate = 1.0 - jishogi_rate
    sente_win_rate_on_normal_game = normal_game_rate * sente_win_rate
    gote_win_rate_on_normal_game = normal_game_rate - sente_win_rate_on_normal_game

    sente_win_on_draw = (0.5 - normal_game_rate * sente_win_rate_on_normal_game) / jishogi_rate

    # 0.5 = normal_game_rate * sente_win_rate_on_normal_game + jishogi_rate * sente_win_on_draw
    #   0 = (normal_game_rate * sente_win_rate_on_normal_game + jishogi_rate * sente_win_on_draw) - 0.5
    # -(normal_game_rate * sente_win_rate_on_normal_game + jishogi_rate * sente_win_on_draw) = - 0.5
    # normal_game_rate * sente_win_rate_on_normal_game + jishogi_rate * sente_win_on_draw = 0.5
    # jishogi_rate * sente_win_on_draw = 0.5 - normal_game_rate * sente_win_rate_on_normal_game
    # sente_win_on_draw = (0.5 - normal_game_rate * sente_win_rate_on_normal_game) / jishogi_rate

    # 0.5 を目指す
    half = normal_game_rate * sente_win_rate_on_normal_game + jishogi_rate * sente_win_on_draw

    print(f"""\
    将棋の真の持将棋率　　　：{jishogi_rate}
    将棋の真の勝ち負け決着率：{normal_game_rate}
    将棋の真の先手勝率　　　：{sente_win_rate}
    先手勝利で決着する率　　：{sente_win_rate_on_normal_game}
    後手勝利で決着する率　　：{gote_win_rate_on_normal_game}
    先後の差を０にする持将棋時の先手勝星：約 {sente_win_on_draw}
    Check 0.5 =　　　　　：{half}
""")


# ［将棋の真の引分けの数］が増えていくことをシミュレーションする（千日手、上限手数）
for i_jishogi_rate in [2/3]: # [0.0, 0.25, 0.333, 0.5, 0.666, 0.75, 1.0]:

    # ［将棋の真の先手勝率］の各ケースをシミュレーションする
    for i_sente_win_rate in [0.7]: # [0.45, 0.5, 0.55, 0.6, 0.65, 0.7]:

        calculate(
                # 将棋の真の持将棋率
                jishogi_rate = i_jishogi_rate,
                # 先手勝率
                sente_win_rate = i_sente_win_rate)
