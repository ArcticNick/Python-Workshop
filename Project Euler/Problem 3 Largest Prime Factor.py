"""
The prime factors of 13195 are 5,7,13, and 29
What is the largest prime factor of a given number N? N = 600851475143 from ProjectEuler.net
"""
from math import sqrt
n = int(input("Enter value to find its largest prime factor:  "))

def largest_prime_factor(n): # function that lists all prime numbers from 1 to n
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

largest_prime_factor(n)

'''
The largest prime factor function takes in a parameter n to be some n ∈ Z. Then we create a list of prime numbers from [1,n]. Where the function checks every number in 
the prime list if the number is a factor of the parameter n and if it is then it appends that number to prime factor list. To get the result we use max() function to get 
the largest number in prime factor list. 


To improve: need to find a way to optimize this code because takes a lot of time when n > 10^5.
'''

def faster_func(n):
    pass
