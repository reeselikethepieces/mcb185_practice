# yikeserroni, this page is still in progress 


# 32stats

# write a prog that reports descriptive stats for the numbers on the command line
# descriptive stats = [num of values, min and max values, mean and sd, mediam]

import sys

# is this hardcoding?
# numsum = len(sys.argv[1:])

vals = []
for arg in sys.argv[1:]:
	f = float(arg)
	vals.append(f)

# initiation variables
# n of values
numsum = 0
# mini, maxi
mini = vals[0]
maxi = vals[0]
# mean
total = 0
avg = 1
# sd
s = 0
sd = 1
# median
medi = 1

for x in vals:
	# n of values
	numsum = len(vals)
	
	# mini, maxi
	if x < mini: mini = x
	if x > maxi: maxi = x
	
	# mean
	total += x
	avg = total / numsum
	
	# s in sd calculation
	s += (x - avg)**2
	s.diffs.append(s)
	# sum of s 
	stotal = 0
	for s in s.diffs:
		stotal += vals
	# final calc of sd 
	sd = (s / (numsum -1)**0.5
	
	# pickup here
	# median
	vals.sort()
	if _ % 2 == 0: medi = vals[int((numsum//2) + (numsum/2 +1))/2]
	else:          medi = vals[numsum//2]
	
	
	

print(sys.argv)
print(f'n: {numsum}, min: {mini}, max: {maxi}, mean: {avg:.3f}, sd: {sd:.3f}')