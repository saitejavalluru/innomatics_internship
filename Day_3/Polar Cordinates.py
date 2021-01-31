import cmath

line= str(input()).strip()

c = complex(line)
r = abs(complex(c.real, c.imag))
p = cmath.phase(complex(c.real, c.imag))

print('{0:}'.format(r))
print('{0:}'.format(p))
