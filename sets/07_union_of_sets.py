def union_of_sets(set1, set2):
    return set1.union(set2)

if __name__ == "__main__":
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    union_set = union_of_sets(set1, set2)
    print("Union of sets:", union_set)