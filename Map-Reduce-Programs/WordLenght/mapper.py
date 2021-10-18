import sys

# reading entire line from STDIN (standard input)
for line in sys.stdin:
	# to remove all  whitespaces
	line = line.strip()

	# split the line into words
	# words will be stored in list
	words = line.split()

	# use for loop to iterate all words in list
	for word in words:
		# creating key value pair for each word
		print ('%s\t%s' % (len(word), 1))
