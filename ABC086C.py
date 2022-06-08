N = int(input())

t_before = 0
x_before = 0
y_before = 0
flag = 1

for _ in range(N):
    t, x, y = map(int, input().split())
    time = t - t_before
    distance = abs(x-x_before) + abs(y-y_before)

    if time < distance:
        flag = 0
    elif time % 2 != distance % 2:
        flag = 0
    if flag == 0:
        break

    t_before = t
    x_before = x
    y_before = y

if flag:
    print('Yes')
else:
    print('No')    
