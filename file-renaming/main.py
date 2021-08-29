import os
import glob
import re

# ディレクトリーを選んでください
print("""Which directory?
Example: .""")
# C:\muzudho\picture\2021-08-pg

path = input()
os.chdir(path)

# フィル名を一覧します
print(f"""Current directory: {os.getcwd()}

Files
-----""")

files = glob.glob("./*")
for file in files:
    # `file` - Example: `.\20210815shogi67.png`
    basename = os.path.basename(file)
    print(basename)

# 正規表現のパターンを入力してください

print(r"""
Please enter a regular expression pattern.
Example: ^example-([\d\w]+)-([\d\w]+).txt$""")
# ^(.+)shogi(.+)$

patternText = input()
pattern = re.compile(patternText)

print(r"""
Enter the pattern after the conversion.
Example: example-\2-\1.txt""")

replacement = input()

print("""
Simulation
----------""")
for file in files:
    basename = os.path.basename(file)
    result = pattern.match(basename)
    if result:
        # Matched
        converted = re.sub(patternText, replacement, basename)
        print(f"[x] {basename} --> {converted}")
    else:
        # Unmatched
        print(f"[ ] {file}")

print("""
Do you want to run it (y)?""")

answer = input()

if answer == "y":
    for file in files:
        basename = os.path.basename(file)
        result = pattern.match(basename)
        if result:
            # Matched
            converted = re.sub(patternText, replacement, basename)
            oldPath = os.path.join(os.getcwd(), basename)
            newPath = os.path.join(os.getcwd(), converted)
            os.rename(oldPath, newPath)
            print(f"Renamed {oldPath} --> {newPath}")
else:
    print("Canceld")
