"""
折り返しを除去します。
"""

with open('object-1.txt', mode='r', encoding='utf-8') as f:
    data = f.read()

lines = data.split('\n')

new_data = []

for line in lines:

    if line.startswith('あ　') or line.startswith('ち　') or line.startswith('か　') or line.startswith('４　') or line.startswith('き　') or line.startswith('た　') or line.startswith('み　'):
        buffer = ''
        tokens = line.split('　')
        for token in tokens:
            if len(buffer) == 0:
                buffer = token
            elif len(buffer) + 1 + len(token) <= 52:
                buffer += '　' + token
            else:
                # ２行目以降
                new_data.append(buffer)
                buffer = '　　' + token

        if buffer != '':
            new_data.append(buffer)
    else:
        new_data.append(line)

with open('object-2.txt', mode='w', encoding='utf-8') as f:
    f.write('\n'.join(new_data))
