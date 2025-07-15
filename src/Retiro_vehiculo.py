import Datos
import time
from datetime import datetime
import Ingreso_vehiculo as ingreso

def retirar_vehiculo():
    
    documento = input('Ingresar documento'.ljust(18) + '--> ')
    placa = input('Ingresar placa'.ljust(18)+'--> ')

    if ingreso.validar_placa(Datos.dicUsuarios, documento, placa):
        print('\nDocumento y placa correctos, bienvenido al sistema')

        # Retiro del vehículo
        # Datos necesario
        hora_salida_impresion = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        hora_salida = time.time()
        hora_ingreso = float(Datos.dicUsuarios[documento]['Hora ingreso segundos'])
        nombre_usuario = Datos.dicUsuarios[documento]['Nombre']
        apellido_usuario = Datos.dicUsuarios[documento]['Apellido']
        espacio_liberado = int(Datos.dicUsuarios[documento]['Espacio'])

        #Cálculo del tiempo de parqueo
        duracion = hora_salida - hora_ingreso
        minutos = duracion / 60
        horas = int(minutos // 60)
        minutos_restantes = minutos % 60
        cuartos = int((minutos_restantes + 14) // 15) 

        # Cálculo total a pagar
        totalpago = (horas * 7000) + (cuartos * 1500)
        if totalpago < 7000:
            totalpago = 7000
        
        # Guardar datos de salida
        Datos.dicUsuarios[documento]['Hora salida impresión'] = hora_salida_impresion
        Datos.dicUsuarios[documento]['Hora salida segundos'] = str(round(hora_salida, 0))
        Datos.dicUsuarios[documento]['Tiempo estancia segundos'] = str(int(duracion)) 
        Datos.dicUsuarios[documento]['Tiempo estancia minutos'] = str(int(minutos))    
        Datos.dicUsuarios[documento]['Total pagado'] = str(totalpago)

        # Liberar espacio
        if 'Espacio' in Datos.dicUsuarios[documento]:
            del Datos.dicUsuarios[documento]['Espacio']
        Datos.espacios.append(espacio_liberado)
        Datos.espacios.sort()
        
        # Factura 
        print('\n' + '='*64)
        print('FACTURA DE SALIDA - UdeA iPark'.center(64))
        print('='*64)
        print(f'Usuario: {nombre_usuario} {apellido_usuario}')
        print(f'Documento: {documento}')
        print(f'Placa: {placa.upper()}')
        print(f'Espacio liberado: {espacio_liberado}')
        print('-'*64)
        print(f'Hora de ingreso: {Datos.dicUsuarios[documento]['Hora ingreso impresión']}')
        print(f'Hora de salida: {hora_salida_impresion}')
        print(f'Tiempo total: {horas} horas y {int(minutos_restantes)} minutos')
        print('-'*64)
        print(f'Total a pagar: ${totalpago:,.0f}')
        print('='*64)
        print('¡Gracias por usar UdeA iPark!'.center(64))

    else:
        print(ingreso.error)
        print('Favor verificar los datos')
