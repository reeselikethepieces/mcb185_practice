# certain event:
	# need to roll d20 --> succeed or not
	# can give advantage(max(two d20s)) or disadvantage(min(two d20s))
# saving throws have difficulty classes (DC)
# write program that simulates saving throws against 5, 10, 15 DCs
# make a table showing the probability of success normally, advantage, and disadvantage

import random

def my_max(a, b):
	if a > b: return a
	return b

def my_min(a, b):
	if a < b: return a
	return b

trials = 1000

# dc5 success
norm5 = 0
adv5 = 0
dis5 = 0
# dc10 success
norm10 = 0
adv10 = 0
dis10 = 0
# dc15 success
norm15 = 0
adv15 = 0
dis15 = 0

for i in range(trials):
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	
	norm = r1
	adv = my_max(r1, r2)
	dis = my_min(r1, r2)

	# dc5
	if norm   >= 5: norm5 += 1
	if adv    >= 5: adv5  += 1
	if dis    >= 5: dis5  += 1
	
	# dc10
	if norm  >= 10: norm10 += 1
	if adv   >= 10: adv10  += 1
	if dis   >= 10: dis10  += 1

	# dc15
	if norm  >= 15: norm15 += 1
	if adv   >= 15: adv15  += 1
	if dis   >= 15: dis15  += 1

print('     | norm | adv | dis |')
print('dc5  |', format(norm5/trials, '.3f'), format(adv5/trials, '.3f'), format(dis5/trials, '.3f'))
print('dc10 |', format(norm10/trials, '.3f'), format(adv10/trials, '.3f'), format(dis10/trials, '.3f'))
print('dc15 |', format(norm15/trials, '.3f'), format(adv15/trials, '.3f'), format(dis15/trials, '.3f'))