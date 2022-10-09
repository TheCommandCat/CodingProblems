'''

The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

x = 0
y = 0
for i in range(1, 101):
    x += i ** 2
    y += i
print(y ** 2 - x)
