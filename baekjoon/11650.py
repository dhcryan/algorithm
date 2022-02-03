import sys
n=int(input())
arr=[]
for i in range(n):
    [row,col]=map(int,input().split())
    arr.append([row,col])
arr.sort(key=lambda x:(x[0],x[1]))
for i in arr:
    print(i[0],i[1])
