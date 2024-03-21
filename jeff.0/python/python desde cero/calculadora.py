print("CALCULADORA \n")
print("""opciones 
        1.- suma    3.- multiplicacion   5.- division entera   7.- modulo o resto 
        2.- resta   4.- division        6.- exponente """)
opcion = int (input(""))
if opcion == 1 :
    print("escriba los dos para sumar ")
    num = int(input(""))
    num += int(input(""))
    print("el resultado de la suma es " , num )
elif opcion == 2 :
    print("escriba los dos para restar  ")
    num = int(input(""))
    num -= int(input(""))
    print("el resultado de la resta  es " , num )
elif opcion == 3 :
    print("escriba los dos para multiplicar ")
    num = int(input(""))
    num *= int(input(""))
    print("el resultado de la multiplicacion es " , num )
elif opcion == 4 :
    print("escriba los dos para dividir ")
    num = float(input(""))
    num /= float(input(""))                   # round sirve para disminuir los decimales 
    print("el resultado de la division es " , round(num, 2 ))
elif opcion == 5 :
    print("escriba los dos para division entera  ")
    num = float(input(""))
    num //= float(input(""))
    print("el resultado de la division entera  es " , num )
elif opcion == 6 :
    print("escriba los dos uno para el numero base y el otro como exponente  ")
    num = int(input(" escriba la base "))
    num **= int(input("escriba el exponente "))
    print("el resultado de la multiplicacion con exponente es " , num )
elif opcion == 7 :
    print("escriba los dos numeros para modulo o resto ")
    num = float(input(""))
    num %= float(input(""))
    print("el resultado modulo o resto es  " , num )
else :
    print("opcion no encontrada ")
