# similar to the 33birthday.py problem but instead of bdays = [], calendar = []
# previously, bdays was appended to a list, this time:
	# all possible days are already in a list so assigning a birthday is:
		# calendar[birthday] += 1
# another way to think of this problem is throwing darts at a calendar
	# a shared birthday is when a dart hits 

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
students = int(sys.argv[3])

shared = 0
for _ in range(trials):
	
	calendar = []
	for _ in range(days):
		calendar.append(0)     # need to have a full "blank" calendar
	
	for _ in range(students):
		bday = random.randint(0, days-1)
		calendar[bday] += 1
		
		if calendar[bday] == 2:
			shared += 1
			break

print(f'{shared/trials}')