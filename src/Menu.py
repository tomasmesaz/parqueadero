ESPACIADO = 64

def limpiar_consola():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def fecha_hora():
    from datetime import datetime as dt

    fecha = dt.now()
    anio, mes, dia = fecha.year, fecha.month, fecha.day
    fecha_ymd = f'{str(anio)}-{str(mes).zfill(2)}-{str(dia).zfill(2)}'
    hora, min = fecha.hour, fecha.minute
    estado = 'am'
    if hora >= 13:
        hora -= 12
        estado = 'pm'
    fecha_hm = f'{str(hora).zfill(2)}:{str(min).zfill(2)} {estado}'
    return fecha_ymd, fecha_hm

def imprimir_menu(nombre):

    carro = [
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣶⣶⣿⠿⠿⠿⢿⣶⣶⣤⣀⣀⣀⣠⣤⣤⣦⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⡿⠿⠛⠛⠉⠉⠀⠀⠀⠀⠀⠈⢿⡏⠉⢻⣿⣿⣿⣿⣿⡆⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠋⠀⠀⠀⣴⣶⡄⠀⠀⢰⣿⠀⠀⠀⠘⣷⡀⠀⢹⣿⣿⣿⣿⣿⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣇⣀⣤⣤⣤⣾⣿⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⡆",
"⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃",
"⠀⣰⠋⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣁⣀⣠⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀",
"⣰⣷⣦⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⣿⣿⣿⣿⣿⣿⣿⠁⠈⠙⢿⣿⣿⣿⣿⠀⣿⠀",
"⣿⣿⣿⣿⣿⣷⡀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠘⣿⣿⣿⣿⠀⣿⠀",
"⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⣀⣀⣀⣀⣀⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣿⣿⣿⣿⣀⣿⠀",
"⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢀⣼⣿⠛⠛⠛⠛⠃⠀",
"⠀⠈⠙⠻⢿⣿⣿⣿⠿⠟⠛⠛⠛⠛⠛⠉⠉⠉⠉⠉⠀⠈⠻⣿⣿⣿⣷⣶⣶⣿⡿⠁⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀"
]
    
    fecha, hora = fecha_hora()
    print('*'*ESPACIADO)
    for linea in carro:
        print(linea.center(ESPACIADO))
    print(nombre.center(ESPACIADO))
    print(fecha.center(ESPACIADO))
    print(hora.center(ESPACIADO))
    print('*'*ESPACIADO)
    print('** Menú **'.ljust(ESPACIADO))
    print('1 --> Registrar usuario')
    print('2 --> Ingresar vehículo')
    print('3 --> Retirar vehículo')
    print('4 --> Administrador')
    print('5 --> Salir')
    print('*'*ESPACIADO)

import Datos
import Registro_usuario as registro
import Ingreso_vehiculo as ingreso
import Retiro_vehiculo as retiro
import Administrador as admin

while True:
    limpiar_consola()
    imprimir_menu('UdeA iPark')
    opcion = input('Seleccione una opción (1-5) --> ')
    ESPACIADO = 64

    match opcion:
        case '1':
            print('*'*ESPACIADO)
            print('Registro de vehículo'.center(ESPACIADO))
            registro.registrar_usuario()
            input('Presiona Enter para continuar')

        case '2':
            print('*'*ESPACIADO)
            print('Ingreso de vehículo'.center(ESPACIADO))
            ingreso.ingresar_vehiculo()
            input('Presiona Enter para continuar')

        case '3':
            print('*'*ESPACIADO)
            print('Retiro de vehículo'.center(ESPACIADO))
            retiro.retirar_vehiculo()
            input('Presiona Enter para continuar')

        case '4':
            print('*'*ESPACIADO)
            print('Panel de administrador'.center(ESPACIADO))
            admin.administrador()
            input('Presiona Enter para continuar')
        
        case '5':
            print('Gracias por usar UdeA iPark. Hasta pronto.')
            break

        case _:
            print('Opción incorrecta. Favor revisar (1-5)')
            input('Presiona Enter para continuar')
