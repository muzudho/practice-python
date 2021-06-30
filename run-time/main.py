import math

# log2 は 終わらない（＾～＾）
# ("log2 n", lambda n:math.log2(n)),
# sqrt も終わらない（＾～＾）
# ("√n", lambda n:math.sqrt(n)),
test_cases = [
    ("n", lambda n: n),
    ("n log2 n", lambda n:n*math.log2(n)),
    ("n^2", lambda n:n**2),
    ("n^3", lambda n:n**3),
    ("2^n", lambda n:2**n),
    ("n!", lambda n:math.factorial(n))]

# 制限時間（単位：秒）
time_required_list = [1.0]

for test_case in test_cases:
    for t in time_required_list:
        # 処理件数
        n = 1  # 0 開始は無理（＾～＾）

        while True:
            if t < (test_case[1](n))/1_000_000:
                break

            n += 1

        print(
            f"{t} 秒で 1,000,000個処理できるマシンの性能が {test_case[0]:>8} になると、{t} 秒では {n-1:>7}個 処理するので精一杯だぜ（＾ｑ＾）")
