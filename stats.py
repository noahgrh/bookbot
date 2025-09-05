def get_num_words(file_contents):
    words = file_contents.split()
    return len(words)

def get_stats(file_contents):
    word_count = {}
    words = file_contents.lower().split()
    for word in words:
        for letter in word:
            if letter not in word_count:
                word_count[letter] = 0
            word_count[letter] += 1
    return word_count

def sort_on(items):
    return items["num"]

def get_sorted_dictionary(dictionary):
    dict_entries = []
    for x in dictionary:
        dict_entries.append({"char": x, "num": dictionary[x]})
    dict_entries.sort(reverse=True, key=sort_on)
    return dict_entries
