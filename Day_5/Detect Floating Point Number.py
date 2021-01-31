import re
for _ in range(int(input())):
    print(bool(re.search(r'^[+-]{0,1}[0-9]*[.][0-9]+$',input().strip())))
