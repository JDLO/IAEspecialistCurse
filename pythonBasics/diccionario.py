frutas = {
    'Platano': 1.35,
    'Manzana': 0.85,
    'Pera': 0.85,
    'Naranja': 0.70
}
frutaInput = input('Escriba la fruta de su eleccion').title()
if frutaInput in frutas:
    kilos = input('Escriba los kilos que desea')
    print(f'El precio de {kilos}Kg de {frutaInput} es de {(frutas[frutaInput] * float(kilos)):.2f}$')
else:
    print('No existe la fruta en inventario')