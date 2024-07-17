def list_difference(list1, list2):
    return list(set(list1) - set(list2))


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    print(list_difference(list1, list2))
