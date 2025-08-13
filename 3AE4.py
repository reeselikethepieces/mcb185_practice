# E. coli genome is 4.6Mbp and you decide to do 5x random shotgun seqs with 100bp length
# reads. make a table with rows of seq depth (e.g. 5x) and columns of read coverage (0x,
# 1x, 2x, etc)

import random
import sys

genome_size = int(float(sys.argv[1]))
depth = int(sys.argv[2])
read_size = int(sys.argv[3])

reads_total = genome_size * depth // read_size

# initializing genome
genome = []
for _ in range(genome_size):
	genome.append(0)

# reads 
for _ in range(reads_total):
	starting_position = random.randint(0, genome_size - 1)
	
	for genome_position in range(starting_position, read_size - 1):
		genome[genome_position] += 1


