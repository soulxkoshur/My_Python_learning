import random

level = int(input("level: "))
win = int(random.randrange(0, level))
while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
        elif guess > win:
            print("Too large!")
        elif guess < win:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
    except KeyError:
        pass
