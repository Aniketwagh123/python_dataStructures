def add_members_to_set(my_set, members):
    my_set.update(members)
    return my_set


if __name__ == "__main__":
    my_set = {1, 2, 3}
    new_members = {4, 5}
    updated_set = add_members_to_set(my_set, new_members)
    print("Updated Set:", updated_set)