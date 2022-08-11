N,M=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
output=[]
def dfs(start):
    global output
    if len(output)==M:
        print(' '.join(map(str,output)))
        return
    for i in range(start,N):
        output.append(arr[i])
        dfs(i)
        output.pop()
dfs(0)