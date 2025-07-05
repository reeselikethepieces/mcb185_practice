# FizzBuzz by Reese

# make a program that writes out the numbers 1-100
	# if divisible by 3. write 'Fizz'
	# if divisible by 5, write 'Buzz'
	# if divisible by both, write 'FizzBuzz'

for i in range(1, 101):
	if i % 3 == 0 and i % 5 == 0: print('FizzBuzz')
	if i % 3 == 0: print('Fizz')
	if i % 5 == 0: print('Buzz')
	else: print(i)