# write a program that provides the closest official color name given RGB values
	# 200, 0, 50 should output a shade of red
	# colors_basic.tsv and colors_extended.tsv are in MCB185/data

import sys
colorfile = sys.argv[1]
'''
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])
'''

# to test code 
R1 = 200
G1 = 0
B1 = 50
R2 = 0
G2 = 0
B2 = 0
input_color = (R1, G1, B1)
rgb = (R2, G2, B2)

def euclidean(RGB, rgb):
	return ((R1 - R2)**2 + (G1 - G2)**2 + (B1 - B2)**2)**0.5

with open(colorfile) as fp:
	for line in fp:
		columns = line.split()
		split_rgb_vals = columns[2].split(',')
		
		#list_rgb_vals = []
		for rgb in split_rgb_vals:
			int_rgb_vals = int(rgb)
		#	list_rgb_vals.append(int_rgb_vals)
	#	print(list_rgb_vals)
			euclidean(input_color, int_rgb_vals)
			print(columns[0])
		
		
			
		
			
			


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
after soft linking: ln -s ~/Code/MCB185/data/colors_extended.tsv ./colors
CL input: python3 45colorname.py colors 200 0 50
'''