# python 3 solution not accepted in python 2
t = int(input())
for i in range(t):
	str1 = input()
	len1 = len(str1)
	if len1 <= 10:
		print(str1)
	else:
		print(f"{str1[0]}{len1-2}{str1[len1-1]}")