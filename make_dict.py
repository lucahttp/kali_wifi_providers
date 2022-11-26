#!/usr/bin/env python  

## Fibertel

# Comienza con 004 ó 014 O 044. - 004 (hombre) o 114 (mujer) 
#       013 si es de Fibercorp hombre mas el CUIT (o CUIL no me acuerdo)
# 3code + DNI
# 3code + DNI - 1 caracter

from __future__ import print_function #Arreglo con los posibles comienzos de la contraseña  
st = ['004','014','044']


fibert_list_passwords = []
for i in range(0, len(st)):
 print(st[i])
 for x in range(2000000, 5000000):  
  # print ('{0}{1:07d}'.format(st[i], x))
  pw_string = '{0}{1:07d}'.format(st[i], x)
  fibert_list_passwords.append(pw_string)
 for x in range(20000000, 50000000):  
  # print ('{0}{1:07d}'.format(st[i], x))
  pw_string = '{0}{1:07d}'.format(st[i], x)
  fibert_list_passwords.append(pw_string)

# print(fibert_list_passwords)

# https://www.folkstalk.com/2022/10/mustpython-write-array-to-file-values-as-separate-lines-with-code-examples.html
with open('listfile.txt', 'w') as filehandle:
    for listitem in fibert_list_passwords:
        filehandle.write('%s\n' % listitem)


## FiberCorp

# Comienza con 010
#       013 si es de Fibercorp hombre mas el CUIT (o CUIL no me acuerdo)

# 20, 23, 24 y 27 para Personas Físicas
# 30, 33 y 34 para Empresas.
# 2000000 y termina en 3400000.
#       30-61025233-4 -> 30-61025|233-4 -> 3061025


# 3code + CUIT - 4

st = ['010']
for i in range(0, len(st)):
 for x in range(2000000, 3400000):
  print ('{0}{1:07d}'.format(st[i], x))


## Claro

# Les paso las de claro: Son los 8 primeros digitos de la mac address y los 4 numeros del nombre de red. Aca no necesitas saber el dni del vecino, pero te hace falta una app que te liste las redes con sus datos.



## Telecentro
# 12 caracteres A-Z 0-9 -> (26+10) ^ 12 -> (36) ^ 12 -> 4.738.381.338.321.616.896




## DEMO
# 4 1-3
# 3*3*3*3 -> 3 ^ 4 -> 81

