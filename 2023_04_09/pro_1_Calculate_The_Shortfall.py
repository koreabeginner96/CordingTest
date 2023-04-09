def solution(price, money, count):
    B=0
    for i in range(1,count+1):
        A=price*i
        B+=A
    if B>money:
        return B-money
    else:
        return 0