n=int(input())
inp=input()
sum=0
arr=[]
for i in range(n):
    x=int(inp[i])
    arr.append(x)
    sum += x
print(sum)