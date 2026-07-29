t=int(input())
for i in range(t):
    numbers=int(input())
    if numbers==0:
        print(0)
        continue
    while numbers>0:
        lastdigit=numbers%10
        numbers=numbers//10
        print(lastdigit,end=" ")
    print()    
        
        
    