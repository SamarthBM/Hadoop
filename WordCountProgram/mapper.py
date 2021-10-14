
# sys is required to read and write data to STDIN and STDOUT
import sys

# reading entire line from STDIN (standard input)
for line in sys.stdin:
	# to remove whitespace
	line = line.strip()
	# split the line into words
	words = line.split() #['The', 'Apache'......]

	# Iterating to every words in list
	for word in words:
	# Printing the key value pairs.
	# Key is word and value is count which is always 1.
		print ('%s\t%s' % (word, 1))
