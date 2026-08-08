inp=int(input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
new_arr =lambda x,y:y+x
print(*new_arr(arr1,arr2))