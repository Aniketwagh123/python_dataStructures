def encode_string(text: str):
    if len(text) == 0:
        return ""
    for i in range(1, len(text)):
        if text[i] == text[0]:
            text= text[:i] + '$' + text[i+1:]
    return text


if __name__ == "__main__":
    str = "restart"
    encoded_string = encode_string(str)
    print(encoded_string)
