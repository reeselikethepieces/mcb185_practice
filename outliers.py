# doesn't work - come back to another time

# outliers - redo this for various file types instead of CL input

# write a program that removes outliers from a set of data with the following criteria:
	# must show calculation of Q1, Q3, and IQR


# CL input: 27, 2, 22, 29, 19, 30, 32, 59, 52, 35
import argparse
import math

def rounding_decimals(x):
	before = int(x)
	after  = x - before
	if after >= 0.5: return math.ceil(x)
	else:            return math.floor(x)

parser = argparse.ArgumentParser()
parser.add_argument("data", nargs="+", type=int)
args = parser.parse_args()
data = args.data
data.sort()

# Locator value
sample_size = len(data)
L25 = rounding_decimals(25/100 * sample_size)
L75 = rounding_decimals(75/100 * sample_size)

# quartiles and InterQuartile Range
first_quartile = data[L25]
third_quartile = data[L75]
IQR = third_quartile - first_quartile

# positions to exclude
lower_bound = first_quartile - (1.5 * IQR)
upper_bound = third_quartile + (1.5 * IQR)

filtered_data = []
for val in data:
	if lower_bound <= val and upper_bound >= val:
		filtered_data.append(val)

print(f'Q1: {first_quartile}, Q3: {third_quartile}, IQR: {IQR}')
print(f'data without outliers: {filtered_data}')