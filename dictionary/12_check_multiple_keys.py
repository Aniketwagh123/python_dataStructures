def check_multiple_keys(d, keys):
    return all(key in d for key in keys)


if __name__ == "__main__":
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    keys_to_check = ['a', 'b', 'd']
    result = check_multiple_keys(sample_dict, keys_to_check)
    print("All keys exist:", result)
