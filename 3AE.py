# practice assessment examples

# 1. Can you figure out what the following line prints without typing it out?
# print('-'.join(list('ABCDE'))[3:6])
	# initially, i thought it would be CDE with '-' in b/w
	# obviously, the answer is -C- b/c the slice is done on the string it is attached
		# to, in this case, '-' string was added to list; thus, slice is on new string


# 2. Add the N50 calculation to your 32stats.py program.
# had to ''' this problem's code block due to ValueError from line 16, f = float(arg)
'''
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
half_vals = total_vals // 2

print(sys.argv)
print(f'n: {num_vals}, min: {mini}, max: {maxi}, mean: {avg:.3f}, sd: {sd:.3f}, medi: 
{medi}, N50: {half_vals}')
'''


# 3. Given a nucleotide sequence such as ATGCTGTAA, create an output that shows the 
	# position, frame, and codon separated by tabs.
'''
1	1	ATG
2	2	TGC
3	3	GCT
4	1	CTG
5	2	TGT
6	3	GTA
7	1	TAA
'''

import sys

seq = str(sys.argv[7])

position = 1
frame = 1

for i in range(len(seq-2)):
	codon = seq[i:i+3]

	print(f'{position}\t{frame}\t{codon}')
	
	position += 1
	
	if frame < 3: frame += 1
	else:         frame = 1


# 4. Comparing 33 and 34, which solution do you like better? In what situations do you 
	# think the 33 strategy is better? When would 34 be better?
''' I 33 better for the type of problem that it is. I feel like when trying to figure
out the shared birthdays in a class, makes sense that as you fill the class with # of
students, each student has a birthday and you almost fill the class based on student's
bdays. 34 doesn't make much sense in the context of the birthday ex to me because the 
calendar is essentially a much bigger range to put 23 "darts" on vs. each student has 
random birthday and as you check off a student, you almost "ask" them what their bday is
while filling the class.'''