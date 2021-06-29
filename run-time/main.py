import time

start_time = time.perf_counter()


names = ["n"]
functions = [lambda n: n]


n = 0

while True:
    if functions[0](n)/1_000_000 > 1:
        break
    n += 1

end_time = time.perf_counter()

# 経過時間(ナノ秒)
erapsed = end_time - start_time
print(f"{names[0]} : {erapsed} ns")
