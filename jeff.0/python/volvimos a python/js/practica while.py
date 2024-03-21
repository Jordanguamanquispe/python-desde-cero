#Contador regresivo: Escribe un programa que solicite al usuario un número y luego 
#imprima un contador regresivo desde ese número hasta 1.
#ejercicio 1 

#print("contador")
#contador = int(input("escriba un numero: "))
#while contador >= 1 :
    #print(contador)
    #contador -= 1 
#print("fin")

# haga un programa que el usuario ingrese la cantidad de productos y sume los precios 
#print("Tienda Tuti")
#num_productos = int(input("Escriba la cantidad de productos: "))
#contador = 0
#print("Escriba los precios de cada producto:")
#while num_productos > 0:
    #precio = float(input("Precio del producto: "))
    #contador += precio
   # num_productos -= 1
#print("El precio total es:", contador)

#JORDAN SI VUELVES A LEER ESTO RECUERDA QUE SI VAS HACER TIPO CONTADOR RECUERDA PONER CONTADOR 
#PRIMERO Y DESPUES ESCRIBE QUE SEA MAYOR A CERO ESTO TE SERVIRA PARA 
#QUE LAS CANTIDADES SE SUMEN Y ABAJO DE LA SUMA Q HAGAS EN EL WHILE 
#PONGAS CONTADOR -= 1 

#tabla de multiplicar 
#print("tabla de multiplicar")
#num1 = int(input("escriba la tabla que desea imprimir en pantalla: "))
#long = int(input("escriba hasta donde quiere que se multiplique la tabla: "))
#x = 0
#resultado = 0 
#while long >= x :
    #print( "{} x {} = {}".format(num1 , x , resultado)  )
   # x += 1
    #resultado = num1 * x 
#print("fin")


#Contador de números pares e impares: Escribe un programa que 
#solicite al usuario un número y luego imprima la cantidad de números pares 
#e impares desde 1 hasta ese número utilizando un bucle while.
num = int(input("escriba hasta donde desea que contemos los numeros pares e impares: "))
x = 1
par = 0 
impar = 0 
while x <= num : 
    if x % 2 == 0 :
        par += 1 
    else :
        impar += 1 
    x += 1 
print("numeros pares encontrados {} numeros impares encontrdados {}".format(par , impar))

       





































