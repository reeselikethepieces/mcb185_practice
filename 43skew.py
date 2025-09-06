# canonical form of translate() fxn in `42ntcomp.py`
'''
w = 10
s = 1
for i in range(0, len(seq) -w + 1, s):
	subseq = seq[i:i+w]
'''

# now, we will write a program that uses a sliding window algorithm
	# to computer GC comp and GC=skew along len(seq)

# first: create functions by adding them to our `sequence.py` dictionary
# then: add a test calling to `test_sequence.py`
# finally: put it all together, below
import sequence

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10
for i in range(len(seq) -w +1):
	s = seq[i:i+w]
	print(sequence.gc_comp(s), sequence.gc_skew(s))