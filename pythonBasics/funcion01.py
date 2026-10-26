def suma(numero, numero2):
    return numero + numero2

def resta(numero, numero2):
    return numero - numero2

def multiplicacion(numero, numero2):
    return numero * numero2

def division(numero, numero2):
    return numero / numero2

def menuCalculadora():
    print('Calculadora')
    print('1) Suma')
    print('2) Resta')
    print('3) Multiplicacion')
    print('4) Division')
    print('0) Salir')

while True:
    try:
        menuCalculadora()
        operacion = int(input('Seleccione una operacion: '))
        if operacion == 0:
            break
        elif operacion not in range(5):
            print('----------------------------------------')
            print('ERROR!! Elegiste un operador erroneo')
            print('----------------------------------------')
            continue
        numero = int(input('Ingrese el primer operador: '))
        numero2 = int(input('Ingrese el segundo operador: '))
        result = 0
        if operacion == 1:
            result = suma(numero, numero2)
        elif operacion == 2:
            result = resta(numero, numero2)
        elif operacion == 3:
            result = multiplicacion(numero, numero2)
        elif operacion == 4:
            if numero2 != 0:
                result = division(numero, numero2)
            else:
                print('----------------------------------------')
                print('Error!!, division entre cero indefinida')
                print('----------------------------------------')
                continue            
        print(f'Resultado de la {'suma' if operacion == '1' else 'resta'} es {result}')
        if operacion == 0:
            print()
    except:
        print('----------------------------------------------------------')
        print("ERROR!! Ingresaste un caracter errorneo, deben ser numeros")
        print('----------------------------------------------------------')