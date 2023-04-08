def solution(players:list, callings:list):
    dict={}
    for i in callings:
        if i not in dict:
            dict[i]= callings.count(i)
    for j in players:
        if j in dict:
            A=players.index(j)
            players.pop(A)
            players.insert(A-dict[j], j)
    return players
print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))
