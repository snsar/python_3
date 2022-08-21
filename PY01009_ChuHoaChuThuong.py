x = input()
low = 0
up = 0
for i in x:
    if i.islower():
        low += 1
    elif i.isupper():
        up += 1

if low >= up:
    print(x.lower())
else:
    print(x.upper())