# Pairwise Comparison

# given a list of things, a freq. operation is to compare all things to each other
	# i.e. list[cities], one might want to compare their pops or distance from each other
	# i.e. list[proteins], want to know which ones are related to each other
	# i.e. list[aas], want to know their alignment score when paired with each other

# there are three ways to perform all-vs-all comparisons
	# all combos
	# unique pairings, allowing self-comparison (half matrix with diagonal)
	# unique pairings, disallowing self-comparisons (half matrix w/out diagonal)

# given
nts = ['A', 'C', 'G', 'T']
# there are 16 pairwise combos (2**n where n == 4)
	# AA, AC, AG, AT, CA, CC, CG, CT, GA, GC, GG, GT, TA, TC, TG, TT
def nt_pairs(nts):
	pairs = []
	for nt1 in nts:
		for nt2 in nts:
			pairs.append(nt1 + nt2)
	return pairs
print(nt_pairs(nts)) # i want to save this list for later, so assign result to a variable

ntpairs = nt_pairs(nts)

# below was written before the list of pairs (ntpairs) 
# pick up here to adjust functions below where position1 and position2 work with analogy
# CA and AC can be redundant
print('sending invitations to dinner party...')
def needs_invite(position1, position2):
	if position1 == position2:
		return False
	else:
		print('send invite with address')
		return True
		
print(needs_invite('C', 'G'))
print(needs_invite('G', 'C'))
# below returns True bc it is redundant to tell yourself your own address
print(needs_invite('C', 'C'))

# CA and AC can also be important and be accounted for
# not that you would, but if you were to take a headcount only given location 
print('headcount?')
def mouths_to_feed(position1, position2):
	myself = 1
	if position1 == position2:
		return myself
	else: 
		return myself + 1

print(mouths_to_feed('C', 'G'))
print(mouths_to_feed('G', 'C'))
print(mouths_to_feed('C', 'C'))


# probably should have continued on reading before i played around above ^
'''
for i in range(0, len(list)):
	for j in range(X, len(list)):
X = 0 = all combinations
X = 1 = half-matrix with diagonal
X = i+1 = half-matrix without diagonal
'''