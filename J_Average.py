from functools import reduce

n = int(input())
arr = list(map(float, input().split()))

total = reduce(lambda x, y: x + y, arr)

average = total / n

print(f"{average:.7f}")