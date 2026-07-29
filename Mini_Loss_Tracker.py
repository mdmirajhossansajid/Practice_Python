t=int(input())
x=float(input())
total=0
for i in range(t):
    numbers=float(input())
    total+=numbers
average=total/t 
if(x>=average):
    print("PASS")
else:
    print("RETRY")