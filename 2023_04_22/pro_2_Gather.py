from itertools import *
def solution(word):
    gather='AEIOU'
    list=[]
    for i in range(1,6):
        for j in product(gather,repeat=i):
            list.append(''.join(j))
    list.sort()
    return list.index(word)+1