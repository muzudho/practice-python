# 素因数分解の練習
#
# cd math/prime_factorization
# python step1_1_1_0.py

import math

def factorize(n, debug=True):

    # int( ... ) だと、取りこぼしてしまうようだ。 math.ceil( ... ) とした
    # + 1 が必要
    a_max = math.ceil(math.log(n, 7))+1
    b_max = math.ceil(math.log(n, 5))+1
    c_max = math.ceil(math.log(n, 3))+1
    d_max = math.ceil(math.log(n, 2))+1

    reversed_a_list = list(reversed(range(0,a_max)))
    reversed_b_list = list(reversed(range(0,b_max)))
    reversed_c_list = list(reversed(range(0,c_max)))
    reversed_d_list = list(reversed(range(0,d_max)))

    for a in reversed_a_list:
        aa = 7 ** a

        # n 以下の小さな合成数 7a なら、とりあえず n から、それを引く
        if aa <= n:
            remain = n - aa

            if debug:
                print(f"(7x{a}) remain:{remain}")

            # 割り切れた
            if remain == 0:
                return [a, 0, 0, 0]

            # 余った数で続きをやる

            for b in reversed_b_list:
                bb = aa * 5 ** b

                if bb <= n:
                    remain = n - bb

                    if debug:
                        print(f"\t(7x{a} x 5x{b}) remain:{remain}")

                    # 割り切れた
                    if remain == 0:
                        return [a, b, 0, 0]

                    # 余った数で続きをやる

                    for c in reversed_c_list:
                        cc = bb * 3 ** c

                        if cc <= n:
                            remain = n - cc

                            if debug:
                                print(f"\t\t(7x{a} x 5x{b} x 3x{c}) remain:{remain}")

                            # 割り切れた
                            if remain == 0:
                                return [a, b, c, 0]

                            # 余った数で続きをやる

                            for d in reversed_d_list:
                                dd = cc * 2 ** d

                                if dd <= n:
                                    remain = n - dd

                                    if debug:
                                        print(f"\t\t\t(7x{a} x 5x{b} x 3x{c} x 2x{d}) remain:{remain}")

                                    # 割り切れた
                                    if remain == 0:
                                        return [a, b, c, d]


if __name__ == "__main__":
    
    print("""\
ある正の整数 n があるとする。
とりあえず n は 1～100 ぐらいを考えておく。

n を　2, 3, 5, 7　の素数で素因数分解する。

答えがいくつかあるとき、大きな数を多く使ったものを　１つ　選ぶことにする。
""")

    print("Please input number:")
    n = int(input())

    print(f"Anser:{factorize(n)}")
