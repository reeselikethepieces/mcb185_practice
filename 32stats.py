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

numsum = 0
mini = vals[0]
maxi = vals[0]
total = 0
meanie = 1
d = 0
s = 1
sd = 1
medi = 1
for _ in vals:
	# n of values
	numsum = len(vals)
	# mini, maxi
	if _ < mini: mini = _
	if _ > maxi: maxi = _
	# mean
	total += _
	meanie = total / numsum

# these need to be fixed
	# sd
	s += (_ - meanie)**2
	d = numsum - 1
	sd = (s / d)**0.5
	# median
	vals.sort()
	if _ % 2 == 0: medi = vals[int((numsum//2) + (numsum/2 +1))/2]
	else:          medi = vals[numsum//2]
	
	
	

print(sys.argv)
print(f'n: {numsum}, min: {mini}, max: {maxi}, mean: {meanie:.3f}, sd: {sd:.3f}')