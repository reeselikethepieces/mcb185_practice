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


#3D6
limit = 4
total = 0
for j in range(limit):
#	print(j)
	amt = 3
	roll = 0
	for di in range(amt):
		di = random.randint(1,6)
		print('ind di is', di)
		roll += di
#		print(di, roll)
	print('    roll for 3D6', roll)
	
	total += roll
print('        the average roll is', total/limit)


# 3D6r1
limit = 4 
total = 0
for j in range(limit):
	amt = 3
	roll = 0
	for di in range(amt):
		di = random.randint(1, 6)
#		if di == 1: di = random.randint(1, 6)       see explanation below
		while di == 1: di = random.randint(1, 6)
		
		print('ind di is', di)
		roll += di
	print('    roll for 3D6', roll)
	total += roll
print('        the average roll is', total/limit)

# the commented out conditional only works the for the first time, if a re-roll also
# is a '1', it will stay; thus, to alleviate this, need 'while' loop


# taking break- will continue later
# 3D6x2: roll pairs of six-sided 3 times, taking max each time
# 4D6d1: roll 4 six-sided dice, dropping the lowest die roll