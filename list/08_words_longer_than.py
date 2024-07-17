def words_longer_than(words, n):
    return [word for word in words if len(word) > n]


if __name__ == "__main__":
    words = ['Aniket', 'Wagh', 'orange', 'grape', 'kiwi']
    n = 4
    print(words_longer_than(words, n))
