def solution(cap, n, deliveries, pickups):
    answer = 0
    d_val=0
    p_val=0
    for i in range(n):
        d_val+=deliveries[n-i-1]
        p_val+=pickups[n-i-1]
        while d_val>0 or p_val>0:
            answer+= (n-i)*2
            d_val-= cap
            p_val-= cap
    return answer