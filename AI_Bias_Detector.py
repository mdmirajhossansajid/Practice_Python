# inp=input().split()
# A=0; B=0
# for i in range(len(inp)):
#     if inp[i]=="A":
#         A+=1
#     else:
#         B+=1
# total=len(inp)
# if A> total*0.7 or B> total*0.7:
#     print("Biased Model")
# else:
#     print("Fair Model")
 #using map and lamda function
inp=input().split()
a=list(map(lambda x: x=="A", inp))
b=list(map(lambda x: x=="B", inp))
total=len(inp)
if sum(a)> total*0.7 or sum(b)> total*0.7:
    print("Biased Model")
else:
    print("Fair Model")
