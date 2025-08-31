# Incomplete

# there is computational inefficiency in `43skew.py`
	# each window is counted and then forgotten
	# (ex) s = 1 and w = 1000 bp and you're counting by hand
		# first you get 500 Gs and 500Cs, how many will be in the next window?
		# the GC comp will be: 499, 500, or 501
			# considering w is shifted only once (removing 1 from L and adding 1 to R),
			# the counts will not change by more than the two (L del and R insert)
	# instead of recounting all in the middle, a more efficient algorithm only counts
		# the initial window, after that, it "moves" the window by dropping off 1 nt
		# on the left and adding one on the right

# rewrite `43skew.py` using this more efficient algorithm
# then run it with GC-skew and GC comp in 1000 nt windows in Ecoli genome

import sys

import mcb185
import sequence

# slow
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	w = 10
	for i in range(len(seq) -w +1):
		s = seq[i:i+w]
		print(i, sequence.gc_comp(s), sequence.gc_skew(s))

'''
RC numbers:
Size 	Slow 	Fast
 10		7.28
100		7.24
1000	7.35	
2000    7.17
3000 	7.40
4000 	7.28
5000	7.38 	
'''

'''
IK numbers:
Size 	Slow 	Fast
 10     4.27 	3.50
100 	5.35 	3.61
1000 	15.3 	3.65
2000 	26.3 	3.81
3000 	36.1 	3.79
4000 	47.7 	3.71
5000 	59.0 	3.73
'''