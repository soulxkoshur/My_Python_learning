import inflect

p = inflect.engine()

list = []
while True:
    try:
        x = input("Name: ").strip().title()
        list.append(x)
    except KeyboardInterrupt:
        print()
        break
    except EOFError:
        print()
        break

print("Adieu, adieu, to", p.join((list)))
