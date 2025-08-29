# an example of 'unit tests' and 'integration tests'
	# where the test calls library functions with various arguments

import sequence

print(sequence.transcribe('ACGT'))
print(sequence.revcomp('AAACGT'))
print(sequence.translate('ATGCCCTAA'))

# calling for `43skew.py`
s = 'ACGTGGGGGGCATATG'
print(sequence.gc_comp(s))
print(sequence.gc_skew(s), sequence.gc_skew(sequence.revcomp(s)))