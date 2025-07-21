# adding more while loop examples
	# two types of while loops: `while True` and `while`
	# the first returns a value, endlessly, until 'break'
	# the second returns boolean T/F, and will end based on a provided condition
# `while True` - writing lines A and B would make an infinite loop
# adding the other lines in this code block confines the repeats
repeats = 0
# line A
while True:
# line B
	print('Loopdee loop')
	repeats += 1	
	if repeats >= 5:
		break		
# while False - we don't use. Why? see print statement
while False:
	print('this will print')
# `while` some condition 
	
# side by side 
limit = 12
for i in range(limit):
	print(i)
	
s = 'ABCDEFGHIJ'
print(s[0:8:2])