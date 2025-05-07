import random


def main():
    level = get_level()
    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)


        answer = x + y
        trying = True
        tries = 0
        while trying:
            while True:
                try:
                    response = int(input(f'{x} + {y} = '))
                    break
                except ValueError:
                    pass
            if answer == response:
                score += 1
                trying = False
            else:
                print("EEE")
                tries += 1
            if tries == 3:
                print(f'{x} + {y} = {answer}')
                trying = False

    print(f'Score: {score}')


def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl < 1 or lvl > 3:
                raise ValueError
            return lvl
        except ValueError:
            pass

def generate_integer(level):
        if level == 1:
            return random.randint(0, 9)
        elif level == 2:
            return random.randint(10, 99)
        elif level == 3:
            return random.randint(100, 999)

if __name__ == "__main__":
    main()
