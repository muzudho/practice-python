"""
折り返しを除去します。
"""
import re

with open('object-1.txt', mode='r', encoding='utf-8') as f:
    data = f.read()

lines = data.split('\n')

new_data = []

for line in lines:

    if line.startswith('あ　') or line.startswith('ち　') or line.startswith('か　') or line.startswith('４　') or line.startswith('き　') or line.startswith('た　') or line.startswith('み　') or re.match('\w+：　', line):
        # 句読点を除外
        line = line.replace('、　', '　')
        line = line.replace('。　', '　')
        line = line.replace('、', '　')
        line = line.replace('。', '　')

        # 英単語（アスキーコード文字）に挟まれているところ以外で出てくる１つ分の半角スペースを、全角スペース１つに変換
        line = re.sub(r'([^!-~\s]) ([^!-~\s])', r'\1　\2', line)

        buffer = ''
        tokens = line.split('　')
        for token in tokens:
            if len(buffer) == 0:
                # 話者名を強調します Markdown書式
                buffer = f'**{token}**'
            elif len(buffer) + 1 + len(token) <= 54:
                # 行頭に「**文**」の５文字が付いているが、これは１文字幅とカウントしたい（４つ多くカウントする）
                # 全体として５０文字に収めたい
                buffer += '　' + token
            else:
                # 末尾に空白２つ追加
                new_data.append(f'{buffer}  ')
                # ２行目以降
                buffer = '　　' + token

        if buffer != '':
            # 末尾に空白２つ追加
            new_data.append(f'{buffer}  ')
    elif line.startswith('# '):
        new_data.append('')
        new_data.append(line)
        new_data.append('')
    else:
        # 末尾に空白２つ追加
        new_data.append(f'{line}  ')

with open('object-2.txt', mode='w', encoding='utf-8') as f:
    f.write('\n'.join(new_data))
