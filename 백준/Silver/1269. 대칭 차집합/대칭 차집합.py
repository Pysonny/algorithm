T = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

list_0=list((set(B)) ^ set(A))

print(len(list_0))