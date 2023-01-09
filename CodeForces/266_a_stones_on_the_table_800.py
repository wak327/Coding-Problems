str1 = input()
str1 = input()
len1 = len(str1)
c=0
for i in range(len1-1):
	if str1[i]==str1[i+1]:
		c+=1
print(c)