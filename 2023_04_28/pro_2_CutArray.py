def solution(n, left, right):
    return[(max(n//i,n%i)+1 for i in range(left,right+1))]