def circularly_identical(list1, list2):
    return len(list1) == len(list2) and ''.join(map(str, list1 * 2)).find(''.join(map(str, list2))) != -1


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 1, 2, 3]
    print(circularly_identical(list1, list2))
