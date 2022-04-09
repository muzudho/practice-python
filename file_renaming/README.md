# file-renaming

TODO 指定したディレクトリーにあるファイル名を正規表現で変更  

# Run

```shell
cd file_renaming

python main.py
```

# 使用例１

例えばファイル名を以下のように整形したい。  

```plaintext
整形前
201611071744_一手詰め.png

整形後
20161107-1744__doubutsu-shogi__一手詰め.png
```

正規表現は以下のようになる。  

```
整形前
^(\d{8})(\d{4})_([\d\w]+).png$

整形後
\1-\2__doubutsu-shogi__\3.png
```

# 使用例２

例えばファイル名を以下のように整形したい。  

```plaintext
整形前
201611072256.png
201611072256b.png

整形後
20161107-2256__doubutsu-shogi__.png
20161107-2256__doubutsu-shogi__b.png
```

正規表現は以下のようになる。  

```
整形前
^(\d{8})(\d{4})([\d\w]*).png$

整形後
\1-\2__doubutsu-shogi__\3.png
```
