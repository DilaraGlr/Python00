from sys import argv


def get_morse_code():
    """Retourne le dictionnaire de correspondance pour le code Morse."""
    MORSE_CODE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. "
    }
    return MORSE_CODE


def convert(s, dico):
    """Convertit une chaîne en majuscules en code Morse
    en utilisant le dictionnaire fourni."""
    res = ""
    for c in s:
        res += dico[c]
    return res


def main():
    """Programme principal pour encoder
    une chaîne de caractères en code Morse."""
    try:
        assert len(argv) == 2, "the arguments are bad"
        S = argv[1].upper()
        MORSE_DICT = get_morse_code()
        assert all(char in MORSE_DICT for char in S), "the arguments are bad"
        print(convert(S, MORSE_DICT).rstrip())

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == '__main__':
    main()
