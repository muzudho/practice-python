import time
import math

test_cases = [("log2", lambda n:math.log2(n)),
              ("√n", lambda n:math.sqrt(n)), ("n", lambda n: n)]

for test_case in test_cases:
    # 単位：秒
    start_time = time.perf_counter()

    # 処理件数
    sum = 0

    # 制限時間（秒）
    t = 1.0

    while True:
        end_time = time.perf_counter()
        erapsed_secs = end_time - start_time
        # print(f"{erapsed_secs:.2f} secs")
        if t < erapsed_secs:
            break

        sum += 1

    print(
        f"{erapsed_secs:.2f} 秒で 性能が {test_case[0]:>4} だと {sum-1}個 処理するので精一杯だぜ（＾ｑ＾）")
