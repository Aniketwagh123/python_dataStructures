def clone_list(items):
    return items[:]


if __name__ == "__main__":
    items = [1, 2, 3, 4, 5]
    cloned_list = clone_list(items)
    print(cloned_list)
