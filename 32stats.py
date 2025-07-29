# yikeserroni, this page is still in progress 


# 32stats

# write a prog that reports descriptive stats for the numbers on the command line
# descriptive stats = [num of values, min and max values, mean and sd, mediam]

# is this hardcoding?
# numsum = len(sys.argv[1:])
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
s_diff = []
for x in vals:
	# squared differences
	s = (x - avg)**2
	s_diff.append(s)
# sd part 2		
total_s = 0
for s in s_diff:
	total_s += s
# sd part 3
sd = (total_s / (num_vals-1))**0.5
	

# median

print(sys.argv)
print(f'n: {num_vals}, min: {mini}, max: {maxi}, mean: {avg:.3f}, sd: {sd:.3f}')


'''
in CL: 1 1 4 3 2
terminal should return: ['32stats.py', '1', '1', '4', '3' '2']
                        n: 5, min: 1.0, max 4.0, mean: 2.200, sd: 1.304
'''