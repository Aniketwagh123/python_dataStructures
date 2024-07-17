def convert_list_to_tuple(my_list):
    return tuple(my_list)


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    my_tuple = convert_list_to_tuple(my_list)
    print("Original List:", my_list)
    print("Converted Tuple:", my_tuple)
