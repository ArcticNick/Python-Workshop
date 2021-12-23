"""
The prime factors of 13195 are 5,7,13, and 29
What is the largest prime factor of a given number N?
Recall: prime number are natural numbers that is a factor of 1 and itself
"""
from math import sqrt
n = int(input("Enter value to find its largest prime factor:  "))

def largest_prime_factors(n): # function that lists all prime numbers from 1 to n
    start = 0
    prime_list = [1]
    prime_factors = []
    for i in range(start, n + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                prime_list.append(i)

    for num in prime_list:
        if n % num == 0 and num < n + 1:
            prime_factors.append(num)
    print(max(prime_factors))

largest_prime_factors(n)