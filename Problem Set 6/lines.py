import sys

def main():
    i = 0
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command line arguments")
        elif len(sys.argv) < 2:
            sys.exit("Too few command line arguments")
        elif not sys.argv[1].endswith(".py"):
            sys.exit("Not a python file")
    except FileNotFoundError:
        sys.exit("File does not exist")
    with open(sys.argv[1]) as file:
        for row in file:
            if row.lstrip().startswith("#") or row.strip() == "":
                pass
            else:
                i += 1
    print(i)

if __name__ == "__main__":
    main()
