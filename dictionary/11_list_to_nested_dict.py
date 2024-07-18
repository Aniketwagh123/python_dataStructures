def list_to_nested_dict(lst):
    nested_dict = current = {}
    for item in lst:
        current[item] = {}
        current = current[item]
    return nested_dict


if __name__ == "__main__":
    sample_list = [1, 2, 3, 4]
    nested_dict = list_to_nested_dict(sample_list)
    print("Nested dictionary:", nested_dict)
