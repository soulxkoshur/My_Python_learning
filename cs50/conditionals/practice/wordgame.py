master_words = {"Hair": 4, "Pair": 4, "Chair": 5, "Graphic": 7}

def main():
    words = master_words.copy()
    print("> welcome to word spell bee!", "> your letters are: A I P C R H G" , sep="\n")
    while len(words) > 0:
        print(f" > {len(words)} words left!")
        guess = input(">Enter a word: ").title()
        if guess == "Graphic":
            words.clear()
            print("Congrats you have won the game!")
        if guess in words.keys():
            print(f" correct!, you got {words[guess]} points.")
            words.pop(guess)
    if len(words) == 0:
        for word, points in master_words.items():
            print(f"the word is: {word}, and it's worth {points} points.")
main()
