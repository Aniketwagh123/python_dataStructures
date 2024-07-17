def unique_values(lst):
    unique_vals = set()
    for d in lst:
        for value in d.values():
            unique_vals.add(value)
    return unique_vals

if __name__ == "__main__":
    sample_data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
                   {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
    unique_vals = unique_values(sample_data)
    print("Unique values:", unique_vals)