s = input("type any str")
captils = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]
results = "" 
for c in s:
    if c in captils:
        results += "_" + c.lower()
    else:
        results += c.lower()

print(results)