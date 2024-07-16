def unique_sorted_words():
    words = input("Enter a comma-separated sequence of words: ").split(',')
    unique_words = sorted(set(words))
    print("Unique sorted words:", ', '.join(unique_words))

if __name__ == "__main__":
    unique_sorted_words()