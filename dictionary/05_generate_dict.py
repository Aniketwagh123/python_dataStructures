def generate_dict(n):
    return {x: x*x for x in range(1, n+1)}

if __name__ == "__main__":
    n = 5
    generated_dict = generate_dict(n)
    print("Generated dictionary:", generated_dict)