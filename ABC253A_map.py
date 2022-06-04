lis = [-3, 2, -10]
print(map(abs, lis))
# <map object at 0x000001F1C2E64E50>

print(type(map(abs, lis)))
# <class 'map'>

for i in map(abs, lis):
    print(i)
# 3 
# 2 
# 10

print(list(map(abs, lis)))
# [3, 2, 10]