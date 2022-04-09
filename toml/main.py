import pytomlpp

with open('example.toml', mode='r', encoding='utf-8') as f:
    text = f.read()

# print(text)

# ここに Toml の処理を書く
print("Tomlの読込")
doc = pytomlpp.loads(text)

print(f"ip は {doc['servers']['alpha']['ip']}")

# pytomlpp.dumps({"你好": "world"})
