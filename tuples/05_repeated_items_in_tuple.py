def find_repeated_items(my_tuple):
    repeated_items = []
    for item in my_tuple:
        if my_tuple.count(item) > 1 and item not in repeated_items:
            repeated_items.append(item)
    return repeated_items


if __name__ == "__main__":
    my_tuple = (1, 2, 3, 2, 4, 5, 2)
    repeated = find_repeated_items(my_tuple)
    print("Tuple:", my_tuple)
    print("Repeated items:", repeated)
