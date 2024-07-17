def slice_tuple(my_tuple, start, end):
    return my_tuple[start:end]

if __name__ == "__main__":
    my_tuple = (1, 2, 3, 4, 5)
    sliced_tuple = slice_tuple(my_tuple, 1, 4)
    print("Original Tuple:", my_tuple)
    print("Sliced Tuple:", sliced_tuple)