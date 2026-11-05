def main():
    x = input('type any text with, ":)" or ":(" emoticons ')
    print (convert(x))


def convert(n):
     return n.replace(":(", "🙁",).replace(":)", "🙂")

main()

