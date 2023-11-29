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

for a in reversed(range(1,101)):

    # n より小さな合成数 7a なら、とりあえず n から、それを引く
    if (7 * a) < n:
        o = n - 7 * a
        print(f"(a {a}) remain:{o}")

        # 余った数で続きをやる

        for b in reversed(range(1,101)):

            if (5 * b) < o:
                p = o - 5 * b
                print(f"(b {b}) remain:{p}")

print(f"Hello,! n:{n}")
