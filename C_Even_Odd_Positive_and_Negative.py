n=int(input())
inp=input()
numbers=inp.split()
positive=0;negative=0;odd=0;even=0;
for i in range(n):
    x=int(numbers[i])
    if x>0:
     positive+=1
    elif x<0:
     negative+=1
    if x%2==0:
     even+=1
    else:
     odd+=1
print("Even:",even)
print("Odd:",odd)
print("Positive:",positive)
print("Negative:",negative)
