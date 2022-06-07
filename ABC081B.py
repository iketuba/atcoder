N = int(input())
A = list(map(int, input().split()))

flag = 1
count = 0
while True:
    for i in range(N):
        if A[i] % 2 != 0:
            flag = 0
    if flag == 0:
        break

    for i in range(N):
        A[i] /= 2
    count += 1

print(count)