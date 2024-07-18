def count_values_by_key(data, key):
    return sum(1 for item in data if item.get(key) == True)


if __name__ == "__main__":
    sample_data = [{'id': 1, 'success': True, 'name': 'Lary'},
                   {'id': 2, 'success': False, 'name': 'Rabi'},
                   {'id': 3, 'success': True, 'name': 'Alex'}]
    key_to_check = 'success'
    count = count_values_by_key(sample_data, key_to_check)
    print(
        f"Count of how many dictionaries have {key_to_check} as True:", count)
