with open('input.txt', mode='r', encoding='utf-8') as f:
    data = f.read()

tokens = data.split('\n')

new_data = []

for token in tokens:
    # 末尾の半角スペース２つを削ります
    token = token.rstrip()

    row = 0
    column = 0

    # 全角スペース区切りで分割します
    phrases = token.split('　')
    for phrase in phrases:

        size = len(phrase)

        # 最初の１回の折り返し
        if row == 0 and 54 <= size:
            new_data.append(f" 54 {phrase[0:54]}  ")
            phrase = phrase[54:]
            size -= 54
            column += 54

            if 54 <= column:
                row += 1
                column -= 54

        # 2回目以降の折り返し
        while 52 <= size:
            new_data.append(f" 52 　　{phrase[0:52]}  ")
            phrase = phrase[52:]
            size -= 52
            column += 52

            if 52 <= column:
                row += 1
                column -= 52

        if size == 0:
            new_data.append(f"  0")
        else:
            if 1 <= row:
                new_data.append(f"{size:3} 　　{token}  ")
            else:
                new_data.append(f"{size:3} {token}  ")

with open('output.txt', mode='w', encoding='utf-8') as f:
    # f.write(data)
    f.write('\n'.join(new_data))
