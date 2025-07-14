# 30demo.py by Reese

# strings = [containers that hold: letters, numbers, punctuation, and other symbols]
s1 = 'hello world'
print(s1)

# strings w/ quotations
s1 = 'strings "look"'                   # single quotes outside of double quotes
s2 = "like they're quotes"              # double quotes outside of single quote
s3 = 'they p\'much are'                 # backslash in front of special character

print(s1, s2)                           # will print on one line WITH a space b/w strings
print(s3)

# backslash flashback
	# \' tells python the single quote is not a delimiter
	# \n tells python newline character
	# \t tells python horizontal tab
	
space =  '\nmake some room\n'
print(space)

s1 = "5'"
s2 = '-' * 6
s3 = "3'"
print(s1 + s2, end='')

repeats = 5
for i in range(1, repeats):
	if i == 1: s4 = '|ex'
	else:      s4 = 'ex'
	s5 = 'in'
	print (s4, i, end='|')
	print (s5, i, end='|')
	
s6 = 'splicing'
print(s2 + s3, s6, sep='\n\t\t')

print(s1 + s2, end='')
repeat = 5
for i in range(1, repeat):
	if i == 1: s4 = '|ex'
	else:      s4 = 'ex'
	print(s4, i, end='|')

print(s2 + s3)

# comparison operators work like ints except strings are compared by ASCII

# string functions
	# len(s) - length of string
	# chr(n) - gets character whose ASCII value is n
	# ord(c) - gets ASCII value of character c
	
# method syntax
	# everything thus far has been "function syntax" 
		# function(string) shows function first the variable type (string)
		# string.method    shows the variable type (string) first then the method
	# IP1: python strings are immutable (can't change them) 
	
s = 'hello world'
print(s.upper())   # IP1: s is not converted into CAPS, it's a new copy that is in CAPS
print(s.replace('o', ''))
print(s.replace('o', '').replace('r','i'))

print(s.count('o'))

print(s.endswith('world'))
print(s.endswith('hell'))
print(s.startswith('world'))
print(s.startswith('hell'))
print(s.strip('hell'))
print(s.strip('world'))

# string formatting
	# str.format() - older method\
	# printf-style - looks more like print() from C
	# f-strings - modern/best
		# f'{code}'
			# code is interpolated, live: variables = expanded; fxns = called
			# f for fixed point (default = 6)
			# e for exponent notation
			# < ^ > left, center, or right justify
import math 
# f-string
print(f'{math.pi}')
print(f'{math.pi:.3f}')       # 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}')   # exponent notation
print(f'{"hello world":>20}') # right justify with space filler
print(f'{"hello world":.20}') # right justify with dot filler
print(f'{20:<10} {10}')       # left justify

# str.format()
print('{} {:.3f}'.format('str.format', math.pi))
	# here, `str.format` goes into empty {} 
	# pi goes into second set with precision of 3

# printf-style
print('%s %.3f' % ('printf', math.pi))
	# to the left of the isolated modulo = 'string'
	# to the right of the isolated modulo = tuple()
	# %s simply means string and %.3f still refers to digit precision 


# indexes
	# every char in string has an index (position)

seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

for nt in seq:
	print(nt, end='')   # each iteration prints on one line (horizontally)
#	print(nt)           # each iteration prints line by line (vertically)
print()                 # newline?

for i in range(len(seq)):
	print(i, seq[i])


# slices
	# subset of a container
	# slice operator = [initial position:end-before limit:step size]

s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])
print(s[0:5], s[:5])             # (same, same)
print(s[5:len(s)], s[5:])        # (same, same)
print(s, s[::], s[::1], s[::-1]) # (same. same, same, emas)

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
	codon = dna[i:i+3]
	print(i, codon)


# tuples
	# are container that holds multiple values
	
tax = ('Homo', 'sapiens', 9606)  # construct tuple
print(tax)                       # note the () in the output

# tuples are immutable (!= contents via indices)
# next two lines return errors
'''
s[0] = 'C'
tax[0] = 'human'
'''
# next two lines show how tuples can be indexed and sliced like strings
print(tax[0])
print(tax[::-1])


# enumerate() and zip()
# stepping through containers, often useful to have both indices and values
nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])
# alternatively: enumerate() 
for i, nt in enumerate(nts):
	print(i, nt)
	
# stepping through containers in parallel
nts = 'ACGT'
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])
# zip()
for nt, name in zip(nts, names):
	print(nt, name)
	
# enumerate the zip
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)


# lists
	# similar to tuples, but have [] and ARE MUTABLE

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

# mk elements
nts.append('C')
print(nts)

# rm elements
last = nts.pop()
print(last)

# sorted with `list.sort()` --> only works w/ mix of ints and floats, but not mix with str
nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

# if a new variable is added to an existing list, OG list is 1 name, other name is 2 name
nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)    # (same, same)

# make a copy
	# `list.copy()` = "shallow" copy = xdim []s + complex data strc not fully copied

# list()
	# empty creates empty lists
	
items = list()
print(items)
items.append('eggs')
print(items)

# as a fxn, coerces other 'iterables' into lists
# i.e. conver string into list of letters

alph = 'ABCDEFGHIJKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)

# alternatively, create empty list by assigning a variable to []
stuff = []
stuff.append(3)
print(stuff)

# split() and join()

# splits into lists of strings
text = 'good day                  to you'
words = text.split()                         # useful for segmenting words, delimiter=' '
print(words)

# TSV CSV data, split on \t or comma
line = '1.41,2.72,3.14'
print(line.split(','))

# list --> string via delimiter-joining
s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)


# searching for items in containers: `in`, `find()`, `index()`

# `in` reads well with conditional statements
if 'A' in alph: print('yay')
if 'a' in alph: print('no')

# `index()` method, if !find, print fxn throws error
print('index G?', alph.index('G'))
#print('index Z?', alph.index('Z'))

# `find()` method, if !find, print fxn returns '-1' ~~~> oNlY StRiNgS
print('index G?', alph.find('G'))
print('index Z?', alph.find('Z'))

# for tuples and lists, if you're not sure !find or not, use `in`
	# i.e.	if thing in list: idx = list.index(thing)