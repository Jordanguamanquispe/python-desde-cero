print(" escriba 3 numeros para verificar cual es el numero mayor")
num = int(input(""))
num2 = int (input(""))
num3 = int(input(""))
if num > num2 and num > num3:
    print("el numero ", num , " es mayor que todos ")
elif num2 > num3 :
    print("el numero", num2 , " es mayor")
else : 
    print("el numero" , num3, "es mayor que todos ")
