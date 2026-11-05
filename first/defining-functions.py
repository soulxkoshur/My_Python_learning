#first things first, we define function by "def" key, and what that function does is written after ":"
def main():
    x = int(input("type a number"))
    print("square of x is ",square(x))

#here, we defined main as a function, which takes an input and prints it, notice we used square above
#we defined a function called square, which has a function of squaring number, as we defined below
#then we used the return function to store the operation or something basically passing it down,,,ig

def square (n):
    return pow(n,2)

main ()
