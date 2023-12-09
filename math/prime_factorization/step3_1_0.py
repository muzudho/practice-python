# 素因数分解の練習
#
# cd math/prime_factorization
# python step3_1_0.py

import time
#from step1 import factorize
#from step1_1_0 import factorize
from step1_1_1_0 import factorize # これが高速
#from step1_2_0 import factorize

print("Start")

start = time.time()

#with open('data_time.txt', mode='w') as f_t:
with open('data_time.txt', mode='a') as f_t:
    #with open('data.txt', mode='w') as f:
    with open('data.txt', mode='a') as f:

        f.write("""\
     i,          n,    7,    5,    3,    2
------, ----------, ----, ----, ----, ----
""")

        #n = 1
        n = 53343361
        #for i in range(0,1000001):
        for i in range(3038,1000001):
            # 答えが出るまで繰り返す
            while True:
                answer = factorize(n, debug=False)

                if answer is not None:
                    f.write(f"{i:6}, {n:10}, {answer[0]:4}, {answer[1]:4}, {answer[2]:4}, {answer[3]:4}\n")

                n += 1

                if answer is not None:
                    break

            # 100件ごとにタイムを入れる
            if i % 100 == 0:
                end = time.time()
                f_t.write(f"# (i={i}) Time: {end-start} seconds\n")
                f_t.flush()     # バッファーが溜まると書き出されるが、とりあえず毎回書きだす

        end = time.time()
        f_t.write(f"# (Finished) Time: {end-start} seconds\n")

print("Finished")
