def set_difference(set1, set2):
    return set1.difference(set2)


if __name__ == "__main__":
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    difference_set = set_difference(set1, set2)
    print("Difference of sets:", difference_set)