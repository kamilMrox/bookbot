char = {}
def get_num_words(text):
	number_of_words = len(text.split())
	return number_of_words

def get_chars_dict(text):
    for ch in text.lower():
          if ch not in char:
                char[ch] = 0
          if ch in char:
                char[ch] += 1
    return char

def sort_on(d):
      return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
      sorted_list = []
      for ch in num_chars_dict:
            sorted_list.append({"char": ch, "num":num_chars_dict[ch]})
      sorted_list.sort(reverse=True, key=sort_on)
      return sorted_list

