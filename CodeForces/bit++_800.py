t =  int(input())
c = 0
for _ in range(t):
	s = input()[1]
	if(s=='+'):
		c+=1
	else:
		c-=1
print(c)