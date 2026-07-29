t=int(input())
yesCount=0;NoCount=0
for i in range(t):
    votes=input()
    if votes=="YES":
        yesCount+=1
    else:
        NoCount+=1
if yesCount>=NoCount:
    print("ACCEPT")
else:
    print("REJECT")