# 素因数分解の練習
#
# cd math/prime_factorization
# python step3_0.py

import time
#from step1 import factorize
#from step1_1_0 import factorize
from step1_1_1_0 import factorize
#from step1_2_0 import factorize


start = time.time()
n = 1

for i in range(0,1001):
    # 答えが出るまで繰り返す
    while True:
        answer = factorize(n, debug=False)

        if answer is not None:
            print(f"({i}) n={n} Answer={answer}")

        n += 1

        if answer is not None:
            break

end = time.time()
print(f"Time: {end-start} seconds")
