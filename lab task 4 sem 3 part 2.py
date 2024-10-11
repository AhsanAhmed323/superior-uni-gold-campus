import string

def remove_punctuation(input_string):
    """Remove punctuation from the input string."""
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    cleaned_string = remove_punctuation(user_input)
    print(f"String without punctuation: {cleaned_string}")