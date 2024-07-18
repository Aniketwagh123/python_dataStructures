import array as arr


def remove_first_occurrence(array, element):
    try:
        array.remove(element)
    except ValueError:
        pass


if __name__ == "__main__":
    int_array = arr.array('i', [1, 2, 3, 2, 5])
    element_to_remove = 2
    remove_first_occurrence(int_array, element_to_remove)
    print("Array after removing first occurrence of",
          element_to_remove, ":", int_array)
