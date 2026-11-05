#use argument and store variable
name = input("what's your name? ").title().strip()

#remove whitespace from the string (accident commas basically, works on first world)
###name = name.strip()

# Make the string in capital
###name = name.title()
"""
or you can chain them in one go
"""
#name = name.title().strip():::: hell with this you can just put it in the first line tooo!!

#another formating function split
#so this here tells the program to break, name variable data after space into two variables!

first, last = name.split(" ")

#use variables and argument
print("hello, " + last + ".")

"""
things we can put in the function like print "print( inside here)" are called parameters, and the values,
we put are called arguments

end="anything goes here, it stops line break after print"
sep="same as above, but with space"

positional parametes: "anything in double qoutes in print function", or named parameteres
example of named parameters is, end="" and sep=""
note: you can use these parameters anywhere generally at the end, also... you can use their name
that's why they called named parameters.

"""
