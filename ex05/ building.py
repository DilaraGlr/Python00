import sys
import string


def analyze_text(text):
    """
    Affiche le nombre de majuscules, minuscules, ponctuation,
    espaces et chiffres contenus dans la chaîne de caractères fournie.
    """

    if len(sys.argv) == 1 and text:
        text += '\n'
    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0
    digit_count = 0
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char in string.punctuation:
            punctuation_count += 1

    len_text = len(text)
    print(f"The text contains {len_text} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    if len(sys.argv) > 2:
        assert False, "more than one argument is provided"
        sys.exit(1)
    text = ""
    if len(sys.argv) == 1:
        text = input("What is the text to count?\n")
    elif len(sys.argv) == 2:
        text = sys.argv[1]
    analyze_text(text)


if __name__ == "__main__":
    main()
