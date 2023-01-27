heap = []

for _ in range(int(input())):
    heap.append(input())

result_1 = set(heap)
result = list(result_1)
result.sort()
result.sort(key=len)

print(*result,sep='\n') # 리스트 한 줄 씩 출력