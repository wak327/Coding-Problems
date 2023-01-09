a,b = 0,0
for i in range(5): 
	c = input().replace(" ","").find('1')
	if(c>=0):
		a = i
		b = c
print(abs(a-2)+abs(b-2))