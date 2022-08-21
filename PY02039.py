n = int(input())
nuaTren = 0
nuaDuoi = 0
for i in range(n):
    x = input()
    ls = list(map(int, x.split()))
    for j in range(len(ls)):
        if j > i:
            nuaTren += ls[j]
        elif j < i:
            nuaDuoi += ls[j]
k = int(input())

chenhLech =  abs(nuaTren - nuaDuoi)
check = k - chenhLech

if check >= 0:
    print('YES')
else:
    print("NO")

print(chenhLech)