import os
import glob
import re

# ディレクトリーを選んでください
while True:
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

    # とりあえず一覧します
    for file in files:
        # `file` - Example: `.\20210815shogi67.png`
        basename = os.path.basename(file)
        print(basename)

    print("""
Are you sure this is the right directory (y/n)?""")

    answer = input()

    if answer == "y":
        break

# 正規表現のパターンを入力してください
while True:
    print(r"""
Please enter a regular expression pattern.
Example: ^example-([\d\w]+)-([\d\w]+).txt$""")
    # ^(.+)shogi(.+)$

    patternText = input()
    pattern = re.compile(patternText)

    # とりあえず一覧します
    for i, file in enumerate(files):
        basename = os.path.basename(file)
        result = pattern.match(basename)
        if result:
            # Matched
            # グループ数
            groupCount = len(result.groups())
            buf = f"({i+1}) {basename}"
            for j in range(0, groupCount):
                buf += f" \\{j+1}=[{result.group(j+1)}]"
            print(buf)
        else:
            # Unmatched
            print(f"[ ] {basename}")

    print("""
Was there a match (y/n)?""")

    answer = input()

    if answer == "y":
        break

print(r"""
Enter the pattern after the conversion.
Example: example-\2-\1.txt""")
# \2pg\1

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
Do you want to run it (y/n)?""")

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
