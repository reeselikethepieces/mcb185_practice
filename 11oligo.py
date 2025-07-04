# write a fxn that returns the oligo Tm given num of nts in the oligopolies

def tm(A, C, G, T):
	total = A + C + G + T
	if total <= 13: return (A+T)*2 + (G+C)*4
	else:           return 64.9 + 41*(G+C -16.4) / total

print(tm(1, 2, 2, 1))
print(tm(5, 7, 3, 4))