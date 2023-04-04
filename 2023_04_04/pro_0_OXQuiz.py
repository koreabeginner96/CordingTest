def solution(quiz):
    A=quiz
    B=[]
    C=[]
    Answer=[]
    for i in A:
        i = i.split(' ')
        B = []
        B.extend(i)
        B[0] = int(B[0])
        B[2] = int(B[2])
        B[4] = int(B[4])
        if "-" in i:
            if B[0]-B[2]==B[4]:
                C.append("O")
            else:
                C.append("X")
        else:
            if B[0]+B[2]==B[4]:
                C.append("O")
            else:
                C.append("X")
    return C
