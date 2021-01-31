def merge_the_tools(a,K):
    for n in range(len(a)//K):
        s = set([])
        out = ""
        for i in range(K*n, K*(n+1)):
            if a[i] not in s:
                s.add(a[i])
                out += a[i]
        print(out)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
