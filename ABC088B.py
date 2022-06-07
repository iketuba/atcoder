N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

alice = sum(a[0::2])
bob = sum(a[1::2])
print(alice - bob)