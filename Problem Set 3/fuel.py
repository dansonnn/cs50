def main():
        fuel = get_prompt()

        if fuel <= 1:
            fuel = "E"
        elif fuel >= 99:
             fuel = "F"
        else:
            fuel = (f'{fuel}%')
        print(fuel)

def get_prompt():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            current = round((int(x)/int(y))*100)
            if current <= 100:
                return current
            else:
                continue
        except (ValueError, ZeroDivisionError):
            pass

main()
