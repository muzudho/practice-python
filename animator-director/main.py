import urllib
import pandas as pd

animator_df = pd.read_csv("./animator-director/animator.csv")
names = animator_df["NAME"].values.tolist()

print("""
|Name|Ansa|Nico|
|----|----|----|""")

for name in names:
    # Deletes space.
    keyword = name.replace(" ", "")
    # Escape.
    keyword = urllib.parse.quote(keyword)
    print(
        "|{0}|[Ansa](https://ansaikuropedia.org/index.php?search={1})|[Nico](https://dic.nicovideo.jp/s/al/t/{1})|".format(name, keyword))
