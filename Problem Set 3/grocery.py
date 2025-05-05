def main():
    items = {
}

    while True:
        try:
            item = input().upper()
            if item not in items:
                    items[item] = 1
            else:
                items[item] += 1
        except EOFError:
            for item, number in sorted(items.items()):
                print(f'{number} {item}')
            break

main()
