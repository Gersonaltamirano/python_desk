booleanos = [False, True]

# Tabla de verdad de or

print('x\ty\tx or y')
print('-'*22)
for x in booleanos:
    for y in booleanos:
        print(x, y, x or y, sep = '\t')

print()

# Tabla de verdad de and

print('x\ty\tx and y')
print('-'*22)
for x in booleanos:
    for y in booleanos:
        print(x, y, x and y, sep = '\t')
        
print()

# Tabla de verdad de not

print('x\tnot x')
print('-'*13)
for x in booleanos:
    print(x, not x, sep = '\t')

print()

# Tabla de verdad de ^

print('x\ty\tx ^ y')
print('-'*21)
for x in booleanos:
    for y in booleanos:
        print(x, y, x ^ y, sep = '\t') 

# http://elclubdelautodidacta.es/wp/2012/11/python-los-operadores-logicos-y-sus-tablas-de-verdad/