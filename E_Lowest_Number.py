n=int(input())
inp=input()
numbers=inp.split()
ar=[]
for i in range(n):
    x=int(numbers[i])
    ar.append(x)
lowest=min(ar)
for i in range(n):
    if ar[i]==lowest:
      print(lowest,i+1)
      break