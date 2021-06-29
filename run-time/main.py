import time
import math

test_cases = [("√n", lambda n:math.sqrt(n)), ("n", lambda n: n)]

for test_case in test_cases:
    # 単位：秒
    start_time = time.perf_counter()

    # 処理件数
    sum = 0

    while True:
        end_time = time.perf_counter()
        erapsed_secs = end_time - start_time
        # print(f"{erapsed_secs:.2f} secs")
        if 1.0 <= erapsed_secs:
            break

        sum += 1

    print(f"{erapsed_secs:.2f} secs : {test_case[0]:>2} : {sum} loops")
