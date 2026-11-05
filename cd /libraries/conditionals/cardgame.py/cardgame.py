def main():
    difficulty = input("difficult or easy")
    players = input("Multiplayer or single-player?")
    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("cricket")
        else:                                        #this is if they choose single-player
            recommend("skippers")
    else:                                            # this is if they choose casual
        if players == "Multiplayer":
            recommend("Pubg")
        else:
            recommend("basketball")


def recommend(game):
    print("game you might like", game)

main()
