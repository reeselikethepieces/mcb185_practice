# practice assessment examples

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

seq = str(sys.argv[1])

position = 1
frame = 1

for i in range(len(seq) - 2):	
	frame = i % 3 + 1
	
	codon = seq[i:i+3]
	print(f'{position}\t{frame}\t{codon}')
	
	position += 1
	
	
	

# 4. Comparing 33 and 34, which solution do you like better? In what situations do you 
	# think the 33 strategy is better? When would 34 be better?
''' I 33 better for the type of problem that it is. I feel like when trying to figure
out the shared birthdays in a class, makes sense that as you fill the class with # of
students, each student has a birthday and you almost fill the class based on student's
bdays. 34 doesn't make much sense in the context of the birthday ex to me because the 
calendar is essentially a much bigger range to put 23 "darts" on vs. each student has 
random birthday and as you check off a student, you almost "ask" them what their bday is
while filling the class.'''