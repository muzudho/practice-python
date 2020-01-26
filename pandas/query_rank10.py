import os
import pandas as pd

# UTF-8
df = pd.read_csv(
    "{}/practice-pandas/data/test-participant.csv".format(os.getcwd()), sep=',', engine='python')
"""
print(df.head(1000))
    ID   GENRE_CODE
0    1          Red
1    2          Red
2    3         Blue
3    4         Blue
4    5        Green
5    6         Blue
6    7          Red
7    8         Blue
8    9        Green
9   10        Green
10  11       Purple
11  12          Red
12  13       Violet
13  14        Green
14  15         Blue
15  16       Yellow
16  17         Blue
17  18       Yellow
18  19      SkyBlue
19  20       Yellow
20  21          Red
21  22         Blue
22  23        Black
23  24        Black
24  25        White
25  26       Yellow
26  27         Blue
27  28         Pink
28  29        Green
29  30         Blue
30  31       Yellow
31  32       Orange
32  33         Blue
33  34         Pink
34  35         Gray
35  36        Green
36  37          Red
37  38       Orange
38  39        White
39  40         Blue
40  41          Red
41  42        Green
42  43       Yellow
43  44        Green
44  45  YellowGreen
45  46        Black
46  47        Brown
47  48        White
48  49         Gray
49  50         Blue
50  51       Yellow
51  52          Red
52  53        Green
53  54       Orange
54  55       Violet
55  56         Blue
56  57        Green
57  58       Yellow
58  59        White
59  60         Blue
"""

# Add column.
df2 = df.assign(RANK=df["GENRE_CODE"].rank())
"""
print(df2.head(1000))
    ID   GENRE_CODE  RANK
0    1          Red  40.5
1    2          Red  40.5
2    3         Blue  10.5
3    4         Blue  10.5
4    5        Green  25.5
5    6         Blue  10.5
6    7          Red  40.5
7    8         Blue  10.5
8    9        Green  25.5
9   10        Green  25.5
10  11       Purple  36.0
11  12          Red  40.5
12  13       Violet  46.5
13  14        Green  25.5
14  15         Blue  10.5
15  16       Yellow  55.5
16  17         Blue  10.5
17  18       Yellow  55.5
18  19      SkyBlue  45.0
19  20       Yellow  55.5
20  21          Red  40.5
21  22         Blue  10.5
22  23        Black   2.0
23  24        Black   2.0
24  25        White  49.5
25  26       Yellow  55.5
26  27         Blue  10.5
27  28         Pink  34.5
28  29        Green  25.5
29  30         Blue  10.5
30  31       Yellow  55.5
31  32       Orange  32.0
32  33         Blue  10.5
33  34         Pink  34.5
34  35         Gray  19.5
35  36        Green  25.5
36  37          Red  40.5
37  38       Orange  32.0
38  39        White  49.5
39  40         Blue  10.5
40  41          Red  40.5
41  42        Green  25.5
42  43       Yellow  55.5
43  44        Green  25.5
44  45  YellowGreen  60.0
45  46        Black   2.0
46  47        Brown  18.0
47  48        White  49.5
48  49         Gray  19.5
49  50         Blue  10.5
50  51       Yellow  55.5
51  52          Red  40.5
52  53        Green  25.5
53  54       Orange  32.0
54  55       Violet  46.5
55  56         Blue  10.5
56  57        Green  25.5
57  58       Yellow  55.5
58  59        White  49.5
59  60         Blue  10.5
"""

df3 = df2.groupby('GENRE_CODE').size().rank(
    ascending=False,
    method='first'
).astype(int).reset_index(name='RANK')
# print(df3.head(1000))

"""
     GENRE_CODE  RANK
0         Black     6
1          Blue     1
2         Brown    11
3          Gray     8
4         Green     2
5        Orange     7
6          Pink     9
7        Purple    12
8           Red     3
9       SkyBlue    13
10       Violet    10
11        White     5
12       Yellow     4
13  YellowGreen    14
"""

df2 = df2.drop("RANK", axis=1)

df2 = df2.merge(df3, right_index=True, on='GENRE_CODE').sort_index()
# print(df2.head(1000))

"""
      ID  GENRE_CODE  RANK
0    1.0        40.5     3
1    2.0        40.5     3
2    3.0        10.5     1
3    4.0        10.5     1
4    5.0        25.5     2
5    6.0        10.5     1
6    7.0        40.5     3
7    8.0        10.5     1
8    9.0        25.5     2
9   10.0        25.5     2
10  11.0        36.0    12
11  12.0        40.5     3
12  13.0        46.5    10
13  14.0        25.5     2
14  15.0        10.5     1
15  16.0        55.5     4
16  17.0        10.5     1
17  18.0        55.5     4
18  19.0        45.0    13
19  20.0        55.5     4
20  21.0        40.5     3
21  22.0        10.5     1
22  23.0         2.0     6
23  24.0         2.0     6
24  25.0        49.5     5
25  26.0        55.5     4
26  27.0        10.5     1
27  28.0        34.5     9
28  29.0        25.5     2
29  30.0        10.5     1
30  31.0        55.5     4
31  32.0        32.0     7
32  33.0        10.5     1
33  34.0        34.5     9
34  35.0        19.5     8
35  36.0        25.5     2
36  37.0        40.5     3
37  38.0        32.0     7
38  39.0        49.5     5
39  40.0        10.5     1
40  41.0        40.5     3
41  42.0        25.5     2
42  43.0        55.5     4
43  44.0        25.5     2
44  45.0        60.0    14
45  46.0         2.0     6
46  47.0        18.0    11
47  48.0        49.5     5
48  49.0        19.5     8
49  50.0        10.5     1
50  51.0        55.5     4
51  52.0        40.5     3
52  53.0        25.5     2
53  54.0        32.0     7
54  55.0        46.5    10
55  56.0        10.5     1
56  57.0        25.5     2
57  58.0        55.5     4
58  59.0        49.5     5
59  60.0        10.5     1
"""

df2 = df2.drop("ID", axis=1)
# print(df2.head(1000))

df_grouped = df2.groupby("GENRE_CODE").count()
"""
print(df_grouped.head(1000))
             RANK
GENRE_CODE
Black           3
Blue           14
Brown           1
Gray            2
Green          10
Orange          3
Pink            2
Purple          1
Red             8
SkyBlue         1
Violet          2
White           4
Yellow          8
YellowGreen     1
"""

df_sorted = df_grouped["RANK"].sort_values(ascending=True)
print(df_sorted.head(1000))
"""
GENRE_CODE
Brown           1
Purple          1
SkyBlue         1
YellowGreen     1
Gray            2
Pink            2
Violet          2
Black           3
Orange          3
White           4
Red             8
Yellow          8
Green          10
Blue           14
Name: RANK, dtype: int64
"""

print("Info    : Finished.")
