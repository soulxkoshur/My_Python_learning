months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def main():

        while True:
            try:
                date = input("Date: ")
                if "/" in date:
                    if intdate(date) is not True:
                        break
                    else:
                        continue
                else :
                    if strdate(date) is not True:
                        break
                    else:
                        continue
            except ValueError:
                continue

def intdate(n):
    a, b, c = n.split("/")
    m = int(a)
    d = int(b)
    y = int(c)
    if d <= 31 and m <= 12 :
        print("{y:04d}-{m:02d}-{d:02d}".format(y=y, m=m, d=d))
    else:
        return True
def strdate(n):
    a, b, z = n.split(" ")
    if a in months:
        if "," in b:
            b = b.removesuffix(",")
            d = int(b)
            m = months.index(a)+1
            y = int(z)
            if d <= 31 and d not in months:
                print("{y:04d}-{m:02d}-{d:02d}".format(y=y, d=d, m=m))
            else:
                return True
        else:
            return True
    else:
        return True
main()
