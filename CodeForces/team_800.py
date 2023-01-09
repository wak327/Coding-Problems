# python 3 solution not accepted in python 2
def okayS(str1):
	c = 0
	for i in str1:
		if(i == '1'):
			c+=1
		if(c>1):
			return True
	return False
t = int(input())
c = 0
for i in range(t):
	str1 = input()
	if okayS(str1):
		c+=1
print(c)