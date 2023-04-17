import sys
A=int(sys.stdin.readline())
stack=[]
for i in range(A):
    c = sys.stdin.readline().split()
    if 'push' in c:
        A,B= c.split(' ')
        stack.append(B)
    elif c == 'pop':
        if stack:
            d=stack.pop()
            print(d)
            continue
        else:
            print('-1')
    elif 'size' == c:
        print(len(stack))
        continue
    elif 'empty' == c:
        if stack:
            print(1)
            continue
        else:
            print(0)
            continue
    elif 'top' == c:
        if stack:
            print(stack[-1])
        else:
            print(-1)