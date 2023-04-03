
def solution(array:list, n):
    B=[]
    array.append(n)
    array.sort()
    C=array.index(n)
    B.append(array[C-1])
    if array[-1] ==n:
        return array[C-1]
    B.append(array[C+1])
    if n-B[0]>B[1]-n:
        return B[1]
    else:
        return B[0]
print(solution([3,10,28],20))

