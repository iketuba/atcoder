num = list(map(int, input().split()))
b = num[1]
m = sorted(num)[1]
if b == m:
    print('Yes')
else:
    print('No')