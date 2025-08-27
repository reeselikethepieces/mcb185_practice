# created soft link with CL 'ln -s ~/Code/MCB185/src/mcb185.py .'
# libraries are collections of reusable fxns 

import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline[:30], seq[:40], len(seq))

# each iteration of the `for` loop retrieves the next seq record from the FASTA file
	# each record is returned as a tuple containing defline and seq as a string
	# this function works with both normal and compressed files

'''
CL run:
python3 41fasta.py ../MCB185/data/A.thaliana.fa.gz
python3 41fasta.py ../MCB185/data/C.elegans.fa.gz
python3 41fasta.py ../MCB185/data/D.melanogaster.fa.gz
'''
