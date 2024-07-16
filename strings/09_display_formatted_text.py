import textwrap


def display_formatted_text(text, width=50):
    count = 0
    for _ in range(len(text)):
        count += 1
        if count % width == 0:
            text = text[:count]+'\n'+text[count:]

    print(text)


if __name__ == "__main__":
    sample_text = "This is a sample text that will be formatted to a specified width for display purposes."
    display_formatted_text(sample_text)
