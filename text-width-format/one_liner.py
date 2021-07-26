"""
折り返しを除去します。
"""

with open('input.txt', mode='r', encoding='utf-8') as f:
    data = f.read()

tokens = data.split('\n')

new_data = []
line = ""

for token in tokens:
    # 末尾の半角スペース２つを削ります
    token = token.rstrip()

    if token.startswith('　　'):
        line += f"　{token[2:]}"
    else:
        if line != "":
            new_data.append(line)
        line = token

if line != "":
    new_data.append(line)

with open('object-1.txt', mode='w', encoding='utf-8') as f:
    # f.write(data)
    f.write('\n'.join(new_data))
