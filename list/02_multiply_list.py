def multiply_list(items):
    result = 1
    for item in items:
        result *= item
    return result


if __name__ == "__main__":
    print(multiply_list([1, 2, 3, 4, 5, 6]))
