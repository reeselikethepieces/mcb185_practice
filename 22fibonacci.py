# write prog that reports the first 10 numbers from Fibonacci seq
	# fibseq = 0,1,1,2,3,5,8,13,21,34
	# initialize and keep track of 2 values

a = -1
b = 1
for _ in range(10):
	c = a + b
	print(c)
	a = b
	b = c