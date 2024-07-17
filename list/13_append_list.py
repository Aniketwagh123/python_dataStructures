def append_list(list1, list2):
    list2.extend(list1)
    return list2


if __name__ == "__main__":
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print(append_list(list1, list2))
