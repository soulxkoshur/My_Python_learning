d = {}
item = ""
while True:

        try:
            item = input().upper()
            if d.get(item) == None:
                n = 0
                n += 1
                d[item] = n
            else:
                x = d.get(item)
                d[item] = x + 1
        except EOFError:
            break
        except KeyboardInterrupt:
            break

for item, count in set(sorted(d.items())):
    print(f"{count} {item}", end="\n")
