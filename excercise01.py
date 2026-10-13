#
flag =True
while flag == True:
    userName = input('Ingrese nombre de usuario: ')
    numberTimesStr = input('Ingrese numero de veces a imprimir en consola: ')
    numberTime = int(numberTimesStr)

print((userName + "\n") * numberTime)