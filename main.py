
def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	num_words = get_num_words(text)
	print(f"Found {num_words} total words")


def get_book_text(path):
	with open(path) as f:
		return f.read()
	
def get_num_words(book):
	number_of_words = len(book.split())
	return number_of_words


main()
