#DP문제이다. 하나씩 주석을 담아서 이해한다.
def solution(board):
    col=len(board)
    row=len(board[0])
    #정사각형을 시작하기 위해 1,1 구간부터 시작하고
    for i in range(1,col):
    #사전에 미리 0,1:,1,0: 제외 시키고 한다. 왜냐하면 정사각형을 못구현한다.
        for j in range(1,row):
    #1보다 크다면으로 해야한다. 1과 같다고 하면 안된다.
            if board[i][j]>=1:
    #3개의 위치 값을 전부 비교하고 그 중에서 가장 작은 값에 +1씩 키우면 된다.
                board[i][j]=min(board[i-1][j],board[i-1][j-1],board[i][j-1])+1
    answer = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
    #마지막으로 최대숫자를 구한다음. 제곱해서 정답을 추론하면된다.
            answer = max(answer, board[r][c])

    return answer ** 2
