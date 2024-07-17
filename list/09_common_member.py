def common_member(list1, list2):
    return len(set(list1) & set(list2)) > 0


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    print(common_member(list1, list2))
