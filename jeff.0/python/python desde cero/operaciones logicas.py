# and not  or
#and 
print ( "and \n")
num = int(input("escriba un numero mayor a 2 y menor a 5 "))
if num > 2 and num < 5 :
    print("el numero ", num , "es meyor y menor a 5 \n")
else: 
    print("el numero ", num , "no es mayor a 2  o menor a 5 ")


#Escribe un programa en Python que pida al usuario ingresar dos números enteros.
#Luego, el programa debe verificar si ambos números son pares.
#Si ambos son pares, mostrar un mensaje que diga 
#Ambos números son pares", de lo contrario, mostrar un mensaje que diga 
#Al menos uno de los números no es par".

print("escriba dos numeros enteros ")
num1 = int(input(""))
num2 = int(input(""))
if num1 % 2 == 0 and num2 % 2 == 0:
    print("los numeos son pares ")
else :
    print("al menos uno de los numeros no es par \n ")

#or 
print(" discoteca solo pueden entrar mayores de edad , pero necesita hacer previo registro\n")

num = int(input("escriba su edad "))
name = input("escriba su nombre ")
genero = input("escriba su genero con la inicial para Masculino la 'M' y para femenino la 'F'")

if num >= 18 or (genero == "f" and genero=="M"):
    print("puedes pasar ", name)
else:
    print("disculpa", name , "no puedes pasar ")

#not 
print(" escriba su nombre ")
name = input("")
if  not any(caracter.isdigit() for caracter in name ):
    print("el nombre es valido ")
else : 
    print("el nombre es invalido ")


