def check_element_in_tuple(my_tuple, element):
    return element in my_tuple


if __name__ == "__main__":
    my_tuple = (1, 2, 3, 4, 5)
    element = 3
    if check_element_in_tuple(my_tuple, element):
        print(f"Element {element} exists in tuple.")
    else:
        print(f"Element {element} does not exist in tuple.")
