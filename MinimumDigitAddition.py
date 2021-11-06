t=int(input())

for _ in range(t):
  n = int(input())
  arr = []
  arr = [int(x) for x in str(n)]
  a,b = 0,0
  arr.sort()
  
  for i in range(len(arr)):
    if(i%2 != 0):
      a = a*10 + arr[i]
    else:
      b = b*10 + arr[i]
  print(a+b)
