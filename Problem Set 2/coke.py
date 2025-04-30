def main():
    remain = 50
    while remain > 0:
        print(f"Amount due: {remain}")
        i = int(input("Insert coin: "))
        if i == 5 or i == 10 or i == 25:
            remain -= i
            if remain <= 0:
                print(f"Change owed: {-remain}")
                break
main()
