'''
N명의 사람 중 2명을 선택해야하는데 1명만 선택해서 그 사람에게 비례 값을 곱해서 몇 명이 존재하는지 확인한다면 굳이 2명을 선택할 필요 없지 않을까?
이런 식으로 조합에서 필요한 경우를 줄여서 생각해보고 그래도 시간복잡도가 해결하기에 불가능하다면  더 줄여보자.

(이 과정이 어렵기에 알고리즘이 어렵다고 생각한다.)


그러면 C(N, 1)에서 선택한 A가

A * (3 / 2)

A * (4 / 3)

A * (4 / 2) 이런 값을 가지는 B가 있는가? 있으면 갯수를 세라. 이런 논리로 접근할 수 있다.

이 때 A와 같은 값을 가지는 경우도 생각해주어야한다. (같은 값을 비교할 때 거리가 서로 같으
'''
def solution(weights):
    answer = 0

    dic = {}

    for i in weights:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for i in dic:
        if dic[i] > 1:
            answer += (dic[i] * (dic[i] - 1)) / 2
        if i * 2 in dic:
            answer += dic[i] * dic[2 * i]
        if i * 2 / 3 in dic:
            answer += dic[i] * dic[i * 2 / 3]
        if i * 3 / 4 in dic:
            answer += dic[i] * dic[i * 3 / 4]

    return answer