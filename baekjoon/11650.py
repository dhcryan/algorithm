n=int(input())
arr=[]
for i in range(n):
    [row,col]=map(int,input().split())
    arr.append([row,col])
arr=sorted(arr)
for i in range(n):
    print(arr[i][0],arr[i][1])
