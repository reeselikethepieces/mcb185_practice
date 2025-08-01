import sys

alpha = str(sys.argv[1])
mat = int(sys.argv[2])
mis = int(sys.argv[3])

rows = []
for i in range(5):
	row = []
	
	# row 1
	if i == 0:
		# blank space
		row.append(' ')
		
		for letter in alpha:
			row.append(letter)
			
		str_row = []
		for val in row:
			str_row.append(str(val))
		
		print(' '.join(str_row))
	
	# row 2
		if i == 1:
		# nt 1
		row.append(alpha[0])
		
		for letter in alpha:
		
			