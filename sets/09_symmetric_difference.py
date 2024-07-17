def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

if __name__ == "__main__":
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    symmetric_difference_set = symmetric_difference(set1, set2)
    print("Symmetric difference of sets:", symmetric_difference_set)