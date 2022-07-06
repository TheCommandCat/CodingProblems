'''


215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

'''


x = 0
num = str(2 ** 1000)
for i in range(len(num)):
    x += int(num[i])
print(x)

