import re
a = re.findall(r"([A-Za-z0-9])\1+", input())
if(len(a) > 0):
     print(a[0])
else:
    print("-1")
