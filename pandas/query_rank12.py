import os
import pandas as pd


def query_rank12():
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

    df2 = df.assign(RANK=df["GENRE_CODE"].rank())
    df3 = df2.groupby('GENRE_CODE').size().rank(
        ascending=False,
        method='first'
    ).astype(int).reset_index(name='RANK')
    df2 = df2.drop("RANK", axis=1)
    df2 = df2.merge(df3, right_index=True, on='GENRE_CODE').sort_index()
    df2 = df2.drop("ID", axis=1)
    df_grouped = df2.groupby("GENRE_CODE").count()
    """
    df_sorted = df_grouped["RANK"].sort_values(ascending=True)
    print(df_sorted.head(1000))
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

    df4 = df.merge(df_grouped, right_index=True, on='GENRE_CODE')
    """
    print(df4.head(1000))
        ID   GENRE_CODE  RANK
    0    1          Red     8
    1    2          Red     8
    6    7          Red     8
    11  12          Red     8
    20  21          Red     8
    36  37          Red     8
    40  41          Red     8
    51  52          Red     8
    2    3         Blue    14
    3    4         Blue    14
    5    6         Blue    14
    7    8         Blue    14
    14  15         Blue    14
    16  17         Blue    14
    21  22         Blue    14
    26  27         Blue    14
    29  30         Blue    14
    32  33         Blue    14
    39  40         Blue    14
    49  50         Blue    14
    55  56         Blue    14
    59  60         Blue    14
    4    5        Green    10
    8    9        Green    10
    9   10        Green    10
    13  14        Green    10
    28  29        Green    10
    35  36        Green    10
    41  42        Green    10
    43  44        Green    10
    52  53        Green    10
    56  57        Green    10
    10  11       Purple     1
    12  13       Violet     2
    54  55       Violet     2
    15  16       Yellow     8
    17  18       Yellow     8
    19  20       Yellow     8
    25  26       Yellow     8
    30  31       Yellow     8
    42  43       Yellow     8
    50  51       Yellow     8
    57  58       Yellow     8
    18  19      SkyBlue     1
    22  23        Black     3
    23  24        Black     3
    45  46        Black     3
    24  25        White     4
    38  39        White     4
    47  48        White     4
    58  59        White     4
    27  28         Pink     2
    33  34         Pink     2
    31  32       Orange     3
    37  38       Orange     3
    53  54       Orange     3
    34  35         Gray     2
    48  49         Gray     2
    44  45  YellowGreen     1
    46  47        Brown     1
    """

    df_sorted = df4.sort_values('RANK', ascending=False)
    """
    print(df_sorted.head(1000))
        ID   GENRE_CODE  RANK
    29  30         Blue    14
    5    6         Blue    14
    55  56         Blue    14
    49  50         Blue    14
    39  40         Blue    14
    32  33         Blue    14
    26  27         Blue    14
    21  22         Blue    14
    16  17         Blue    14
    14  15         Blue    14
    7    8         Blue    14
    3    4         Blue    14
    2    3         Blue    14
    59  60         Blue    14
    4    5        Green    10
    9   10        Green    10
    13  14        Green    10
    8    9        Green    10
    28  29        Green    10
    35  36        Green    10
    41  42        Green    10
    43  44        Green    10
    52  53        Green    10
    56  57        Green    10
    15  16       Yellow     8
    19  20       Yellow     8
    25  26       Yellow     8
    30  31       Yellow     8
    42  43       Yellow     8
    50  51       Yellow     8
    57  58       Yellow     8
    17  18       Yellow     8
    0    1          Red     8
    6    7          Red     8
    1    2          Red     8
    51  52          Red     8
    40  41          Red     8
    36  37          Red     8
    20  21          Red     8
    11  12          Red     8
    58  59        White     4
    47  48        White     4
    38  39        White     4
    24  25        White     4
    53  54       Orange     3
    45  46        Black     3
    23  24        Black     3
    22  23        Black     3
    31  32       Orange     3
    37  38       Orange     3
    34  35         Gray     2
    48  49         Gray     2
    12  13       Violet     2
    33  34         Pink     2
    27  28         Pink     2
    54  55       Violet     2
    18  19      SkyBlue     1
    10  11       Purple     1
    44  45  YellowGreen     1
    46  47        Brown     1
    """

    df_sorted = df_sorted.drop("RANK", axis=1)
    """
    print(df_sorted.values.tolist())
    [[30, 'Blue'], [6, 'Blue'], [56, 'Blue'], [50, 'Blue'], [40, 'Blue'], [33, 'Blue'], [27, 'Blue'], [22, 'Blue'], [17, 'Blue'], [15, 'Blue'], [8, 'Blue'], [4, 'Blue'], [3, 'Blue'], [60, 'Blue'], [5, 'Green'], [10, 'Green'], [14, 'Green'], [9, 'Green'], [29, 'Green'], [36, 'Green'], [42, 'Green'], [44, 'Green'], [53, 'Green'], [57, 'Green'], [16, 'Yellow'], [20, 'Yellow'], [26, 'Yellow'], [31, 'Yellow'], [43, 'Yellow'], [51, 'Yellow'], [58, 'Yellow'], [18, 'Yellow'], [1, 'Red'], [7, 'Red'], [2, 'Red'], [52, 'Red'], [41, 'Red'], [37, 'Red'], [21, 'Red'], [12, 'Red'], [59, 'White'], [48, 'White'], [39, 'White'], [25, 'White'], [54, 'Orange'], [46, 'Black'], [24, 'Black'], [23, 'Black'], [32, 'Orange'], [38, 'Orange'], [35, 'Gray'], [49, 'Gray'], [13, 'Violet'], [34, 'Pink'], [28, 'Pink'], [55, 'Violet'], [19, 'SkyBlue'], [11, 'Purple'], [45, 'YellowGreen'], [47, 'Brown']]
    """

    return df_sorted


# Data frame. (NOT Record set)
df = query_rank12()

for index, row in df.iterrows():
    id = row["ID"]
    genre_code = row["GENRE_CODE"]
    print("Record id:{}, genre_code:{}.".format(id, genre_code))

print("Info    : Finished.")
