print(" RAPPY \n ")
name = input("escriba su nombre ")
print("sistema de bacaciones para trabajadores ")
print(""" Elija el departamento donse usted trabaja 
      1.- Departamento de atencion al cliente 
      2.- Departamento de logistica 
      3.- Gerencia
""")

opcion = int(input("digite la opcion "))
if opcion == 1 :
    print("departamento de atencion al cliente ")
    print("escriba los años que lleva trabajando en el departamento de atencion al cliente ")
    num = int(input(""))
    if num == 1 :
        print("hola usted tiene 6 dias de vacaciones")
    elif num == 2 or  num <= 6 : 
        print(" hola usted tiene 14 dias de vacaciones ")
    elif num >= 7 :
        print("hola usted tiene 20 dias de vacaciones ")
    else:
        print("disfrute sus vacaciones ", name )
elif opcion == 2 :
    print("Departamento de logistica \n")
    num2 = int(input("escriba los años que lleva trabajando: "))
    if num2 == 1 :
        print ("usted tiene 7 dias de vacaciones ")
    elif num2 == 2 or num2 <= 6 :
        print("usted tiene 15 dias de vacaciones ")
    elif num2 >= 7: 
        print("usted tiene 22 dias de vacaciones ")
    else :
        print("disfrute de sus vacaciones señor", name )
elif opcion == 3 :
    print("Gerencia  \n")
    num3 = int(input("escriba los años que lleva trabajando: "))
    if num3 == 1 :
        print ("usted tiene 10 dias de vacaciones ")
    elif num3 == 2 or num3 <= 6 :
        print("usted tiene 20 dias de vacaciones ")
    elif num3 >= 7: 
        print("usted tiene 30 dias de vacaciones ")
    else :
        print("disfrute de sus vacaciones señor", name )

else: 
    print ("opcion no encontrada ")