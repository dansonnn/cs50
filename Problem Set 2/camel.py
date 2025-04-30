def main():
    camel = input("camelCase: ")
    print("snake_case: ", end="")
    for i in camel:
        if i.isupper():
            print(i.replace(i, f'_{i.lower()}'), end="")
        else:
            print(i, end="")
    print("")
main()
