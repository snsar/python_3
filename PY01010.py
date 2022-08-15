t = input()
t = int(t)

while t:
    n = input()
    if n[-2]+n[-1] == n[0]+n[1]:
        print("YES")
    else:
        print("NO")
    t -= 1
'''
3
12321
1234512
10233211111
'''