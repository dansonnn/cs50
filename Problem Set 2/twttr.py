def main():
    tweet = input("Input: ")
    print("Output: ", end="")
    for letter in tweet:
        if letter.lower() == "a" or letter.lower() == "e" or letter.lower() == "i" or letter.lower() == "o" or letter.lower() == "u":
            continue
        else:
            print(letter, end="")
    print("")
main()
