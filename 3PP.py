# unit3 practice problems

# write fxn that returns min value of a list

listA = ['apples', 'spinach', 'chicken', 'Lucerne cottage cheese', 'lemons']
listB = ['ASDLFKHSDGLSGH']

# reese OG
def minval(x):
	x.sort()
	return x[0]
	 
print(minval(listA))

# kouse way
def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini

print(minimum(listA))
 
# write fxn that returns both min and max value of list
# did wrong without looking Dx
# did again reese way (hardcoding)
def minimaxi(vals):
	vals.sort()
	mini = vals[0]
	maxi = vals[-1]
	return mini, maxi

print(minimaxi(listA))

# kouse way 
def minimaxi(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi

print(minimaxi(listA))
	
# write fxn that returns mean of values of list
s = 'ASDLFKHSDGLSGH'
s1 = ['A', 'C', 'G', 'T']
probs = [0.2, 0.4, 0.1, 0.3]
def mean(vals):
	total = 0
	for val in vals: total += val
	return total/len(vals)

# print(mean(listA))
print(mean(probs))

# write fxn that computes entropy of probability distribution
import math

def entropy(probs):
	h = 0
	for p in probs:
		h -= p * math.log2(p)
	return h

print(entropy([0.2, 0.3, 0.5]))

# write fxn that computes Kullback-Leibler distance b/w 2 sets of prob distributions
def dkl(P, Q):
	d = 0
	for p,q in zip(P, Q):
		d += p * math.log2(p/q)
	return d
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.2)     # allowed bc lists and tuples can be zipped in parallel
print(dkl(p1, p2))