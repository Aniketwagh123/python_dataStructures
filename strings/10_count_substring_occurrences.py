def count_substring_occurrences(s, sub):
    if len(sub) > len(s):
        return 0
    count = 0
    start = 0
    end = len(sub)

    while end <= len(s):
        if s[start:end] == sub:
            count += 1
        start += 1
        end += 1

    return count


if __name__ == "__main__":
    main_string = "hello world, welcome to the world of Python"
    substring = "world"
    print(f"Occurrences of '{substring}':",
          count_substring_occurrences(main_string, substring))
