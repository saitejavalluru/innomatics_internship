if __name__ == '__main__':
    n = int(input())
    a = map(int, input().split())
    a=list(set(a))
    a.sort()
    print(a[len(a)-2])
