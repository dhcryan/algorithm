n,m=map(int,input().split())
str1=list(map(int,input().split()))
str1.sort()
visited=[0]*n
solved=[]
def solve(idx):
    global solved
    if len(solved)==m:
        print(' '.join(map(str,solved)))
        return
    for i in range(idx,len(str1)):
        if visited[i]==True:
            continue
        solved.append(str1[i])
        solve(i + 1)
        solved.pop()
solve(0)
