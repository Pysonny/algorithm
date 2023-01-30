a = [sum(list(map(int,input().split()))) for i in range(5)]
# split()은 str형식으로 리스트에 저장됨
print(a.index(max(a))+1,max(a))