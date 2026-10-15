primer_curso = ['Matematicas', 'Español', 'Fisica']
lengua = 'prueba'

def add_course(curses, curse):
    curses.append(curse)
    curses.append(lengua)
    return

add_course(primer_curso, 'Quimica')
print(primer_curso)
