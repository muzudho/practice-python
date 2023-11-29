# 素因数分解の練習
#
# cd math/prime_factorization
# python step2_0.py

from step1_0 import factorize

for n in range(1,101):
    print(f"N={n} Answer={factorize(n, debug=False)}")
