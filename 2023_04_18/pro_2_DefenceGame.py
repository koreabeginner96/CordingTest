from heapq import heappop, heappush
#최대 최솟값 빠르게 찾기
def solution(n, k, enemy):
    answer, sumEnemy = 0, 0
    heap = []

    for e in enemy:
        # -e 로 최대값 저장 하기
        heappush(heap, -e)
        sumEnemy += e
        # 최대한 n에 집어넣기
        if sumEnemy > n:
            if k == 0: break
            # heap 최솟값이용해서 음수 가 큰것 =제일 작은것 sum에서 빼기
            sumEnemy += heappop(heap)
            k -= 1
        answer += 1
    return answer
