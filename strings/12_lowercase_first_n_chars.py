def lowercase_first_n_chars(s, n):
    if n > len(s):
        return s.lower()
    return s[:n].lower() + s[n:]


if __name__ == "__main__":
    sample_string = "HELLO World"
    n = 5
    print("Modified string:", lowercase_first_n_chars(sample_string, n))
