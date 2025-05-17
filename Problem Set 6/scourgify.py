import sys
import csv
def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")

        all_info = []
        with open(sys.argv[1]) as oldfile:
            reader = csv.DictReader(oldfile)
            for row in reader:
                last, first = row["name"].split(",")
                all_info.append({"first": first.strip(), "last": last.strip(), "house": row["house"]})

        with open(sys.argv[2], "w", newline='') as newfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(newfile, fieldnames=fieldnames)
            writer.writeheader()
            for names in all_info:
                writer.writerow(names)

    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')

if __name__ == "__main__":
    main()
