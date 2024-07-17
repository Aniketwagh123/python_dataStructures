if __name__ == "__main__":
    my_dict = {1: 40, 2: 10, 3: 30, 4: 20}
    sorted_asc = {i: my_dict[i] for i in sorted(
        my_dict, key=lambda x: my_dict[x], reverse=False)}
    sorted_desc = {i: my_dict[i] for i in sorted(
        my_dict, key=lambda x: my_dict[x], reverse=True)}
    print("Sorted dictionary (ascending):", sorted_asc)
    print("Sorted dictionary (descending):", sorted_desc)
