cursoMaterias = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
count = 0
for curso, creditos in cursoMaterias.items():
    print(f"{curso} tiene {creditos} creditos")
    count += creditos
print(f"Número total de creditos: {count}")