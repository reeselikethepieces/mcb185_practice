# write prog that finds all pythagorean triples for triangles 
	# sides a and b < 100
	# all sides must be integers


for a in range(1, 100):
	for b in range(a, 100):
		c = (a**2 + b**2)**0.5
		if c % 1 == 0: print(a, b, c)