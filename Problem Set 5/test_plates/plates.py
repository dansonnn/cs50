def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

# Checks if plate starts with 2 letters.
    i = 0
    for letter in s:
        if letter.isalpha() == False:
            return False
        else:
            i += 1
            if i == 2:
                break
# Checks if plate is between 2 to 6 characters long.
    if 2 <= len(s) <= 6:
        pass
    else:
        return False
# Checks if plate ends with numbers (if applicable).
    digit_present = False
    if s.isalpha() == False:
            for k in s:
                if digit_present == False:
                    if k.isdigit():
                        digit_present = True
                else:
                    if k.isalpha():
                        return False
# Checks if first number is not 0
    if s.isalpha() == True:
        pass
    else:
        for j in s:
            if j.isdigit():
                if j == "0":
                    return False
                else:
                    break
# Checks if plate contains periods, spaces or punctuation marks.
    if s.isalnum():
        pass
    else:
        return False

    return True

if __name__ == "__main__":
    main()
