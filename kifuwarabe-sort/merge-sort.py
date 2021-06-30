# [マージソート](https://ja.wikipedia.org/wiki/%E3%83%9E%E3%83%BC%E3%82%B8%E3%82%BD%E3%83%BC%E3%83%88)


def merge(A, B, left, mid, right):
    """
    A : str[int]
    B : str[int]
        ソート済み配列
    left : int
    mid : int
    right : int
    """
    i = left
    j = mid

    # ソート済み配列の添え字
    k = 0
    # l

    # i が 真ん中より下で、 j が　右端より左
    while i < mid and j < right:
        # i側の方が小さい（か等しい）なら
        if A[i] <= A[j]:
            # i側の方をソート済みの方へ移す
            B[k] = A[i]
            i += 1
            k += 1
        else:
            # j側の方をソート済みの方へ移す
            B[k] = A[j]
            j += 1
            k += 1

    if i == mid:  # i側のAをBに移動し尽くしたので、j側も順番にBに入れていく
        while j < right:
            B[k] = A[j]
            j += 1
            k += 1
    else:
        while i < mid:  # j側のAをBに移動し尽くしたので、i側も順番にBに入れていく
            B[k] = A[i]
            i += 1
            k += 1

    for l in range(0, k):
        A[left + l] = B[l]


def merge_sort(A, B, left, right):
    """
    A: str[int]
    B: str[int]
    left: int
    right: int
    """

    print(f"left={left} right={right}")

    # int mid
    if left == right or left == right - 1:  # 等しいか、１つ追い抜くか
        return

    # 真ん中
    mid = (left + right) // 2  # 小数点以下切り捨て（＾～＾）
    merge_sort(A, B, left, mid)
    merge_sort(A, B, mid, right)
    merge(A, B, left, mid, right)


def main():
    a = ['J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
    b = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # とりあえず配列のサイズを確保しとく

    n = 10  # 定数
    merge_sort(a, b, 0, n)
    for i in range(0, n):
        print(f"{a[i]} ", end='')

    print("")  # New line


main()
