# 素因数分解の練習
#
# cd math
# python prime_factorization.py

print("""\
ある正の整数 n があるとする。
とりあえず n は 1～100 ぐらいを考えておく。

n を　2, 3, 5, 7　の素数で素因数分解する。

答えがいくつかあるとき、大きな数を多く使ったものを　１つ　選ぶことにする。
""")

print("Please input number:")
n = int(input())

def factorize(n):

    for a in reversed(range(1,101)):
        aa = 7 * a

        # n より小さな合成数 7a なら、とりあえず n から、それを引く
        if aa < n:
            o = n - aa
            print(f"(7x{a}) remain:{o}")

            # 割り切れた
            if o == 0:
                return [a]

            # 余った数で続きをやる

            for b in reversed(range(1,101)):
                bb = aa * 5 * b

                if bb < o:
                    p = o - bb
                    print(f"\t(5x{b}) remain:{p}")

                    # 割り切れた
                    if p == 0:
                        return [a, b]

                    # 余った数で続きをやる

                    for c in reversed(range(1,101)):
                        cc = bb * 3 * c

                        if cc < p:
                            q = p - cc
                            print(f"\t\t(3x{c}) remain:{q}")

                            # 割り切れた
                            if q == 0:
                                return [a, b, c]

                            # 余った数で続きをやる

                            for d in reversed(range(1,101)):
                                dd = cc * 2 * d

                                if dd < q:
                                    r = q - dd
                                    print(f"\t\t\t(2x{d}) remain:{r}")

                                    # 割り切れた
                                    if r == 0:
                                        return [a, b, c, d]

    for b in reversed(range(1,101)):
        bb = 5 * b

        if bb < n:
            p = n - bb
            print(f"(5x{b}) remain:{p}")

            # 割り切れた
            if p == 0:
                return [a, b]

            # 余った数で続きをやる

            for c in reversed(range(1,101)):
                cc = bb * 3 * c

                if cc < p:
                    q = p - cc
                    print(f"\t(3x{c}) remain:{q}")

                    # 割り切れた
                    if q == 0:
                        return [a, b, c]

                    # 余った数で続きをやる

                    for d in reversed(range(1,101)):
                        dd = cc * 2 * d

                        if dd < q:
                            r = q - dd
                            print(f"\t\t(2x{d}) remain:{r}")

                            # 割り切れた
                            if r == 0:
                                return [a, b, c, d]

    for c in reversed(range(1,101)):
        cc = 3 * c

        if cc < n:
            q = n - cc
            print(f"(3x{c}) remain:{q}")

            # 割り切れた
            if q == 0:
                return [a, b, c]

            # 余った数で続きをやる

            for d in reversed(range(1,101)):
                dd = cc * 2 * d

                if dd < q:
                    r = q - 2 * d
                    print(f"\t(2x{d}) remain:{r}")

                    # 割り切れた
                    if r == 0:
                        return [a, b, c, d]

    for d in reversed(range(1,101)):
        dd = 2 * d

        if dd < n:
            r = n - dd
            print(f"(2x{d}) remain:{r}")

            # 割り切れた
            if r == 0:
                return [a, b, c, d]

print(f"Anser:{factorize(n)}")
