### 標準入力 ###
a = input() # 入力: あ
print(a) # 出力: あ

b = int(input()) # 入力: 3
print(b) # 出力: 3 

c = input().split() # 入力: a b c
print(c) # 出力: ['a', 'b', 'c']

d = list(map(int, input().split())) # 入力: 1 2 3
print(d) # 出力: [1, 2, 3]
print(d[0]) # 出力: 1
print(d[2]) # 出力: 3

e = [input() for i in range(3)]
# 入力: 
# あ 
# い
# う
print(e) 
# 出力: ['あ', 'い', 'う']

f = [int(input()) for i in range(3)]
# 入力:
# 1
# 2
# 3
print(f)
# 出力: [1, 2, 3]