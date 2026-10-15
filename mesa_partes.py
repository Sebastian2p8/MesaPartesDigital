import csv
import os

ARCHIVO = 'expedientes.csv'


def cargar():
    registros = []
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, 'r', encoding='utf-8', newline='') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if len(fila) == 4:
                    registros.append(fila)
    return registros


def guardar(registros):
    with open(ARCHIVO, 'w', encoding='utf-8', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(registros)


def registrar(registros):
    codigo = input('Código del expediente: ').strip().upper()
    if not codigo or any(fila[0] == codigo for fila in registros):
        print('Código vacío o repetido.')
        return
    nombre = input('Nombre del ciudadano: ').strip()
    documento = input('DNI (8 dígitos): ').strip()
    asunto = input('Asunto del trámite: ').strip()
    if not nombre or not asunto or len(documento) != 8 or not documento.isdigit():
        print('Datos incorrectos. Revisa nombre, DNI y asunto.')
        return
    registros.append([codigo, nombre, documento, asunto])
    guardar(registros)
    print('Expediente registrado correctamente.')


def mostrar(registros):
    if not registros:
        print('No hay expedientes.')
    for fila in registros:
        print(' | '.join(fila))


def buscar(registros):
    codigo = input('Código a buscar: ').strip().upper()
    for fila in registros:
        if fila[0] == codigo:
            print('Encontrado:', ' | '.join(fila))
            return
    print('Expediente no encontrado.')


def ordenar(registros):
    ordenados = sorted(registros, key=lambda fila: fila[0])
    mostrar(ordenados)


def main():
    registros = cargar()
    while True:
        print('\nMESA DE PARTES DIGITAL')
        print('1. Registrar expediente')
        print('2. Mostrar expedientes')
        print('3. Buscar por código')
        print('4. Ordenar por código')
        print('5. Salir')
        opcion = input('Elige una opción: ').strip()
        if opcion == '1':
            registrar(registros)
        elif opcion == '2':
            mostrar(registros)
        elif opcion == '3':
            buscar(registros)
        elif opcion == '4':
            ordenar(registros)
        elif opcion == '5':
            break
        else:
            print('Opción incorrecta.')


if __name__ == '__main__':
    main()
