### 全要素をカウントする ###
l = ['a', 'b', 'c', 'a', 'c', 'a']
print(len(l))

### 各要素の個数をカウントする ###
l = ['a', 'b', 'c', 'a', 'c', 'a']
print(l.count('a'))
print(l.count('b'))
print(l.count('c'))

### 各要素の出現回数を一括で取得したいとき ###
import collections
l = ['a', 'b', 'c', 'a', 'c', 'a']
c = collections.Counter(l)
print(c)