from collections import deque
def solution(cards1, cards2, goal):
    stack=[]
    cards1=deque(cards1)
    cards2 = deque(cards2)
    for i in goal:
        if cards1 and i == cards1[0]:
            cards1.popleft()
        elif cards2 and i == cards2[0]:
            cards2.popleft()
        else:
            return "No"
            break
    return "Yes"
print(solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"]))