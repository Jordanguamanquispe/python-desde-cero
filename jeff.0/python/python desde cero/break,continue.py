#ejemplo para break 
print("while con la sentencia break \n ")
contador = 0 
while contador < 10 :
    contador += 1 
    if contador == 5:
        break 
    print (" valor actual", contador)
print("fin")

# ejemplo continue 
print("while con la sentencia continue \n ")
contador = 0 
while contador < 10 :
    contador += 1 
    if contador == 5:
        continue
    print (" valor actual", contador)
print("fin")
