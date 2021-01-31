import re

a=input()
b=re.compile(input())
c = b.search(a)
if not  c:
    print((-1,-1))
while c:
    print((c.start(),c.end()-1))
    c=b.search(a,c.start()+1)
