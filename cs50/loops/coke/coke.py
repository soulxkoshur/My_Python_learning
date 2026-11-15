amount = 50
print("Amount due:", amount)
while True:
    if amount > 0:
        coin = int(input("insert coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            amount -= coin
            if amount > 0:
                print("Amount due:", amount)
        elif coin != 25 or coin != 10 or coin != 5:
            print("Amount due:", amount)
        else:
            continue
    else:
        if amount <= 0:
            print("Change owed:", -amount)
        break
