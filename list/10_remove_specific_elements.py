def remove_specific_elements(items):
    return [item for i, item in enumerate(items) if i not in [0, 4, 5]]


if __name__ == "__main__":
    items = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    print(remove_specific_elements(items))
