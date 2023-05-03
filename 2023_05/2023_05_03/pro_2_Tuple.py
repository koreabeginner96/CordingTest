import re
from collections import Counter
def solution(s):
    #같은 숫자끼리 dict로 묻고 counter세기
    s=Counter(re.findall('\d+',s))
    #value큰걸로 순서 정렬 하고 key으로 내보내기 items 사용해서
    return list(map(int,[k for k,v in sorted(s.items(),key=lambda x : x[1],reverse=True)]))