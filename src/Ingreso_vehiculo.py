import Datos
import time 
from datetime import datetime

def validar_placa(dic:dict, documento:str, placa:str)->bool:
    validar = True
    global error
    error = ''

    llaves = list(dic.keys())

    if documento in llaves:
        clave = dic[documento]['Placa']
        if clave.upper() == placa.upper():
            validar = True
        else:
            validar = False
            error += 'Error, la placa no se encuentra en el sistema|\n'
    else:
        validar = False
        error += 'Error, el documento no se encuentra registrado en el sistema|\n'
    return validar

def ingresar_vehiculo(): 
    
    documento = input('Ingresar documento'.ljust(18) + '--> ')
    placa = input('Ingresar placa'.ljust(18)+'--> ')
    
    if validar_placa(Datos.dicUsuarios, documento, placa):
        print('\nDocumento y placa correctos, bienvenido al sistema')

        # Buscar espacio libre
        if len(Datos.espacios) == 0:
            print('El parqueadero está lleno. No hay espacio disponibles')
            print('Regrese más tarde')
        else:
            espacio_asignado = Datos.espacios.pop(0)
            
            # Guardar hora ingreso y espacio asignado 
            Datos.dicUsuarios[documento]['Hora ingreso impresión'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            Datos.dicUsuarios[documento]['Hora ingreso segundos'] = str(round(time.time(),0))
            Datos.dicUsuarios[documento]['Espacio'] = str(espacio_asignado)

            # Imprimir tiquete de ingreso 
            print('\n' + '='*64)
            print('Tiquete de ingreso'.center(64))
            print('='*64)
            print(f'Placa: {placa.upper()}')
            print(f'Usuario: {Datos.dicUsuarios[documento]["Nombre"]} {Datos.dicUsuarios[documento]["Apellido"]}')
            print(f'Hora de entrada: {Datos.dicUsuarios[documento]["Hora ingreso impresión"]}')
            print(f'Espacio asignado: {Datos.dicUsuarios[documento]["Espacio"]}')
            print('='*64)
    
    else:
        print(error)
        print('Favor verificar los datos')
