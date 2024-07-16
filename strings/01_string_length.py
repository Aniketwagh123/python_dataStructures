def get_length(text:str):
    # return len(text)
    length:int = 0
    for _ in text:
        length+=1
    return length

if __name__ == "__main__":
    str = "Aniket wagh"
    length = get_length(str)
    print(f'length of string \'{str}\' is : {length}')