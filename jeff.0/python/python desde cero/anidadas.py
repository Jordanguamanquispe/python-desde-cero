print("conversor \n" )
print("menu de opciones ")

print("""  1.- numeros a palabras 
           2.- palabras a numeros \n """)
opcion= int(input("digite la opcion "))

if opcion == 1 : 
    print("\n conversor de numeros a palabras \n ")
    opcion1 = int(input("escriba el numero que desea convertir a palabra: "))
    if opcion1 == 1 :
        print("el numero es uno")
    elif opcion1 == 2:
        print("el numero es dos")
    elif opcion1 == 3 :
        print("el numero es tres ")
    elif opcion1 == 4 : 
        print("el numero es cuatro")
    elif opcion1 == 5 :
        print("el numero es cinco")
elif opcion == 2 :
    print("\n conversor de palabra a numero ")
    opcion2 = input("escriba la palabra que desee convertir en numero : ")
    if opcion2 == "uno" :
        print("el numero es 1")
    elif opcion2 == "dos":
        print("el numero es 2 ")
    elif opcion2 == "tres" :
        print("el numero es 3 ")
    elif opcion2 == "cuatro" : 
        print("el numero es 4")
    elif opcion2 == "cinco" :
        print("el numero es 5 ")
else:
    print("opcion no encontrada ")











































































































