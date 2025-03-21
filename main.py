from stats import wordcount
from stats import charcount
from stats import sorterreporter
import sys

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
		wordcount(file_contents)	

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	sorterreporter(sys.argv[1])

main()
