'''

1. land를 이용해서 N과 M을 구하고 2차원 dp를 정의
2. dp의 맨 윗줄을 land값으로 초기화
3. dp
    - 이전 행에서 자신의 열을 제외한 dp리스트(슬라이싱 이용)에서 가장 큰 값과 자신의 값의 합을 dp에 초기화
4. dp의 마지막 행의 최댓값 출력
'''
def solution(land):
    N, M = len(land), len(land[0])
    dp = [[0 for _ in range(M)] for _ in range(N)]
    for j in range(M):
        dp[0][j] = land[0][j]
    for i in range(1, N):
        for j in range(M):
            #이게 Dp의 핵심
            dp[i][j] = max(dp[i-1][:j]+dp[i-1][j+1:])+land[i][j]
    return max(dp[-1])
print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))