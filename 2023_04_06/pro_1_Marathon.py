def solution(players:list, callings):
    dict={}
    s=set(callings)
    for i in s:
        dict[i]=callings.count(i)
    for j in players:
        if j in dict:
            D=players.index(j)
            players.pop(D)
            players.insert(D-dict[j],j)
    return players
