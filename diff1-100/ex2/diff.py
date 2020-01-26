"""
Command line arguments:
            "args": [
                "C:/Users/むずでょ/OneDrive/ドキュメント/practice-py/diff1-100/ex2/sample1.txt",
                "C:/Users/むずでょ/OneDrive/ドキュメント/practice-py/diff1-100/ex2/sample2.txt"
            ]
"""

import sys
import os

args = sys.argv

# ファイル読取
file1 = open(args[1], "r")
file2 = open(args[2], "r")

# 行ごとにします
lines1 = file1.readlines()
lines2 = file2.readlines()

# 一行ずつ表示します
for line1 in lines1:
    line1 = line1.rstrip(os.linesep)
    print(line1)

for line2 in lines2:
    line2 = line2.rstrip(os.linesep)
    print(line2)

# ファイルをクローズします
file1.close()
file2.close()
