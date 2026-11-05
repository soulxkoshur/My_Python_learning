while True:
    try:
        x, y = input("Enter fraction: ").split("/")
        if int(x) > int(y) or int(x) < 0 or int(y) < 0:
            continue

        result = (int(x) / int(y))*100

        if int(result) <= 1:
            print("E")
                
        elif int(result) >= 99:
            print("F")
        else:
            print(f"{round(result)}%", end="")
        break
    except(ValueError, ZeroDivisionError):
        pass



        



