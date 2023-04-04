def solution(num, k):
    num=str(num)
    k=str(k)
    for i,o in enumerate(num):
        if o == k:
            return i+1
    return -1