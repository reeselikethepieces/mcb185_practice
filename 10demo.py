# 10demo.py by Reese

print("hello, again") # greeting

# print is a statement

"""
This is a
multi-line
comment
"""

print(1.5e-2)

# numbers aren't real

print(0.1 * 1)
print(0.1 * 3)

# assignment and types

import math 

a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print(c)
print(type(a), type(b), type(c), sep=', ', end='!\n') # cursor not on prev line

# functions

def pythagoras(a, b):              # a and b are 'parameters'
	c = math.sqrt(a**2 + b**2)     # calculation (c) is sent to the 'caller'
	return c

hyp = pythagoras(3, 4)
print(hyp)

'''
more simply, the code could be written as:

def pythagoras(a,b): return math.sqrt(a**2 + b**2)

above is allowed to be in 1 line b/c there is only 1 statement block
'''

# strings

s = 'hello world'
print(s, type(s))

# conditionals

# a = 3 --> for this example, only the last print() displays since its outside conditional
a = 2
b = 2
if a == b:
	print('a equals b')

if a == b:
	print('a equals b')
	print(a, b)

if a == b:
	print('a equals b')
print(a, b)

# using modulo

def is_even(x):
	if x % 2 == 0: return True
	return False

print(is_even(2))
print(is_even(3))

# boolean

c = a == b     # has value and type
print(c)
print(type(c))

# if-elif-else

if a < b:   print('a < b')
elif a > b: print('a > b')
else:       print('a == b')

if a < b:    print('a < b')
elif a <= b: print('a <= b')
elif a == b: print('this will never print!') # b/c first true condition is above

# chaining

if a < b or a > b:  print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False:       print(True)

# floating point warning: NEVER test for equality with floats, instead examine difference

print(abs(a - b))
if abs(a - b) < 1e-9: print('close enough')

# string comparison: ASCII values a > A-Z

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

# mismatched type error

a = 1
s = 'G'
# if a < s: print('a < s')

# none type

def silly(m, x, b):
	y = m * x + b
	
print(silly(2, 3, 4))     # 'None' reports because there is no 'return' statement
