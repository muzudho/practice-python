import os
import glob

# ディレクトリーを選んでください
print("""Which directory?
Example: .""")

path = input()
os.chdir(path)

# フィル名を一覧します
print(f"""Current directory: {os.getcwd()}

Files
-----""")

files = glob.glob("./*")
for file in files:
    print(file)
