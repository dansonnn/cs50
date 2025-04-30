def main():
    period = convert(input("What time is it? "))
    if period >= 7 and period <= 8:
        print("breakfast time")
    elif period >= 12 and period <= 13:
        print("lunch time")
    elif period >= 18 and period <= 19:
        print("dinner time")

def convert(time):
    x, y = time.split(":")
    y = int(y) / 60
    return(float(int(x) + y))

if __name__ == "__main__":
    main()
