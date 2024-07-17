def remove_duplicates(items):
    return list(set(items))


if __name__ == "__main__":
    items = [1, 2, 2, 3, 4, 4, 5]
    print(remove_duplicates(items))
