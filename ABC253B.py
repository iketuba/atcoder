# 入力を受け取る
H, W = map(int, input().split())
S = [input() for i in range(H)]
print(H, W)
print(S)

# oの位置をリストに保存する
A = []
for h in range(H):
    for w in range(W):
        if S[h][w] == 'o':
            A.append([h, w])       
print(A)

# oの位置の各座標を保存する
h1, w1 = A[0]
h2, w2 = A[1]
print(h1, w1, h2, w2)

# 行の差、列の差を求めて足す
h_diff = abs(h1 - h2)
w_diff = abs(w1 - w2)
ans = h_diff + w_diff
print(ans)