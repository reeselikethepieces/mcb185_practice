# extra assessments

# (1) Add the N50 calculation to your stats program --> seen in 3AE.py

# (2) Make a function called inside() that mimics the in keyword
def inside(thing, container):
	for item in container:
		if item == thing:
			return True
	return False