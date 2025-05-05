def main():
    while True:
        try:
            prompt = input("Date: ").strip()
            month, day, year = split_date(prompt)
            if validate_date(month, day, year):
                print(f'{year}-{month:02}-{day:02}')
                break
            else:
                continue
        except ValueError:
            pass
        
# Check if input starts with the month formatted in string
def split_date(prompt):
    for i in months:
        if prompt.startswith(i):
            list(prompt).index(",")
            month_word, day, year = prompt.replace(",", "").split()
            month = months.index(month_word) + 1
            break
    else:
        month, day, year = prompt.split("/")
    return (int(month), int(day), int(year))

# Check if date is valid (within 31 days per month and 12 months per year)
def validate_date(month, day, year):
    return 1 <= month <= 12 and 1 <= day <= 31

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

main()
