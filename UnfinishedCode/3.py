'''


The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

def isPrime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primeFactors(n):
    primefactors = []
    for i in range(1, n):
        print(i)
        if n % i == 0 and isPrime(i):
            primefactors.append(i)
    return primefactors

print(primeFactors(600851475143))

# answer: 6857

# works but too much slow