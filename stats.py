def get_num_words(book):
	number_of_words = len(book.split())
	return number_of_words

def get_char_count(book):
    char = {}
    for ch in book.lower():
          if ch not in char:
                char[ch] = 0
          if ch in char:
                char[ch] += 1

    return char