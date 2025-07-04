# Assessment Examples


# fxn that computs distance b/w 2 points in graph

def euclid_d(x1, y1, x2, y2): return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(euclid_d(2, 3, 5, 8))


# create a new kind of quality value where the numbers are log2
# use the mappings from symbols to probabilities below
# A 0.5
# B 0.25
# C 0.125
# D 2**-4
# E 2**-5
# F 2**-6
# .... 2**-20

import math


def char_to_prob(c): return 2**((ord(c) - 64)/-1)

print(char_to_prob('A'))
print(char_to_prob('F'))

def prob_to_char(p): 
	if p <= 0 or p >= 1: return None
	else:                return chr(int(-math.log2(p) + 64))

print(prob_to_char(1))
print(prob_to_char(.125))
print(prob_to_char(.000488))



# the rest of the examples were complete and can be seen in 1PP.py