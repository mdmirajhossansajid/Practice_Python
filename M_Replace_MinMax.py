n=int(input())
inp=input()
numbers=inp.split()
arr=[]
for i in range(n):
    x=int(numbers[i])
    arr.append(x)
minValue=min(arr)
maxValue=max(arr)
for i in range(n):
    if arr[i] == minValue:
        arr[i] = maxValue
    elif arr[i] == maxValue:
        arr[i] = minValue

print(*arr)