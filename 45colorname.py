# write a program that provides the closest official color name given RGB values
	# 200, 0, 50 should output a shade of red
	# colors_basic.tsv and colors_extended.tsv are in MCB185/data

import sys
colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

# PICK UP HERE and draw out to confirm/deny conceptual thought below
'''
conceptually:
input 3 values (CL inputs),
	--> distance conditionals to align closest color name to 3 inputs
	--> if 3 values = column 3 in file
		or if 3 values are ~ values in column 3
		 return column 1 
output 1 value (color name)
'''

'''
CL input: python3 45colorname.py ~/Code/MCB185/data/colors_extended.tsv 200 0 50
'''