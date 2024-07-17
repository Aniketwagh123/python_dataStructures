def sort_by_last(tuples):
    return sorted(tuples, key=lambda x: x[-1])


if __name__ == "__main__":
    tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(sort_by_last(tuples))
