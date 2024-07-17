def remove_duplicates(list_of_lists):
    seen = []
    result = []
    for sublist in list_of_lists:
        if sublist not in seen:
            seen.append(sublist)
            result.append(sublist)
    return result


if __name__ == "__main__":
    list_of_lists = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    new_list = remove_duplicates(list_of_lists)
    print("Original List:", list_of_lists)
    print("New List:", new_list)
