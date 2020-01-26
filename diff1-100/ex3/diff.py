"""
Command line arguments:
            "args": [
                "./sample1.txt",
                "./sample2.txt"
            ]
"""

import sys
import os

print("Info    | Current directory: {}".format(os.getcwd()))

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Info    | Current directory: {}".format(os.getcwd()))

args = sys.argv

# ファイル読取
file1 = open(args[1], "r")
file2 = open(args[2], "r")

# 行ごとにします
lines1 = file1.readlines()
lines2 = file2.readlines()

# セット作成
set1 = set()
set2 = set()

# 一行ずつセットに追加
for line1 in lines1:
    line1 = line1.rstrip(os.linesep)
    set1.add(line1)

for line2 in lines2:
    line2 = line2.rstrip(os.linesep)
    set2.add(line2)

# 一要素ずつ表示します
for element1 in set1:
    element1 = element1.rstrip(os.linesep)
    print("Set1: {}".format(element1))

for element2 in set2:
    element2 = element2.rstrip(os.linesep)
    print("Set2: {}".format(element2))

# ファイルをクローズします
file1.close()
file2.close()
