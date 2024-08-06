if __name__ == "__main__":

    # 読込用にファイルをオープンする
    with open('input.txt', 'r', encoding='utf-8') as f:

        # すべての内容を読み込む
        contents = f.read()

        # \n\n を改行に変換する
        contents = contents.replace(r'\n\n', '\n')

        # コンソール表示
        print(contents)


    # 書出し用にファイルをオープンする
    with open('output.txt', 'w', encoding='utf-8') as f:

        print("writing ...")

        # 内容を書き込む
        f.write(contents)

