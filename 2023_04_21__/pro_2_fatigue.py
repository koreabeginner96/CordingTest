from itertools import permutations


def solution(k, dungeons):
    dun_num = len(dungeons)
    answer = 0
    #8개밖에 안되고 모든경우의 수 해도 시간초과가 안되서 permutations 사용했다.
    for permut in permutations(dungeons, dun_num):
        hp = k
        count = 0
        for pm in permut:
            if hp >= pm[0]:
                hp -= pm[1]
                count += 1
            answer = max(count, answer)
    return answer