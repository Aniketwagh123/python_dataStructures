def tuple_clone(my_tuple):
    return my_tuple[:]


if __name__ == "__main__":
    original_tuple = (1, 2, 3, 4, 5)
    cloned_tuple = tuple_clone(original_tuple)
    print("Original Tuple:", original_tuple)
    print("Cloned Tuple:", cloned_tuple)
