# Assessment Examples

# re-write fizzbuzz as fast as you can

for i in range(1, 101):
	if i % 3 == 0 and i % 5 == 0: print('FizzBuzz')
	if i % 3 == 0: print('Fizz')
	if i % 5 == 0: print('Buzz')
	else: print(i)
	

# write an endlessly running program that est pi using Gregory-Leibniz series
	# pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 ...

pi = 0
sign = 1
denom = 1
while True:
	pi += sign * (1 / denom)
	denom += 2
	sign *= -1
	print(4 * pi)


# modify 25deathsaves for haflings (they get adv on death saves)
import random

# advantage max of 2 fxn
def my_max(a, b):
	if a > b: return a
	return b
	
trials = 10000
revi = 0
dies = 0
stab = 0
for i in range(trials):
	fail = 0
	succ = 0
	while True:
		r1 = random.randint(1, 20)
		r2 = random.randint(1, 20)
		roll = my_max(r1, r2)
		
		if  roll == 20: 
			revi += 1 
			break
		
		if   roll == 1:  fail += 2
		elif roll < 10:  fail += 1
		else:            succ += 1
		
		if   fail >= 3:  
			dies += 1 
			break
		if   succ == 3:  
			stab += 1
			break
	
print(dies/trials, stab/trials, revi/trials)
print(dies/trials + stab/trials + revi/trials)   # should equal 1