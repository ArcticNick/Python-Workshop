# Problem 1: If we list all natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6, and 9. The sum of these multiples is 23
#Find the sum of all multiples of 3 or 5 below N
n = int(input("Enter value: ")) # user input asking for a value to compute. typecasted as integer data type

a = (n - 1) // 3 # For variables a,b, and c, we have n - 1 because we the sum BELOW N and not including N.
b = (n - 1) // 5 # using floor division allows us to store an integer into the int variables just in case for possible we get a float
c = (n - 1) // 15
sum = (((3 * a * (a + 1)) // 2) + ((5 * b * (b + 1)) // 2)) - ((15 * c * (c + 1)) // 2)
# all natural numbers that are multiples of 15 are counted twice, lcd(3,5) = 15, so we must remove all multiples of 15
print('The sum of all multiples of 3 and 5 that is less than ' + str(n) + ' is ' + str(sum))

'''
We know from the Gauss Summation Formula that the sum of natural numbers from 1 to N is (N/2)(N+1).
If we just want the sum of multiples of some natural number k, then we have (k/2)(N/k)((N/k)+1) => (N/2)((N/k)+1).
'''