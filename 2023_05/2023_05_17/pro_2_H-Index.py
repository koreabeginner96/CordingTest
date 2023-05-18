def solution(citations):
    citations.sort(reversed=True)
    for i in range(len(citations)):
        if i > citations[i]:
            return i
    return len(citations)