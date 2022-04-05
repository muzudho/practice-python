import random
import math

# 乱数
rnd = random.SystemRandom()

area = 4
# area = 9
# area = 4*4
# area = 5*5
# area = 6*6
# area = 19 * 19  # 囲碁の19路盤を想定
# area = 100 * 100  # でかいケース
# area = 200 * 200  # でかいケース
# area = 400 * 400  # でかいケース
# area = 600 * 600  # でかいケース
# area = 800 * 800  # でかいケース
# area = 1600 * 1600  # でかいケース
# area = 10000 * 10000  # でかいケース
boxes = [0] * area

# 試行回数
# trial = math.ceil(area * math.e)  # (981) 全ての箱が埋まるわけではない
# trial = math.ceil(area * 7)  # 全ての箱が埋まるわけではない
# trial = math.ceil(area * 7.1)  # 全ての箱が埋まるわけではない
# trial = math.ceil(area * 7.2)  # (2599) 全ての箱が埋まるわけではない
# trial = math.ceil(area * math.e ** 2)  # (2667) 全ての箱が埋まることがある
# trial = math.ceil(area * 8)
# trial = math.ceil(area * math.pi ** 2)  # pi ^ 2 = 9.87
# trial = math.ceil(area * 16)
# 2 * pi * e = 17.08 # 1600x1600 なら埋まる
trial = math.ceil(area * 2 * math.pi * math.e)

print("lottery start!")

for i in range(0, trial):
    lottery = rnd.randrange(0, area)
    boxes[lottery] += 1

count_of_zero = 0
count_of_one = 0
count_of_two = 0
count_of_three = 0
count_of_four = 0
print("""+
| Distribution 
+
""")
for i, v in enumerate(boxes):
    if v == 0:
        count_of_zero += 1
    elif v == 1:
        count_of_one += 1
    elif v == 2:
        count_of_two += 1
    elif v == 3:
        count_of_three += 1
    elif v == 4:
        count_of_four += 1

    # print("[{}] {}".format(i, v))

print(f"Trial         = {trial}")
print(f"Count of zero = {count_of_zero} / {area}")
print(f"Count of one  = {count_of_one} / {area}")
print(f"Count of two  = {count_of_two} / {area}")
print(f"Count of three= {count_of_three} / {area}")
print(f"Count of four = {count_of_four} / {area}")
print(f"boxes=[{boxes}]")
