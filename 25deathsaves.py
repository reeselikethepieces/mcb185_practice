# health <= 0: unconscious
# roll d20
	# if roll < 10: failure
	# if roll >=10: success
	# if 3 failures: die
	# if 3 successes = stable
	# if roll == 1: + 2 failures
	# if roll == 20: revive
# output: prob one dies, stabilizes, revives

import random

trials = 10000
revi = 0
dies = 0
stab = 0
for i in range(trials):
	fail = 0
	succ = 0
	while True:
		roll = random.randint(1, 20)
		
		if   roll == 20: 
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