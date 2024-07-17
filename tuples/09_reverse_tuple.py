def reverse_tuple(my_tuple):
    return my_tuple[::-1]


if __name__ == "__main__":
    my_tuple = (1, 2, 3, 4, 5)
    reversed_tuple = reverse_tuple(my_tuple)
    print("Original Tuple:", my_tuple)
    print("Reversed Tuple:", reversed_tuple)
