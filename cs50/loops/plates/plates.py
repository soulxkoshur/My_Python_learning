def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

### All conditions
def is_valid(s):
       if length(s) and first(s) and onlychar(s) and no_letters_after_numbers(s) and start_letters(s):
        return True
       else:
        return False

### length min = 2 and max = 6
def length(n):
     if 2 <= len(n) <= 6:
        return True
     else:
        return False

### first num can't be zero    
def first(n):
    for i in n:
        if i.isdigit():
            if i == "0":
                return False
            return True
    return True     
### can't end with letters
def no_letters_after_numbers(n):
    found_number = False
    for i in n:
        if i.isdigit():
            found_number = True
        elif i.isalpha():
            if found_number:
                return False
    return True
### no punctuations or symbols.    
def onlychar(n):
    letr= punctuation_tuple = ('.', ',', '?', '!', ':', ';', '-', '—', '(', ')', '[', ']', '{', '}', "'", '"', '...', " ")
    for i in n:
        if i in letr:
            return False
    else:
        return True 
### to satisfy the rule, all should start with letters first        
def start_letters(n):
      if n[0:2].isalpha():
        return True
      else:
        return False
main()

