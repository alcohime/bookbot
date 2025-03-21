def wordcount(text):
	with open(text) as file:
		file_contents = file.read()
		print(f'Found {len(file_contents.split())} total words')

def charcount(text):
	charcount = []
	finalized = {}
	with open(text) as file:
		document = file.read()
		document = document.lower()
		document = document.split()
		for i in document:
			for char in list(i):
				charcount.append(char)
		for letter in charcount:
			if letter in finalized:
				finalized[letter] += 1
			else:
				finalized[letter] = 1		
	return finalized

def sorterreporter(text):
	final = charcount(text)
	sortedlist = {}
	wordadded = False
	for i in range(0, 9999):
		maxword = None
		wordadded = False
		maxsofar = float("-inf")	
		for word in final:
			if final[word] > maxsofar and word.isalpha() == True:
				maxword = word
				maxsofar = final[word]
				wordadded = True
		if wordadded == True:
			sortedlist[maxword] = maxsofar
			del final[maxword]		
		else:
			break
	print("============ BOOKBOT ============")
	print(f'Analyzing book found at {text}...')
	print("----------- Word Count ----------")
	wordcount(text)
	print("--------- Character Count -------")
	for key in sortedlist:
		print(f'{key}: {sortedlist[key]}')
	print("============= END ===============")
