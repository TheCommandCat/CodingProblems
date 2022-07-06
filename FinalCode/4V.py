'''


A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''
import time
import timeit


def qustion():
    answer = 0
    factor1 = 0
    factor2 = 0
    num = 0
    for i in range(999, 100, -1):
        for x in range(999, i - 1, -1):
            num = i * x

            if num > answer and str(num) == str(num)[::-1]:
                answer, factor1, factor2 = num, i, x

    return f'answer: {answer}, factors: {factor1}, {factor2}'


# create a list with x,i and num and short by num
print(timeit.timeit(qustion, number=300) / 300)
