# unit 1 practice problems by Reese


# write a fxn that det if a number is an int

def is_integer(n):
	if n % 1 == 0: return True
	else:          return False

print(is_integer(1))
print(is_integer(12))
print(is_integer(-6))
print(is_integer(1.0))
print(is_integer(3.132))

# write a fxn that determines if a number is a valid prob

def is_validprob(n):
	if n >= 0 and n <= 1: return True
	else:                 return False
# given multiple probabilities, an additional condition is necessary (sum of n's == 1)

print(is_validprob(1))
print(is_validprob(3))
print(is_validprob(0.35875))
print(is_validprob(0))
print(is_validprob(-.245))

# write a fxn that returns mw of DNA letter; return 'None' if not a nt

def mw_dna(nt):
	if nt == 'A': return 313.2
	if nt == 'C': return 289.2
	if nt == 'G': return 329.2
	if nt == 'T': return 304.2
	else:         return None

print(mw_dna('C'))
print(mw_dna('c'))
print(mw_dna('Z'))

# write a fxn that returns complement of DNA letter; return 'None' if not DNA

def dna_comp(nt):
	if nt == 'A': return 'T'
	if nt == 'C': return 'G'
	if nt == 'G': return 'C'
	if nt == 'T': return 'A'
	else:         return None

print(dna_comp('C'))
print(dna_comp('A'))
print(dna_comp('Z'))

# write a fxn that returns max of 3 numbers

def maxofnums(a, b, c):
	if a > b and a > c:   return a
	elif b > a and b > c: return b
	else:                 return c

print(maxofnums(2, 5, 8))
print(maxofnums(15, 45, 5))
print(maxofnums(26, 8, 5))

# write a fxn that returns sensitivity, specificity, and F1 score

def statvals(tp, tn, fp, fn):
	denom1 = (tp + fn)
	denom2 = (tn + fp)
	denom3 = ((2 * tp) + fp + fn)
	if denom1 == 0 or denom2 == 0 or denom3 == 0:
		return 'undefined'
	sens = tp / denom1
	spec = tn / denom2
	f1 = (2 * tp) / denom3
	return sens, spec, f1

print(statvals(8, 5, 2, 6))
print(statvals(0, 5, 0, 0))
print(statvals(0, 5, 2, 0))

# write a fxn that returns shannon entropy for nt counts

import math

def shentropy(A, C, G, T):	
	
	total = A + C + G + T
	if total == 0: return 0
	
	pa = A/total
	pc = C/total
	pg = G/total
	pt = T/total
	
	if pa > 0: ea = -pa * math.log2(pa)
	else:      ea = 0
	if pc > 0: ec = -pc * math.log2(pc)
	else:      ec = 0
	if pg > 0: eg = -pg * math.log2(pg)
	else:      eg = 0
	if pt > 0: et = -pt * math.log2(pt)
	else:      et = 0.0
	
	return ea + ec + eg + et
	
print(shentropy(0, 0, 0, 0))
print(shentropy(8, 6, 6, 8))
print(shentropy(0, 5, 5, 6))
print(shentropy(0, 5, 2, 0))