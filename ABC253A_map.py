l = [-3, 2, -10]
print(map(abs, l))
# <map object at 0x000001F1C2E64E50>

print(type(map(abs, l)))
# <class 'map'>

for i in map(abs, l):
    print(i)
# 3 
# 2 
# 10

print(list(map(abs, l)))
# [3, 2, 10]