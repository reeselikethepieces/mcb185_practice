# import libraries
import sys
import math

# harvest words on the command line and turn them into probabilities
# container to hold probabilities
probs = []
# steps thru each argument (word) on CL using slice to skip over `sys.argv[0]`
for arg in sys.argv[1:]:
	f = float(arg)
	if f <= 0 or f >= 1: sys.exit('error: not a valid probability')
	probs.append(f)

# check if sum(probs) on CL == 1
total = 0
for p in probs: total += p
if not math.isclose(total, 1.0):        # bc we never ask if floats are == to anything 
	sys.exit('error: probs must sum to 1.0')

# calculate entropy
h = 0
for p in probs:
	h -= p * math.log2(p)

print(f'{h:.4f}')

'''
python3 31entropy.py 0.5 0.5
python3 31entropy.py 0.25 0.25 0.25 0.25
python3 31entropy.py 0.4 0.3 0.2 0.1
python3 31entropy.py 0.5 0.6
python3 31entropy.py 0.5 -1
'''