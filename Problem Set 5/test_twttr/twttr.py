def main():
    tweet = shorten(input("Input: "))
    print(f"Output: {tweet}")

def shorten(word):
    shortened = ""
    for letter in word:
        if letter.lower() == "a" or letter.lower() == "e" or letter.lower() == "i" or letter.lower() == "o" or letter.lower() == "u":
            continue
        else:
            shortened += letter
    return shortened

if __name__ == "__main__":
    main()
