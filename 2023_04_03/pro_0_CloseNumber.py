'''
arr=['abc', 'bac','bca']
sorted(arr, key=lambda x : x)
arr=x를 지정할 전체 단위
맨 뒤 x : 앞서반복할 단위를 어떤식으로 정렬하지
cf x[0]인덱스 ,x는 사전정렬
'''
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

