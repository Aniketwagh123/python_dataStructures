def count_items_in_list_value(d, key):
    if key in d:
        if type(d[key]) == list:
            return len(d[key])
        else:
            return 1
    else:
        return 0


if __name__ == "__main__":
    sample_dict = {'a': [1, 2, 3], 'b': [4, 5], 'c': 6}
    key_to_check = 'a'
    count = count_items_in_list_value(sample_dict, key_to_check)
    print(f"Number of items in the list for key '{key_to_check}':", count)
