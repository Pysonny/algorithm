for _ in range(int(input())):
    N = list(map(int,input().split()))
    N.remove(max(N))
    N.remove(min(N))
    if max(N) - min(N) >= 4:
        print('KIN')
    else:
        print(sum(N))