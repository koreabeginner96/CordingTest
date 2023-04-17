from collections import deque
dr=[-1,0,0,1]
dc=[0,-1,1,0]
def solution(maps):
    answer = 0
    row= len(maps[0])
    col= len(maps)
    for i in range(col):
        for j in range(row):
            if map[i][j] =='S':
                bfs(maps,i,j)
def bfs(maps,i,j):
    queue=deque([i,j])
    maps[i][j]='x'
    cnt=0
    while queue:
        cnt+=1
        i,j = queue.popleft()
        for k in range(4):
            Ni= i+dc[k]
            nj= j+dr[k]
            if Ni > -1 and Ni < len(map) and nj > -1 and nj <len(map[0]):
                maps[Ni][nj]='X'
                queue.append([Ni,nj])
    return cnt