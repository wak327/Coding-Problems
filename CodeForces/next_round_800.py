n, m = input().split()
arr = input().split()
c = 0
for i in arr:
	if(int(i)>=int(arr[int(m)-1]) and int(i) != 0):
		c+=1
print(c)