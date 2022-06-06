N = int(input())
A = list(map(int, input().split()))

# 終了判定用のフラグ
flag = 0
# 2で割り切れた回数
count = 0

while True:
    for i in range(N):
        if A[i] % 2 != 0:
            flag = 1
    if flag == 1:
        break

    for i in range(N):
        A[i] = A[i] / 2
    count += 1

print(count)