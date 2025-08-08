# practice assessment examples

# 1. Can you figure out what the following line prints without typing it out?
# print('-'.join(list('ABCDE'))[3:6])
	# initially, i thought it would be CDE with '-' in b/w
	# obviously, the answer is -C- b/c the slice is done on the string it is attached
		# to, in this case, '-' string was added to list; thus, slice is on new string


# 2. Add the N50 calculation to your 32stats.py program.
# had to ''' this problem's code block due to ValueError from line 16, f = float(arg)

import sys

vals = []
for arg in sys.argv[1:]:
	f = float(arg)
	vals.append(f)

# n of values
num_vals = len(vals)


# mini, max, and mean
mini = vals[0]
maxi = vals[0]
total_vals = 0

for x in vals:
	# mini, maxi
	if x < mini: mini = x
	if x > maxi: maxi = x
	# mean part 1
	total_vals += x
# mean part 2
avg = total_vals / num_vals


# sd part 1
s = 0
for x in vals:
	s += (x - avg)**2
# sd part 3
sd = (s / (num_vals-1))**0.5
	

# median
vals.sort()
medi = None
if num_vals % 2 != 0: medi = vals[num_vals // 2]
else:                 medi = (vals[num_vals // 2] + vals[(num_vals // 2) - 1])/2

# N50
# ctl = contig_length

half_vals = total_vals // 2

ND50 = None
total = 0

for ctl in reversed(vals):
	total += ctl
	if total >= half_vals:
		ND50 = ctl
		break
	
	
	

print(sys.argv)
print(f'n: {num_vals}, min: {mini}, max: {maxi}, mean: {avg:.3f}, sd: {sd:.3f}, medi: {medi}, N50: {ctl}')

# the N50 of {1, 1, 2, 3, 3, 5, 6} is 5