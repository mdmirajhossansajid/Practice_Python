inp=input()
numbers=inp.split()
num1=int(numbers[0])
num2=int(numbers[1])
num3=int(numbers[2])
# min_num=min(num1,num2,num3)
# max_num=max(num1,num2,num3)
min_num=num1;
max_num=num1;
if num2<min_num:
    min_num=num2
if num3<min_num:
    min_num=num3
if num2>max_num:
    max_num=num2
if num3>max_num:
    max_num=num3
print(min_num, max_num)
