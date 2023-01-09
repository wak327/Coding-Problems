from math import ceil
n,m,a = input().split()
n,m,a = int(n),int(m),int(a)
k,j = ceil(n/a), ceil(m/a)
print(k*j)