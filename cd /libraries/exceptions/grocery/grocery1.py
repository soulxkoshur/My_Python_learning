## first step: ask for user input in a loop and break if crtl+d;
#  lets make a fuction which does that
d = {}
item = ""

n = 0
while True:
    try:

        item =  input("enter Item: ")
        if item not in d:
            d.update({item:n}) 
            d[item] = d.get(item, 0)

        elif item in d:
            n += 1
            d.update({item:n}) 
            d[item] = d.get(item, 0)
           
    except EOFError:
        break

# store the value in dictionary!
dsor = sorted(d.items())
for item, count in dsor:
    print(count, item)