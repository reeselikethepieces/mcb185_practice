# redo of `43skew.py` and `44skew.py` without str.count

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

w = int(sys.argv[2])
'''
# slow `43skew.py`	
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) -w +1): 
		c = 0
		g = 0
		for nt in seq[i:i+w]:
			if   nt == 'C': c += 1
			elif nt == 'G': g += 1
		if c+g == 0: 
			gc = 0
			skew = 0
		else: 
			gc = (c+g)/w
			skew = (g-c)/(g+c)
		print(i, gc, skew)
		
'''
'''
windo_size 	 slow    fast
    10	 	 8.25	
   100 	 	35.32	
  1000	   246.77	
  2000	   515.47	
  3000			
  4000			
  5000 	   	
'''

#PICK UP HERE
# fast 
c = 0
g = 0
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	# initial seq
	initial_w = list(seq[:w])
	for nt in initial_w:
		if   nt == 'C': c += 1
		elif nt == 'G': g += 1
	if c+g == 0:
		gc = 0
		skew = 0
	else:
		gc = (c+g)/w
		skew = (g-c)/(g+c)
	print(0, gc, skew)
	# thereafter
	for i in range(len(initial_w), len(seq) -w + 1):
		first_position = initial_w.pop(0)
		if   first_position == 'C': c -= 1
		elif first_position == 'G': g -= 1
		
		last_position  = initial_w.append
		if   last_position == 'C': c += 1
		elif last_position == 'G': g += 1
		
		print(i, gc, skew)	
		
	
	
	
	
