import re

# ファイルをオープンする
file = open("animator-director/web-site.txt", "r", encoding="utf-8")

# すべての内容を読み込む
contents = file.read()

# HTMLタグを半角スペースに変換。
contents = re.sub(r"<[^>]*?>", " ", contents)

# ２つ以上連続する半角スペースを、改行に変換。
contents = re.sub(r" {2,}", "\n", contents)

# 内容を表示する
print(contents)

# ファイルをクローズする
file.close()
