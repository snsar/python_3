t = int(input())

while t:
    x = input()
    if x[-1] == '6' and x[-2] == '8':
        print("YES")
    else:
        print("NO")
    t -= 1