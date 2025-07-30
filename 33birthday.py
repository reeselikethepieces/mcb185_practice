# 33birthday.py 

# write a prog that simulates filling a class of students
# each student has a random birthday
# number of days and number of students need to be CL arguments
# use a list for birthdays

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
students = int(sys.argv[3])

# do not put 'shared' inside the loop bc it will reset each trial to '0'
shared = 0
for _ in range(trials):
	bdays = []
	for i in range(students):
		bday = random.randint(0, days-1)
		if bday in bdays:
			shared += 1
			break
		bdays.append(bday)ß		

print(f'{shared/trials}')

'''
CL: python3 33birthday.py 10000 365 23
'''