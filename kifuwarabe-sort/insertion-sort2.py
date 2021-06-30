# MIT教科書 挿入ソート

# 添え字は 1 から使用
A = [' ', 'E', 'D', 'C', 'B', 'A']

# Start
print(f"(S) {A}")

for j in range(2, len(A)):
    key = A[j]
    # A[j]をソート済みの列 A[1..j-1]に挿入する
    i = j-1
    while i > 0 and A[i] > key:
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key
    print(f"({j}) {A}")
