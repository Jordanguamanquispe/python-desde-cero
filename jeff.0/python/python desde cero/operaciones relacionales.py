print("\n escriba dos numeros para ver y dar 3 opciones si son diferentes o es mayor o es mayor o igual ")
number = int(input("esriba el primer numero"))
number2 = int(input("escriba el segundo numero "))

print("numero de comparar son" , number , "y", number2)

if number == number2:
    print("son iguales...")
if number != number2 :
    print("es diferente..")
if number < number2:
    print("es menor...")
if number >number2:
    print("es mayor") 
if number <= number2:
    print("es menor o igual...")
if number >= number2 :
    print("mayor o igual.....")