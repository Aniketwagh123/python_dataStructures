def longest_word_length(word_list):
    max_length = 0
    for word in word_list:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

if __name__ == "__main__":
    word_list = ['my', 'name', 'is', 'aniket', 'wagh']
    max_length = longest_word_length(word_list)
    print(max_length)
