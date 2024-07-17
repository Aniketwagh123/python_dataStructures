def permutations(input_list):
    result = []
    permutations_helper(input_list, 0, result)
    return result


def permutations_helper(input_list, start, result):
    if start == len(input_list):
        result.append(input_list.copy())
    else:
        for i in range(start, len(input_list)):
            input_list[start], input_list[i] = input_list[i], input_list[start]

            permutations_helper(input_list, start + 1, result)

            input_list[start], input_list[i] = input_list[i], input_list[start]


if __name__ == "__main__":
    input_list = [1, 2, 3]
    print(f"Generating permutations of list: {input_list}")
    permutations = permutations(input_list)
    for perm in permutations:
        print(perm)
