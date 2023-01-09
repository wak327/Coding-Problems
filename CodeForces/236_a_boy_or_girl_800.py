set1 = {''}
str1 = input()
for i in str1:
	set1.add(i)
len1 = len(set1)
if len1 % 2:
	print("CHAT WITH HER!")
else:
	print("IGNORE HIM!")