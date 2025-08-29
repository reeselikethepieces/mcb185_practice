# E. coli genome is 4.6Mbp and you decide to do 5x random shotgun seqs with 100bp len read
# make a table with rows of seq depth (e.g. 5x) and columns of read cov (0, 1, 2..)

import random
import sys


genome_size = int(float(sys.argv[1]))
depth = int(sys.argv[2])
read_size = int(sys.argv[3])
max_depth = int(sys.argv[4])

reads_total = genome_size * depth // read_size

# initializing genome
genome = [0] * genome_size

# reads
for _ in range(reads_total):
	starting_position = random.randint(0, genome_size - read_size)

	for genome_position in range(starting_position, starting_position + read_size):
		genome[genome_position] += 1

# alignment
hits = [0] * max_depth
for cov in (genome[read_size: -read_size]):
	if cov >= max_depth: continue
	hits[cov] += 1

# output
for c, d in enumerate(hits):
	print(d/genome_size)