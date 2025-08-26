# most data is stored in files
	# to read data, you must (1) open file (2) stream data from it (3) close when done

'''
fp = open(path)
for line in fp:
	do_something_with(line)
fp.close()
'''

# line 5 uses the open() function which creates a new variable, 'file pointer'
	# open() takes a "path" as an argument (relative or absolute)
	
# a common error is forgetting to close (line 8)
	# alternative way below using 'with'

'''
with open(path) as fp:
	for line in fp:
		do_something_with(line)
'''
		
		
# compressed files - similar to the above with minor changes
	# import gzip and changing open(path) to gzip.open(path, 'rt')
	# essentially s/s as gunzip -c path on CL

'''
import gzip
with gzip.open(path, 'rt') as fp:
	for line in fp:
		print(line, end='')
'''