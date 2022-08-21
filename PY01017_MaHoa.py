for i in range(int(input())):
    str = input()
    str = str + '@'
    # print(str)
    cnt = 0
    tmp = str[0]
    charList = []
    cntList = []
    for i in range(len(str)):
        if str[i] != tmp:
            cntList.append(cnt)
            charList.append(tmp)
            tmp = str[i]
            cnt = 1
        else:
            cnt += 1
   

    for i in range(len(charList)):
        print(f'{cntList[i]}{charList[i]}', end = '')
    
    print()