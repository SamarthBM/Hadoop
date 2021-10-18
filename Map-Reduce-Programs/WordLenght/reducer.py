import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
	# remove all whitespaces
	line = line.strip()

	# slpiting the data on the basis of tab we have provided in mapper.py
	word, count = line.split('\t', 1)

	# convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError:
		continue

	if current_word == word:
		current_count += count
	else:
		if current_word:
			# write result to STDOUT
			print ('%s\t%s' % (current_word, current_count))
		current_count = count
		current_word = word

# do not forget to output the last word if needed!
if current_word == word:
	print ('%s\t%s' % (current_word, current_count))
