import sys
from PIL import Image, ImageOps

def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif not sys.argv[1].lower().endswith(('.png', '.jpg', '.jpeg')) or not sys.argv[2].lower().endswith(( '.jpg', '.jpeg', '.png')):
            sys.exit("Invalid input")
        elif sys.argv[1][-4:] != sys.argv[2][-4:]:
            sys.exit("Input and output have different extensions")
    except FileNotFoundError:
        sys.exit("Input does not exist")

    human = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    cropped_human = ImageOps.fit(human, [600,600])
    cropped_human.paste(shirt, (0,0), shirt)
    cropped_human.save(sys.argv[2])

if __name__ == "__main__":
    main()
