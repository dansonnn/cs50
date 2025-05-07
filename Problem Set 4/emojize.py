from emoji import emojize
def main():
    response = input("Input: ")
    print(f'Output: {emojize(response, language='alias')}')


if __name__ == "__main__":
    main()
