lists = []
for i in range(7):
    a = int(input())
    if a % 2 != 0:
        lists.append(a)
if lists :
    print(sum(lists))
    print(min(lists))
else:
    print('-1')