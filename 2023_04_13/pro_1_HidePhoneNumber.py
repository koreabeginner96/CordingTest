def solution(phone_number):
    A=phone_number[len(phone_number)-4:]
    answer = ''
    for i in range(len(phone_number)-4):
        answer+='*'
    answer+=A
    return answer