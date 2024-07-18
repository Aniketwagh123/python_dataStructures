import array as arr


def count_occurrences(array, element):
    return array.count(element)


if __name__ == "__main__":
    int_array = arr.array('i', [1, 2, 3, 2, 5, 2])
    element_to_count = 2
    occurrences = count_occurrences(int_array, element_to_count)
    print(f"Number of occurrences of {element_to_count}:", occurrences)
