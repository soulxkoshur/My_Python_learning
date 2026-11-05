greeting = input("type a greeting").casefold().strip()

if "hello" in greeting:
    print("$0")
elif greeting.endswith("h",0,1):
    print("$20")
else: 
    print("$100")