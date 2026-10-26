n = 5
for i in range(n):
    print(' ' * (n - i), end='')
    print('*' * i)

listy = [1,2,3,4,5,6,7,8,9,10]
listResutl = [n for n in listy if n % 2 == 0]
print('El resultado de la lista es: ', listResutl)


asignaturas = ["Matemáticas", "Física", "Química", "Historia","Lengua"]
copyAsignatura = list(asignaturas)
for asignatura in copyAsignatura:
    nota = float(input(f'Nota de la asignatura {asignatura}'))
    if nota >= 5:
        asignaturas.remove(asignatura)

print('Debes de repetir las siguientes materias:')
print(*asignaturas, sep=" - ")