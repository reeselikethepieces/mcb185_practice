# extra assessments

# (1) Add the N50 calculation to your stats program --> seen in 3AE.py

# (2) Make a function called inside() that mimics the in keyword
def inside(thing, container):
	for item in container:
		if item == thing:
			return True
	return False

# (3) Simulate shotgun sequencing (described below).
	# Given a genome of 4.6Mbp (E. coli), you decide to do 5x random shotgun sequencing
	# with reads that are 100 bp long. Of course, the result will not be 5x everywhere. 
	# Some places will be higher or lower. Some areas of the genome may not even be hit.

	# Make a table with rows of sequencing depth  (e.g 5x) and columns of read coverage 
		# (0x, 1, x2, etc). Do this for several sequencing depths (i.e. not just 5x) 
		# and a bunch of coverages. Put those in a spreadsheet and graph them. The usual
		# assessment question is just 5x and 0x without a graph, but if you can do that, 
		# you can do the full assignment described here. Also, I think the graph has 
		# great educational value.

import random
import sys 

# inputs 
trials = int(sys.argv[1]) 
genome_size = int(float(sys.argv[2])) # 4.6E7
coverage_intent = int(sys.argv[3]) # 5 x
read_l = int(sys.argv[4]) # 100 bp

# total reads
total_reads = genome_size * coverage_intent // read_l

for t in range(trials):

	# initialize empty list 
	hit = []
	for _ in range(genome_size):
		hit.append(0)
		
	# per base coverage
	for _ in range(total_reads):
		ref_read = random.randint(0, genome_size - read_l)
		
		for b_pos in range(ref_read, ref_read + read_l):
			hit[b_pos] += 1
			
	max_depth = max(hit)
	rcov_base = []
	for _ in range(max_depth +1):
		rcov_base.append(0)
		
	for h in hit:
		rcov_base[h] += 1

print("Cov\tbases")
for depth in range(len(rcov_base)):
	print(f'{depth}\t{rcov_base[depth]}')
	
	
# results = high, low, none
# output = table: rows[seq depth], columns[read_cover] --> dump into spreadsheet, graph