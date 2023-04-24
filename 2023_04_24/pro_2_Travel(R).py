from collections import deque


def bfs(maps, i, j, n, m, visited):  # i,j:발견 위치 n,m:기준 크기 visited:방문여부
    days = 0  # 놀 수 있는 날짜 더하기
    visited[i][j] = 1  # 방문처리
    q = deque()  # 방문된 좌표 담기
    q.append([i, j])

    while q:
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        i, j = q.popleft()
        days += int(maps[i][j])  # 해당 위치에 담긴 숫자를 더하기
        for k in range(4):  # 발견한 위치에서 상하좌우를 탐색하며 숫자가 있는지 check
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < m:  # 주어진 크기 내에서 숫자가 있는지 실제 탐색 하는 부분
                if maps[nx][ny] != "X" and visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
    return days


def solution(maps):
    answer = []
    maps = [list(map(str, i)) for i in maps]  # 2차원 배열로 초기화
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]  # 방문:1,미방문:0

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" and visited[i][j] == 0:
                answer.append(bfs(maps, i, j, n, m, visited))
    if answer:
        return sorted(answer)
    else:
        return [-1]
print(solution(["X591X","X1X5X","X231X", "1XXX1"]))


