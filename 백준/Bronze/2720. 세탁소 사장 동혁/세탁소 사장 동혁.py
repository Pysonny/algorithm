for i in range(int(input())):
    C = int(input())
    d = [25,10,5,1]
    l = []
    for n in d:
        l.append(C//n)
        C = C %n
    print(*l)