def main():
    while True:
        
        fraction = input("Enter fraction: ")
        try:
            result = convert(fraction)
            if result is True:
                continue
            else:
                y = gauge(result)
                if y == "E":
                    print("E")
                elif y == "F":
                    print("F")
                else:
                    print(y)
                break
        except ZeroDivisionError, TypeError, ValueError:
            continue
       
def convert(fraction):
    try:
        x, y = fraction.split("/")
        int(x)
        int(y)
    except TypeError:
        raise TypeError
        if int(x) > int(y) or int(x) < 0 or int(y) < 0:
            raise ValueError
        elif int(y)==0:
            raise ZeroDivisionError
        
        else:
            return round((int(x) / int(y))*100)

def gauge(percentage):
    try:
        if percentage <= 1:
            return "E"
                    
        elif percentage >= 99:
            return "F"
        else:
            return f"{percentage}%)"
    except TypeError:
        raise TypeError 

if __name__ == "__main__":
    main()