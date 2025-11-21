import sys
from ft_filter import ft_filter


def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert sys.argv[2].isdigit(), "the arguments are bad"
        N = int(sys.argv[2])
        liste = sys.argv[1].split()
        result = ft_filter(lambda mot: len(mot) > N, liste)
        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == '__main__':
    main()
