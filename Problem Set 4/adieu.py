import inflect

def main():
    p = inflect.engine()
    namelist = []
    while True:
        try:
            name = input("Name: ")
            namelist.append(name)
        except EOFError:
            print(f'\nAdieu, adieu, to {p.join(namelist)}')
            break

if __name__ == "__main__":
    main()
