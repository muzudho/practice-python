import os
import pandas as pd

df = pd.read_csv(
    "{}/practice-pandas/data/test-participant.csv".format(os.getcwd()), sep=',', engine='python', verbose=True)

df_grouped = df.groupby("GENRE_CODE").count()
df_sorted = df_grouped["ID"].sort_values(ascending=False)

# Top 1000.
print(df_sorted.head(1000))

"""
GENRE_CODE
Blue           14
Green          10
Yellow          8
Red             8
White           4
Orange          3
Black           3
Violet          2
Pink            2
Gray            2
YellowGreen     1
SkyBlue         1
Purple          1
Brown           1
Name: ID, dtype: int64
"""

print("Info    : Finished.")
