def add_key_to_dict(d, key, value):
    d[key] = value
    return d


if __name__ == "__main__":
    sample_dict = {0: 10, 1: 20}
    print("sample dictionary:", sample_dict)
    new_key = 2
    new_value = 30
    sample_dict[new_key] = new_value
    print("Updated dictionary:", sample_dict)
