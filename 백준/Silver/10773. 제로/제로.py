result = []

for i in range(int(input())):
    nums = int(input())

    if nums == 0:
        result.pop()
    else:
        result.append(nums)
print(sum(result))