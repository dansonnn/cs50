import sys
import csv
import tabulate

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        else:
            pizzas = []
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                for row in reader:
                    pizzas.append({"type": row[0], "small": row[1], "large": row[2]})
            print(tabulate.tabulate(pizzas, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
