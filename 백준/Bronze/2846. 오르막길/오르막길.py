N = int(input())
lists = list(map(int,input().split()))
max_ = 0
max_lists= []
for i in range(N-1):
    if lists[i] < lists[i+1]:
        max_ += lists[i+1]-lists[i]
    else:
        max_lists.append(max_)
        max_ = 0
max_lists.append(max_)
print(max(max_lists))