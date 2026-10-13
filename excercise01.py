#2.1 Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
# imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número 
# introducido.

flag =True
while flag == True:
    userName = input('Ingrese nombre de usuario: ')
    numberTimesStr = input('Ingrese numero de veces a imprimir en consola: ')
    numberTime = 0
    try:
        numberTime = int(numberTimesStr)
    except:
        print('ERROR!!: Debes escribir un numero entero')

    print((userName + "\n") * numberTime)
    flag = False


