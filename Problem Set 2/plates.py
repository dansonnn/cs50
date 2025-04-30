def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if start_2_letters(s) and length(s) and ends_with_numbers(s) and first_isnot_0(s) and is_alnum(s):
        return True

# Checks if plate starts with 2 letters.
def start_2_letters(s):
    i = 0
    for letter in s:
        if letter.isalpha() == False:
            return False
        else:
            i += 1
            if i == 2:
                return True
# Checks if plate is between 2 to 6 characters long.
def length(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False
# Checks if plate ends with numbers (if applicable).
def ends_with_numbers(s):
    digit_present = False
    if s.isalpha() == False:
            for k in s:
                if digit_present == False:
                    if k.isdigit():
                        digit_present = True
                else:
                    if k.isalpha():
                        return False
    return True

# Checks if first number is not 0
def first_isnot_0(s):
    if s.isalpha() == True:
        return True
    for j in s:
        if j.isdigit():
            if j == "0":
                return False
            else:
                return True
    return True

# Checks if plate contains periods, spaces or punctuation marks.
def is_alnum(s):
    if s.isalnum():
        return True
    else:
        return False

main()
