# D&D Stats
	# 6 stats/character
		# stats = (strength, intelligence, wisdom, dexterity, constitution, & charisma)
			# sum(3*6-sided dice) = stat
				# each stat = range(3, 18) with mean = 10.5
	# write programs with the following variations:
		# 3D6: roll 3 six-sided dice
		# 3D6r1: roll 3 six-sided dice, but re-roll any 1s
		# 3D6x2: roll pairs of six-sided 3 times, taking max each time
		# 4D6d1: roll 4 six-sided dice, dropping the lowest die roll
import random

# works 
'''
roll = 0
for j in range(5):
	d1 = random.randint(1,6)
	d2 = random.randint(1,6)
	d3 = random.randint(1,6)
	roll = d1 + d2 + d3
	print(j, roll)
'''

# also works
'''
random.seed(1)
total = 0
for i in range(3):
	i = random.randint(1,6)
	total += i
	print(i, total)
'''

# above but rewritten with variables that pertain to the problem
'''
random.seed(1)
dice_roll = 0
amt = 3
for di in range(amt):
	di = random.randint(1,6)
	dice_roll += di
	print(di, dice_roll)
'''
# random.seed(1)

# 3D6
trial = 100000
total = 0
for j in range(trial):
	ndice = 3
	stat = 0
	for i in range(ndice):
		di = random.randint(1, 6)
		stat += di
	total += stat
print(total/trial)


# 3D6r1
trial = 100000
total = 0
for j in range(trial):
	ndice = 3
	stat = 0
	for i in range(ndice):
		di = random.randint(1, 6)
		if di == 1: di = random.randint(1, 6)
		stat += di
	total += stat
print(total/trial)

# the commented out conditional only works the for the first time, if a re-roll also
# is a '1', it will stay; thus, to alleviate this, need 'while' loop


# 3D6x2: roll pairs of six-sided 3 times, taking max each time
def my_max(a, b):
	if a > b: return a
	else:     return b

trial = 100000
total = 0
for j in range(trial):
	ndice = 3
	stat = 0
	for i in range(ndice):
		di1 = random.randint(1, 6)
		di2 = random.randint(1, 6)
		stat += my_max(di1, di2)
	total += stat
print(total/trial)


# 4D6d1: roll 4 six-sided dice, dropping the lowest die roll
def min_four(a, b, c, d):
	if a < b < c < d: return a
	elif b < c < d:   return b
	elif c < d:       return c
	else:             return d

trial = 100000
total = 0
for i in range(trial):
	di1 = random.randint(1, 6)
	di2 = random.randint(1, 6)
	di3 = random.randint(1, 6)
	di4 = random.randint(1, 6)
	stat = di1 + di2 + di3 + di4 - min_four(di1, di2, di3, di4)
	total += stat

print(total/trial)