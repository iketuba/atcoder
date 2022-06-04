### sortとsortedの違い ###

# sort: 元のリスト自体が書き換えられる破壊的処理
old = [20, 40, 30, 50, 10]
old.sort()
print(old)

# sorted: 元のリストは変更されない非破壊的処理
old = [20, 40, 30, 50, 10]
new = sorted(old, reverse=True)
print(old)
print(new)