# 20demo.py by Reese


# tuples - a data type that is a collection of values separated by ','
t = 1, 2
print(t)
print(type(t))
# can contain a mixture of types
person = 'Steve', 21, 57891.50
print(person)
# return statements with more than 1 value
def midpoint(x1, y1, x2, y2):
	x = (x1 + x2) / 2
	y = (y1 + y2) / 2
	return x, y
	
print(midpoint(1, 2, 3, 4))     # calls the fxn and output --> print statement
m = midpoint(1, 2, 3, 4)        # variable assignment
mx, my = midpoint(1, 2, 3, 4)   # "unpacks the tuple"
print(mx, my)                   # prints above
print(m[0], m[1])               # s/s strategy as variable assignment but yields ind vals

# using the mixture of types example to unpack
person = 'Steve', 21, 57891.50
name, age, income = person
print(name, age, income)


# iteration (loops) - involved in soln to most complex problems

# 'while' loop
	# simplest loop and can be evaluated as True or False
#while True:
	#print('hello') want to pump the breaks? i do.
i = 0 
while True:
	i = i + 1
	print('hey', i)
	if i == 3: break
# alternatively:
i = 0
while i < 3:
	i =i + 1
	print('hey', i)
# let's say you want to start at 1 instead of 0, increment 3 at a time, and stop at 10:
i = 1
while i < 10:
	print(i)
	i = i + 3
print('the final value of i is', i)

# 'for' loops
	# adding the range() fxn generates integers given init val, end-before limit, and increment
for i in range(5):
	print(i)
# reverse and counting backwards
for i in range(4, -1, -1):
	print(i)
	# adding a container (for now, the only container is a tuple)
basket = 'milk', 'eggs', 'bread'      # is tuple
for thing in basket:
	print(thing)
# alternatively:
for i in range(len(basket)):
	print(basket[i])

# nesting loops
for i in range(7):
	if i % 2 ==0: print(i, 'is even')
	else:         print(i, 'is odd')

# random numbers
import random

for i in range(5):
	print(random.random())
# IMPORTANT: .random will only provide values between 0 and 1
	
for i in range(3):
	print(random.randint(1, 6))
# IMPORTANT: .randint will provide only integers, not floats

# seeds allow you to reuse the same random numbers
	# useful for debugging
	# all random numbers have a starting "seed" number
random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)              # repeats the random numbers from the above seed(1)
print(random.random())
print(random.random())

# compound assignment
	# instead of writing x = x + 1 --> x += 1
	# s/s with -= and *= 
	# others exist but for now, just the above