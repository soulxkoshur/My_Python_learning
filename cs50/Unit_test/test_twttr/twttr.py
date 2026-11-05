def main():
    
    word = input("Input: ")
    x = shorten(word)
    print(x)


def shorten(word):
    vowel = ["a", "e", "i", "o", "u"]
    stripped_word = ""
    for i in word:
        if i.lower() in vowel:
            pass
        
        else:
            stripped_word += i
    return stripped_word


if __name__ == "__main__":
    main()