import sys

alpha = str(sys.argv[1])
mat = str(sys.argv[2])
mis = str(sys.argv[3])

for i in range(5):
	row = []
	
	# row 1
	if i == 0:
		# blank space
		row.append(' ')
		
		for letter in alpha:
			row.append(letter)
		
		print('   '.join(row))
		
	else:
		pairwise = alpha[i-1]
		row.append(pairwise)
		
		for letter in alpha:
			if letter == pairwise: row.append(str(mat))
			else:                  row.append(str(mis))
			
		print('  '.join(row))