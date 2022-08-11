N,M=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
output=[]
visited=[0]*N
def dfs(start):
    global output
    overlap=0
    if len(output)==M:
        print(' '.join(map(str,output)))
        return
    # 각 자리의 방문을 체크하며 이미 쓰인 원소가 다시 쓰이지 않도록 한다.
    # overlap이란 변수를 만들어 비교한다.
    for i in range(N):
        if not visited[i] and overlap!=arr[i]:
            visited[i]=True
            output.append(arr[i])
            overlap=arr[i]
            dfs(start+1)
            visited[i]=False
            output.pop()
dfs(0)