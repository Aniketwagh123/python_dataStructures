def split_by_first_character(words):
    result = {}
    for word in words:
        key = word[0]
        if key in result:
            result[key].append(word)
        else:
            result[key] = [word]
    return result


if __name__ == "__main__":
    words = ['bluebeary', 'avocado', 'apple',
             'banana', 'orange', 'grape', 'kiwi']
    print(split_by_first_character(words))
