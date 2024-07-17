def remove_items_from_set(my_set, items):
    my_set.difference_update(items)
    return my_set


if __name__ == "__main__":
    my_set = {1, 2, 3, 4, 5}
    items_to_remove = {2, 3}
    updated_set = remove_items_from_set(my_set, items_to_remove)
    print("Updated Set after removal:", updated_set)