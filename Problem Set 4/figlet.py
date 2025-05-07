import sys
from pyfiglet import Figlet
from random import choice
def main():
    figlet = Figlet()
    list_fonts = figlet.getFonts()
    random = choice(list_fonts)

    if len(sys.argv) == 1:
        figlet.setFont(font=random)
        print(f'Output:\n{figlet.renderText(input("Input: "))}')
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in list_fonts:
        figlet.setFont(font=sys.argv[2])
        print(f'Output:\n{figlet.renderText(input("Input: "))}')
    else:
        sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
