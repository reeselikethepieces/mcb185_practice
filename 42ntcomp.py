# 42ntcomp.py calculates the composition of nts in a FASTA file


# calculates GC composition of each seq separately
'''
import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	gc = 0
	for nt in seq:
		if nt == 'C' or nt == 'G': gc += 1
#	print(name, gc/len(seq))
'''
'''
CL input: python3 42ntcomp.py ../MCB185/data/C.elegans.fa.gz
'''


# individual variables
# other genomes contain additional or alternative nts
	# i.e. A. thaliana has nts ACGT and N

# stack of if-elif-else statements to assign ind. var to each nt 
'''
import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	A = 0
	C = 0
	G = 0
	T = 0
	N = 0
	for nt in seq:
		if   nt == 'A': A += 1
		elif nt == 'C': C += 1
		elif nt == 'G': G += 1
		elif nt == 'T': T += 1
		else:           N += 1
'''
#	print(name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))
'''
CL input: python3 42ntcomp.py ../MCB185/data/A.thaliana.fa.gz
'''


# list variation is to create a list to hold the counts
'''
import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	counts = [0, 0, 0, 0, 0]
	for nt in seq:
		if   nt == 'A': counts[0] += 1
		elif nt == 'C': counts[1] += 1
		elif nt == 'G': counts[2] += 1
		elif nt == 'T': counts[3] += 1
		else:           counts[4] += 1
	print(name, end=' ')
	for n in counts: print(n/len(seq), end=' ')
	print()
'''
'''
CL input: python3 42ntcomp.py ../MCB185/data/A.thaliana.fa.gz
'''

# indexing with str.find()
# major diff w/ this (ex) is replacing if-elif-else with str.find()
'''
import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	nts = 'ACGTN'
	counts = [0] * len(nts)
	# every nt will be compared to alphabet in 'nts' above
	for nt in seq:
		idx = nts.find(nt)
		counts[idx] += 1
	print(name, end=' ')
	for n in counts: print(n/len(seq), end=' ')
	print()
# important notice: if the seq in the fasta file contained a letter not in the alphabet,
    # 'nts', then that unique letter would get a '-1' which would be totalled in the last
    # position in the list, counts[], AKA nt 'N' 
'''
'''
CL input: python3 42ntcomp.py ../MCB185/data/A.thaliana.fa.gz
'''


# counting any letter ** personal fav
	# in the previous example, the alphabet was a string variable
	# in order to count all letters, the alphabet needs to be in a container
		# this container must be mutable (i.e. a list)
'''
import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	nts = []
	counts = []
	for nt in seq:
		if nt not in nts:
			nts.append(nt)
			counts.append(0)
		idx = nts.index(nt)
		counts[idx] += 1
	print(name)
	for nt, n in zip(nts, counts):
		print(nt, n, n/len(seq))
	print()
'''
'''
CL input: python3 42ntcomp.py ../MCB185/data/A.thaliana.fa.gz
you will see in Chr2, additional nts: Y, K, S
'''


# counting with str.count()
	# count specific letters
	# downside to this version is you have to specify the alphabet ahead of time
		# for those that are not in the alphabet you provide, will not be accounted for
import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	print(name, end=' ')
	for nt in 'ACGTN':
		print(seq.count(nt) / len(seq), end =' ')
	print()
'''
CL input: python3 42ntcomp.py ../MCB185/data/A.thaliana.fa.gz
'''