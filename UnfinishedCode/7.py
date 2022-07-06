'''


By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''

def isPrime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

lastPrime = 0
numOfPrimesFound = 0
i = 1
while numOfPrimesFound < 10001:
    if isPrime(i):
        print(i)
        lastPrime = i
        numOfPrimesFound += 1
    i += 1
print(lastPrime, numOfPrimesFound, i)

# works but too much slow