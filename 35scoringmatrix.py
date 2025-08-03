import sys

alpha = str(sys.argv[1])
mat = str(sys.argv[2])
mis = str(sys.argv[3])

print('   ', end='')

for letter in alpha:
	print(letter, end='  ')
print()

for letter1 in alpha:
	print(letter1, end=' ')
	for letter2 in alpha:
		if letter1 == letter2: print(mat, end=' ')
		else: print(mis, end=' ')
	print()
'''
problems with initial code below is:
	# row1 code block is a header and should be separate outside the loop
	the hard coding of range(5) makes it so the program will not work for all args

The code above was an alternative way to solve the problem without creating a list

for i in range(5):
	row = []
	
	# row 1
	if i == 0:
		# blank space
		row.append(' ')
		
		for letter in alpha:
			row.append(letter)
		
		print('  '.join(row))
		
	else:
		pairwise = alpha[i-1]
		row.append(pairwise + ' ')
		
		for letter in alpha:
			if letter == pairwise: row.append(str(mat))
			else:                  row.append(str(mis))
			
		print(' '.join(row))
'''