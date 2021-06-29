import time
import math

# log2 は 終わらない（＾～＾）
# ("log2", lambda n:math.log2(n)),
test_cases = [
    ("√n", lambda n:math.sqrt(n)), ("n", lambda n: n)]

# 制限時間（単位：秒）
time_required_list = [1.0]

for test_case in test_cases:
    for time_required in time_required_list:
        # 処理件数
        n = 1  # 0 開始は無理（＾～＾）

        # 制限時間（秒）
        t = 1.0

        while True:
            if t < (test_case[1](n))/1_000_000:
                break

            n += 1

        print(
            f"{time_required} 秒で 1,000,000個処理できるマシンの性能が {test_case[0]:>4} になると {n-1}個 処理するので精一杯だぜ（＾ｑ＾）")
