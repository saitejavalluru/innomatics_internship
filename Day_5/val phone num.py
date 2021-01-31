import re
for i in range(int(input())):
  print('YES' if re.match('^[7-9][0-9]{9}$', input()) else 'NO')
