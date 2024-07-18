def print_dict_table(d):
    print(f"{'Key':<10} {'Value':<10}")
    for key, value in d.items():
        print(f"{key:<10} {value:<10}")


if __name__ == "__main__":
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print("Dictionary in table format:")
    print_dict_table(sample_dict)
