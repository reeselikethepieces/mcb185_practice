# practice problems for unit 2


# write fxn that calculates triangular numbers
	# aka sum of the numbers 1 to n

def triangular(n):
	tri = 0
	for i in range(n+1):
		tri = tri + i
		#print(tri)
	return tri

print(triangular(5))
print(triangular(1))

# write fxn calcs factorial of a number

def factorial(n):
	if n == 0: return 1        # outside the loop
	fact = 1
	for i in range(2, n+1):
		fact = fact * i
	return fact
	
print(factorial(0))
print(factorial(1))
print(factorial(3))
print(factorial(5))

# write fxn computing poisson prob of k events
	# expectation of n: n^ke^-n/k!
import math

def poisson(n, k):
	return n**k * math.e**-n / factorial(k)

print(poisson(3, 6))

# write fxn solves "n choose k"
	# n! / k!(n-k)!

def nchook(n, k):
	return factorial(n) / (factorial(k)*factorial(n-k))

print(nchook(2, 3))

# write fxn estimating euler's number (2.71828...)
	# infinite sum of 1/n!

def euler(n):
	ssum = 0
	for i in range(n):
		ssum = ssum + 1 / factorial(i)
	return ssum

print(euler(5))
print(euler(500))

# write fxn determining if number is prime

def is_prime(n):
	for i in range(2, n//2 +1):
		if n % i == 0: return False
	return True

# write fxn estimating Pi(3.14159..) using nilakantha series
	# Pi = 3 + 4/(2x3x4) - 4/(4x5x6) + 4/(6x7x8) -...

#trial1
def nilakantha(n):
	pi_est = 0
	for i in range(1, n+1):
		n = 2 * i
		d = n * (n+1) * (n+2)
		if i % 2 == 0: pi_est = pi_est - 4 / d
		else:          pi_est = pi_est + 4 / d
	return 3 + pi_est

print(nilakantha(5))
	
#korf
def nilakantha(limit):
    pi = 3
    for i in range(1, limit+1):
        n = 2 * i
        d = n * (n+1) * (n+2)
        if i % 2 == 0: pi = pi - 4 / d
        else:          pi = pi + 4 / d
    return pi

print(nilakantha(5))