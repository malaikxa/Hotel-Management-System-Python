alp=input("enter a sentence")
letter=0
digits=0
spaces=0
for i in alp:
    if i.isalpha():
        letter += 1
    elif i.isdigit():
        digits += 1
    elif i.isspace():
        spaces += 1

print("Letters:", letter)
print("Spaces:", spaces)
print("Digits:",digits)