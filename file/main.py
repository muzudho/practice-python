
if __name__ == "__main__":

    # ファイルをオープンする
    with open('input.txt', 'r', encoding='utf-8') as f:

        # すべての内容を読み込む
        contents = f.read()

        # コンソール表示
        print(contents)
