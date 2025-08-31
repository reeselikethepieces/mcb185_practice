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
7.33
7.24
7.39
7.44
7.29
7.31
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

'''
1. How does the function ‘time’ work?
	I imagine there is a loop within the fxn for a few reasons.
	I wonder if the timer begins once 
	compiles/interprets into machine code and stops once the processor returns a value…. 
	or if within the loop, there is some time that collects line vy line and then adds up 
	at the end for a total runtime count
2. Time function is an _internal-based on convo the other day_ ?
    Regardless, could one go in and edit that type of library?
        If yes - maybe change or add ‘total’ time where total = user + system
3. When I ran my programs at various window lengths, it appeared the change in system 
	time was negligible as it barely changed —> but could this be due to something in my 
	computer/RAM…
    	What do terms like i5, i7, i9 mean?
'''