# unit3 practice problems

# write fxn that returns min value of a list

listA = ['apples', 'spinach', 'chicken', 'Lucerne cottage cheese', 'lemons']
listB = ['ASDLFKHSDGLSGH']

# reese OG
def minval(l):
	l.sort()
	for i in range(len(l)):
		return l[0]
	
print(minval(listA))

# kouse way
def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini

print(minimum(listA))
 
# write fxn that returns both min and max value of list
# did without looking xD
def minimaxi(vals):
	mini = vals[0]
	maxi = vals[-1]
	for val in vals[1:]:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi

print(minimaxi(listA))
# write fxn that returns mean of values of list
# write fxn that computes entropy of probability distribution
# write fxn that computes Kullback-Leibler distance b/w 2 sets of prob distributions