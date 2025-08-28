# first library
	# methods used in this file:
		# .replace(), .append(), .join()
# central dogma


# str.replace() method searches for substrings and converts into other substrings
	# in the form of a "copy"
# since strings are immutable, the original string is not modified

# transcription
def transcribe(dna):
	return dna.replace('T', 'U')
	
# reverse-complment (rc)
def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if   nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:           rc.append('N')
	return ''.join(rc)
	
# translation
'''
def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if   codon == 'ATG': aas.append('M')
		elif codon == 'TAA': aas.append('*')
		elif codon == 'TAG': aas.append('*')
		elif codon == 'TGA': aas.append('*')
		else:                aas.append('X')
	return ''.join(aas)
'''

# alternative 
# remember lists and tuples do not have find() method so we must use index()
def translate(dna):
	codons = ('ATG', 'TAA', 'TAG', 'TGA')
	aminos = 'M***'
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		# ask if codon is in the tuple
		if codon in codons:
			# ask for the position
			idx = codons.index(codon)
			aa = aminos[idx]
			aas.append(aa)
		else:
			aas.append('X')
	return ''.join(aas)

# because variables in lines 51, 52 (idx, aa) are only used once, they don't need to exist
	# thus, they can be written in one line (more sophisticated in programming world)
	# but doesn't necessarily make it more readable 
# aas.append(aminos[codons.index(codon)])