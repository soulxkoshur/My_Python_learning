due = 50
change = [5, 15, 25, 10]

while True:
    
    print("Amount Due: ", due)
    coin = int(input("Insert coin: "))
    if  coin not in change:
        continue 
    elif due >= coin:
        print(f"Change Owed: {due}")
        due = due - coin
    if due == 0:
        print("Change Owed: 0")
        break