def main():
    while True:
        try:
            answer = input("Fraction: ")
            if answer.endswith("0"):
                raise ZeroDivisionError
            break
        except (ValueError, ZeroDivisionError):
            pass
    percentage = convert(answer)
    print(gauge(percentage))


def convert(fraction):
        try:
            x, y = fraction.split("/")
            fraction = round((int(x)/int(y))*100)
            if fraction <= 100:
                return fraction
            else:
                raise ValueError
        except (ValueError, ZeroDivisionError):
            pass


def gauge(percentage):
    if percentage <= 1:
        return ("E")
    elif percentage >= 99:
        return ("F")
    else:
        return (f'{percentage}%')

if __name__ == "__main__":
    main()
