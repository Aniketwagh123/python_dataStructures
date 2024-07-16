def last_part_before_char(s, char):
    for i in range(len(s)-1, -1, -1):
        if s[i] == char:
            return s[:i]

    return s


if __name__ == "__main__":
    test_string = "https://www.w3resource.com/python-exercises"
    specified_char = '-'
    print("Result:", last_part_before_char(test_string, specified_char))