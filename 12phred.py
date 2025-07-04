# write fxns that conver quality value symbols into error rates and vice-versa
# ord(letter) --> ASCII value
# chr(ASCII value) --> letter

import math


def char_to_prob(c): return 10**((ord(c) - 33)/-10)

print(char_to_prob('A'))
print(char_to_prob('B'))
print(char_to_prob('!'))


def prob_to_char(p): 
	if p <= 0 or p >= 1: return None
	else:                return chr(int(-10 * math.log10(p)) + 33)
	
print(prob_to_char(0.001))
print(prob_to_char(0))
print(prob_to_char(0.398))