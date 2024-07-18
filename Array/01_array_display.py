import array as arr

if __name__ == "__main__":
    int_array = arr.array('i', [1, 2, 3, 4, 5])
    print("Array items:")
    for item in int_array:
        print(item)
    print("Accessing individual elements:")
    for i in range(len(int_array)):
        print(f"Element at index {i}: {int_array[i]}")
