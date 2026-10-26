import os
def readFile(filename, end=-1):
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        columnas = lines[0]
        for columna in columnas.split(','):
            print(columna if columna != '\n' else '',end=' |')
        print('\n')
        for line in lines[1:end]:
            for word in line.split(','):
                print(word, end=' ')
        f.close()
    except FileNotFoundError:
        print('No existe el fichero')

def loadFile(filename, end=-1):
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        columnas = lines[0].split(',')
        doc = []
        for line in lines[1:end]:
            lineClean = line.split(',')
            doc.append({columnas[index]: word for index, word in enumerate(lineClean)})
        return doc
    except FileNotFoundError:
        print('Error en el fichero')

def findById(doc, id):
    return next((element for element in doc if element['id'] == id), None)


fichero = 'pisos_gijon_500.csv'
doc = loadFile(fichero, 6)

print(doc)
print(findById(doc, '1'))
