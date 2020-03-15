lista = dict(user_name= 'Manuel', user_idade= 44)
print(lista)

# Modo 1
if 'location' in lista:
    print(lista['location'])
else:
    print('Não encontrado...')

# Modo 2
try:
    print(lista['location'])
except KeyError:
    print('Não encontrado...')

# Modo 3
loc = lista.get('location', None)
print(loc)

# Método key v1
for key in lista.keys():
    value = lista[key]
    print(key, '=', value)

# Método key v2
for key, value in lista.items():
    print(key, '=', value)
