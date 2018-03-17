import sys

current_word, word = "", ""
count, current_count = 0, 0
for line in sys.stdin:
	word = line.strip()
	if current_word == word:
		current_count += 1
	else:
		if current_word:
			print(current_word, current_count, sep=",")
		current_word, current_count = word, 1

if current_word == word:
	print(current_word, current_count, sep=",")
