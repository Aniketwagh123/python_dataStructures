def remove_item_if_present(my_set, item):
    my_set.discard(item)
    return my_set


if __name__ == "__main__":
    my_set = {1, 2, 3, 4, 5}
    item_to_remove = 3
    updated_set = remove_item_if_present(my_set, item_to_remove)
    print("Updated Set after conditional removal:", updated_set)