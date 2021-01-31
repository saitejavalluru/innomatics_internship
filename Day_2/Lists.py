
if __name__ == '__main__':
    L=[]
    N = int(input())
    for i in range(N):
        lst=str(input())
        lst=lst.split(' ')
        if lst[0]=='insert':
            L.insert(int(lst[1]),int(lst[2]))
        elif lst[0]=='print':
            print(L)
        elif lst[0]=='append':
            L.append(int(lst[1]))
        elif lst[0]=='remove':
            L.remove(int(lst[1]))
        elif lst[0]=='sort':
            L.sort()
        elif lst[0]=='reverse':
            L.reverse()
        elif lst[0]=='pop':
            L.pop()
