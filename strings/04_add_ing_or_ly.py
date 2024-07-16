def add_ing_or_ly(text: str):
    if len(text) < 3:
        return text
    elif text[len(text)-3:] == 'ing':
        return text + 'ly'
    else:
        return text+'ing'


if __name__ == "__main__":
    str = "re"
    new_str = add_ing_or_ly(str)
    print(new_str)
