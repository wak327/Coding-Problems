str1 = input()
str1 = str1.lower()
str1 = str1.translate({ord(i): None for i in 'aoyeui'})
print('.'+'.'.join(list(str1)))