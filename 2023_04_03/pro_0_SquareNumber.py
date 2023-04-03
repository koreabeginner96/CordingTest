def solution(n):
    num =  []
    for i in range(1, n) :
        if n % i == 0 :
            num.append(i)

    if len(num) % 2 == 0 : #제곱수라면
        return 1
    else:
        return 2
