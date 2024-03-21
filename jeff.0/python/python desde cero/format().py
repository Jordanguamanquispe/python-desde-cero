nombre = input("escribe tu nombre: ")
edad= input("escribe tu edad: ")
print("hola {} tienes {} ".format(nombre, edad ))

#ejemplo2 
print("hola {nombre} tienes {edad}".format(nombre = "jeff" , edad = 19 ))

#ejemplo3
nombre = input("escribe tu nombre: ")
edad= input("escribe tu edad: ")
print("hola {1} tienes {0} ".format(nombre, edad )) # aunque tengas las variables desordenadas 
#en format puedes acomodarlas solo dandole el orden en los corchetes 
