# INCOMPLETE

# E. coli genome is 4.6Mbp and you decide to do 5x random shotgun seqs with 100bp length
# reads. make a table with rows of seq depth (e.g. 5x) and columns of read coverage (0x,
# 1x, 2x, etc)

import random
import sys

#random.seed(5)

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

hits = [0] * max_depth
for cov in (genome[read_size: -read_size]):
	if cov >= max_depth: continue
	hits[cov] += 1

for c, d in enumerate(hits):
	print(d/(genome_size*depth))
	


'''
# below is too big for google sheets
# alternatively, I thought about going through the appended lists and pooling like-vals
# i.e. pulling all of the '1's, 2's etc. --> similar to ..WAIT
no_covrg_counts = []
coverage_counts = []

for position, coverage in enumerate(genome):
	if coverage != 0:
		coverage_counts.append(coverage)
	else:
		no_covrg_counts.append(position)


content = '\n'.join(str(x) for x in coverage_counts)






# for all:

no_covrg_counts = []
coverage_counts = []
coverage_position = []

for position, coverage in enumerate(genome):
	if coverage != 0:
		coverage_counts.append(coverage)
		coverage_position.append(position)
	else:
		no_covrg_counts.append(position)


# https://www.youtube.com/watch?v=0zrygaLGxuM

textfile = open('/Users/pieces/Code/coverage_counts.txt', 'w')

# copilot help
content = '\n'.join(str(x) for x in coverage_counts)

textfile.writelines(content)
textfile.close()
'''