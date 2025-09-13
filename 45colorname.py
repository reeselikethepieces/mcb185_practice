# write a program that provides the closest official color name given RGB values
	# 200, 0, 50 should output a shade of red
	# colors_basic.tsv and colors_extended.tsv are in MCB185/data

import sys
colorfile = sys.argv[1]
'''
R int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])
'''

# to test code with RGB = 200, 0 , 50

def euclidean(RGB, rgb):
	R, G, B = RGB
	r, g, b = rgb
	return ((R - r)**2 + (G - g)**2 + (B - b)**2)**0.5

RGB = (200, 0, 50) # to test
color = None
min_distance = None

with open(colorfile) as fp:
	for line in fp:
		columns = line.split()
		split_rgb_vals = columns[2].split(',')
		
		list_rgb_vals = []
		for val in split_rgb_vals:
			int_rgb_vals = int(val)
			list_rgb_vals.append(int_rgb_vals)
		
		rgb = tuple(list_rgb_vals)
		# next line is needed because floats cannot use comparison operators
		distance = round(euclidean(RGB, rgb))
		
		if distance < min_distance:
			min_distance = distance
			print(color = columns[0])



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