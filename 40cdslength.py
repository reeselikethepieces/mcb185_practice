# examine E. coli GFF file using command below
	# zless ~/Code/MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz

# create a program that reports the lengths of protein-coding genes in E. coli genome
	# needs to perform the following as it reads each line of the file:
		# skip over comment lines (beginning)
		# find CDS features (or skip over all non-CDS features)
		# extract begin and end coordinates
		# convert coordinates to integers
		# report length of CDS (end - begin +1)
	
import gzip
import sys

with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line[0] != '#': 
			words = line.split()
			if words[2] == 'CDS':
				beg = int(words[3])
				end = int(words[4])
				print(end - beg + 1)
				

# 'continue' statement is used to immediately end current iteration and restart with 
	# the next iteration 
	# other languages use 'next'

with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		words = line.split()
		if words[2] != 'CDS': continue
		beg = int(words[3])
		end = int(words[4])
		print(end-beg + 1)