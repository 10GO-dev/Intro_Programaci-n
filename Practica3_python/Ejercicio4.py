''' •	Crear un programa que muestre las letras de la Z (mayúscula) a la A (mayúscula, descendiendo)'''

letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q',
          'r','s','t','u','v','w','x','y','z']

desc = reversed(letras)
for x in desc:
 print(x.upper())