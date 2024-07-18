def dict_from_string(s):
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1
    return result


if __name__ == "__main__":
    sample_string = "w3resource"
    result_dict = dict_from_string(sample_string)
    print("Dictionary from string:", result_dict)
