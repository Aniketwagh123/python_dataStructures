def concatenate_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result


if __name__ == "__main__":
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    concatenated_dict = concatenate_dicts(dic1, dic2, dic3)
    print("Concatenated dictionary:", concatenated_dict)
