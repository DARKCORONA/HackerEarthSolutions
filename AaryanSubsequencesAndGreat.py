n = int(input())

a = list(map(int,input().strip().split()))

v = 0
for i in range(n):
    v = v | a[i]
print(v)
