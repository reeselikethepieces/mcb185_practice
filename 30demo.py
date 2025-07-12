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



