# redo of 44skew.py

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

w = int(sys.argv[2])

'''
# slow
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) -w +1):
		s = seq[i:i+w]
		print(i, sequence.gc_comp(s), sequence.gc_skew(s))
'''

'''
# medium
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) -w +1):
		window = seq[i:i+w]
		g = window.count('G')
		c = window.count('C')
		if g+c == 0: continue
		print(i, (g+c)/w, (g-c)/(g+c))
'''
		
'''
windo_size 	slow	med?*    fast
    10	 	7.33	 6.65	 6.93
   100 	 	9.09	 7.59    8.01
  1000		23.71	12.48	12.89
  2000		42.24	25.55	26.25
  3000		72.43	37.87	38.40
  4000		91.78	50.29	50.95
  5000 	   117.95 	63.62   64.36
'''

# fast
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	initial_w = seq[:w]
	g = initial_w.count('G')
	c = initial_w.count('C')
	if g+c == 0: continue
	print(0, (g+c)/w, (g-c)/(g+c))

	for i in range(1, len(seq) - w + 1):
		next_nt = seq[i + w - 1]
		rest_w = initial_w[1:] + next_nt
		
		g = rest_w.count('G')
		c = rest_w.count('C')
		if g+c == 0: continue
		print(i, (g+c)/w, (g-c)/(g+c))
		
		initial_w = rest_w
