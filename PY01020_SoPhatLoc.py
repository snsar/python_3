import re
t = int(input())


while t > 0:

    txt = input()
    x = re.search("86$", txt)
    if x:
        print("YES")
    else:
        print("NO")
    t -= 1