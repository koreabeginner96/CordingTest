def solution(keymap, targets):
    answer = []
    sum=0
    key_dict = {}
    for o in keymap:
        for i,key in enumerate(o):
            if key not in key_dict:
                key_dict[key] = i+1
            else:
                key_dict[key]= min(key_dict[key],i+1)
    for i in targets:
        sum=0
        for j in i:
            if j not in key_dict:
                sum= -1
                break

            sum +=key_dict[j]
        answer.append(sum)
    return answer
