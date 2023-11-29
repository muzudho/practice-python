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

        # n より小さな合成数 7a なら、とりあえず n から、それを引く
        if (7 * a) < n:
            o = n - 7 * a
            print(f"(7x{a}) remain:{o}")

            # 割り切れた
            if o == 0:
                return [a]

            # 余った数で続きをやる

            for b in reversed(range(1,101)):

                if (5 * b) < o:
                    p = o - 5 * b
                    print(f"\t(5x{b}) remain:{p}")

                    # 割り切れた
                    if p == 0:
                        return [a, b]

                    # 余った数で続きをやる

                    for c in reversed(range(1,101)):

                        if (3 * c) < p:
                            q = p - 3 * c
                            print(f"\t\t(3x{c}) remain:{q}")

                            # 割り切れた
                            if q == 0:
                                return [a, b, c]

                            # 余った数で続きをやる

                            for d in reversed(range(1,101)):

                                if (2 * d) < q:
                                    r = q - 2 * d
                                    print(f"\t\t\t(2x{d}) remain:{r}")

                                    # 割り切れた
                                    if r == 0:
                                        return [a, b, c, d]

    for b in reversed(range(1,101)):

        if (5 * b) < n:
            p = n - 5 * b
            print(f"(5x{b}) remain:{p}")

            # 割り切れた
            if p == 0:
                return [a, b]

            # 余った数で続きをやる

            for c in reversed(range(1,101)):

                if (3 * c) < p:
                    q = p - 3 * c
                    print(f"\t(3x{c}) remain:{q}")

                    # 割り切れた
                    if q == 0:
                        return [a, b, c]

                    # 余った数で続きをやる

                    for d in reversed(range(1,101)):

                        if (2 * d) < q:
                            r = q - 2 * d
                            print(f"\t\t(2x{d}) remain:{r}")

                            # 割り切れた
                            if r == 0:
                                return [a, b, c, d]

    for c in reversed(range(1,101)):

        if (3 * c) < n:
            q = n - 3 * c
            print(f"(3x{c}) remain:{q}")

            # 割り切れた
            if q == 0:
                return [a, b, c]

            # 余った数で続きをやる

            for d in reversed(range(1,101)):

                if (2 * d) < q:
                    r = q - 2 * d
                    print(f"\t(2x{d}) remain:{r}")

                    # 割り切れた
                    if r == 0:
                        return [a, b, c, d]

    for d in reversed(range(1,101)):

        if (2 * d) < n:
            r = n - 2 * d
            print(f"(2x{d}) remain:{r}")

            # 割り切れた
            if r == 0:
                return [a, b, c, d]

print(f"Anser:{factorize(n)}")
