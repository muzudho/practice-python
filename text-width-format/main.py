with open('input.txt', mode='r', encoding='utf-8') as f:
    data = f.read()

tokens = data.split('\n')

new_data = []

for token in tokens:
    size = len(token)

    wrap = 0

    # 最初の１回の折り返し
    if 54 <= size:
        new_data.append(f" 54 {token[0:54]}")
        token = token[54:]
        size -= 54
        wrap += 1

    # 2回目以降の折り返し
    while 52 <= size:
        new_data.append(f" 52 　　{token[0:52]}")
        token = token[52:]
        size -= 52
        wrap += 1

    if 1 <= wrap:
        new_data.append(f"{size:3} 　　{token}")
    else:
        new_data.append(f"{size:3} {token}")

with open('output.txt', mode='w', encoding='utf-8') as f:
    # f.write(data)
    f.write('\n'.join(new_data))
