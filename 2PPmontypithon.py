# harder unit 2 practice problem


# monty pi-thon
	# write a program that est pi using Monte Carlo methods
		# generate random values for x and y from 0 to 1 (1)
		# calculate distance to the origin (2)
		# if distance is < 1, point is inside circle (3)
		# ratio of points(inside) vs. total == pi/4 (4)
		# output each iteration and watch ratio get closer to pi (5)
		# use endless while loop and stop with ctrlC (6)


import random

inside = 0                          # (4.0)
outside = 0                         # (4.0)
while True:                         # (6)
	x = random.random()             # (1)
	y = random.random()             # (1)
	# print(x, y)
	d = (x**2 + y**2)**0.5          # (2)
	if d < 1: inside += 1           # (3)
	else:     outside += 1
	total = inside + outside        # (4.1)
#	NO print(4 * inside)
	print(4 * inside/total)         # (4.2) and (5)