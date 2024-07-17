def intersection_of_sets(set1, set2):
    return set1.intersection(set2)


if __name__ == "__main__":
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    intersected_set = intersection_of_sets(set1, set2)
    print("Intersection of sets:", intersected_set)
