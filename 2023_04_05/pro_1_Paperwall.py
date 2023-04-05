def solution(wallpaper):
    temp=[]
    x=0
    y=0
    answer=[]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
                if wallpaper[i][j]=='#':
                    x=i
                    y=j
                    if not temp:
                        temp.append(x)
                        temp.append(y)
                        temp.append(x)
                        temp.append(y)
                    else:
                        temp[0] = min(temp[0], x)
                        temp[1] = min(temp[1], y)
                        temp[2] = max(temp[2], x)
                        temp[3] = max(temp[3], y)
    temp[2]+=1
    temp[3]+=1
    return temp
print(solution(["..", "#."]))