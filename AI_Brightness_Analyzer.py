inp=input()
numbers=inp.split()
total=0
for i in range(len(numbers)):
    total+=int(numbers[i])
average=total/len(numbers)
if average<85:
    print("Dark Image")
elif average<=170:
    print("Normal Image")
else:
    print("Bright Image")