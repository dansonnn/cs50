from random import randint

def main():
    while True:
        try:
            level = int(input("Level: "))
            correct = randint(1, level)
            while True:
                guess = int(input("Guess: "))
                if guess <= 0:
                    continue
                elif guess > correct:
                    print("Too large!")
                elif guess < correct:
                    print("Too small!")
                else:
                    print("Just right!")
                    break
            break

        except ValueError:
            pass

if __name__ == "__main__":
    main()
