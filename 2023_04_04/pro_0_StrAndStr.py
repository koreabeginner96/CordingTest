def solution(str1, str2):
    for o,i in enumerate(str1):
        if str1[o] ==str2[0]:
            l=0
            for i in range(len(str2)):
                if o+i<len(str1) and str1[o+i]==str2[i]:
                    l+=1
            if len(str2)==l:
                return 1
    return 2