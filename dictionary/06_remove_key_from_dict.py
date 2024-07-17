def remove_key_from_dict(d, key):
    if key in d:
        del d[key]
    return d

if __name__ == "__main__":
    sample_dict = {1: 10, 2: 20, 3: 30}
    key_to_remove = 2
    updated_dict = remove_key_from_dict(sample_dict, key_to_remove)
    print("Dictionary after removing key:", updated_dict)