x = input()

count4 = count7 = 0

for i in x:
    if i == 4:
        count4 += 1
    elif i == 7:
        count7 += 1

res = count4 + count7
if res == 4 or res == 7:
    print("YES")
else:
    print("NO")
