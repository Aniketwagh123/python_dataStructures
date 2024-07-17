def find_max_min(my_set):
    return max(my_set), min(my_set)


if __name__ == "__main__":
    my_set = {1, 2, 3, 4, 5}
    max_value, min_value = find_max_min(my_set)
    print("Maximum value in the set:", max_value)
    print("Minimum value in the set:", min_value)
