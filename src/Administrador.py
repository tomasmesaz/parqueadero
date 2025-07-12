import Datos

# Lista de administradores
admins = {'SEBAS':'2309',
          'TOMAS':'3141',
          'REBE':'0107',
          'PROFE':'1234'}

#Validar administrador 
def validar_admin():
    usuario = input('Usuario administrador: ').upper()
    clave = input('Contraseña administrador: ')
    
    if usuario in admins and admins[usuario] == clave:
        print(f'\nBienvenido administrador {usuario}')
        return True
    else:
        print('\nUsuario o contraseña incorrectos')
        return False

#Mostrar menú de administrador
def imprimir_menu_admin():
    print('\n** Menú administrador **')
    print('1 --> Total de vehículos registrados')
    print('2 --> Total de vehículos retirados')
    print('3 --> Total de vehículos sin retirar')
    print('4 --> Total pago de vehículos retirados')
    print('5 --> Tiempo promedio de estancia por vehículo')
    print('6 --> Lista de usuarios')
    print('7 --> Vehículo con máximo y mínimo tiempo de parqueo')
    print('8 --> Salir')

#Definir funciones para cada opción del menú
#Opción 1: Total de vehículos registrados
def total_vehiculos_registrados():
    total = len(Datos.dicUsuarios)
    print(f'\nTotal de vehículos registrados: {total}')
    return total

#Opción 2: Total de vehículos retirados
def total_retirados():
    contador = 0
    for usuario in Datos.dicUsuarios.values():
        if 'Hora salida segundos' in usuario:
            contador += 1
    print(f'\nTotal de vehículos retirados: {contador}')
    return contador

#Opción 3: Total de vehículos sin retirar
def total_sin_retirar():
    contador = 0
    for usuario in Datos.dicUsuarios.values():
        if 'Hora salida segundos' not in usuario:
            contador += 1
    print(f'\nTotal de vehículos sin retirar: {contador}')
    return contador

#Opción 4: Total pago de vehículos retirados
def total_pago():
    total_pago = 0
    contador_pagos = 0
    
    for usuario in Datos.dicUsuarios.values():
        if 'Total pagado' in usuario:
            total_pago += float(usuario['Total pagado'])
            contador_pagos += 1
    
    print(f'\nTotal recaudado: ${total_pago:,.0f}')
    print(f'Número de pagos procesados: {contador_pagos}')
    return total_pago

#Opción 5: Tiempo promedio 
def tiempo_promedio():
    tiempo_total = 0
    cantidad = 0
    
    for usuario in Datos.dicUsuarios.values():
        if 'Tiempo estancia minutos' in usuario:
            tiempo_total += int(usuario['Tiempo estancia minutos'])
            cantidad += 1
    
    if cantidad > 0:
        promedio = tiempo_total / cantidad
        horas = int(promedio // 60)
        minutos = int(promedio % 60)
        print(f'\nTiempo promedio de estancia: {horas} horas y {minutos} minutos')
        print(f'Vehículos analizados: {cantidad}')
        return promedio
    else:
        print('\nNo hay vehículos retirados para calcular promedio')
        return 0

#Opcion 6: Lista de usuarios
def lista_usuarios():

    print('\nLista de usuarios')

    for documento, usuario in Datos.dicUsuarios.items():
        nombre = usuario['Nombre']
        apellido = usuario['Apellido']
        placa = usuario['Placa']

        if 'Espacio' in usuario:
            estado = f'En parqueadero (Espacio: {usuario['Espacio']})'
        elif 'Hora salida segundos' in usuario:
            estado = 'Retirado'
        else:
            estado = 'Solo registrado'
        
        print('|', documento.center(15), '|'.center(3), (nombre+' '+apellido).center(25), '|', placa.center(8), '|'.center(3), estado, sep = '')

#Opcion 7: Vehículo con tiempo de parqueo máximo y mínimo
def vehiculo_max_min_tiempo():
    vehiculos_con_tiempo = []

    for usuario in Datos.dicUsuarios.values():
        if 'Tiempo estancia segundos' in usuario:
            tiempo = int(usuario['Tiempo estancia segundos'])
            vehiculos_con_tiempo.append([tiempo, usuario])

    vehiculos_con_tiempo.sort()

    vehiculo_min = vehiculos_con_tiempo[0][1]
    vehiculo_max = vehiculos_con_tiempo[-1][1]
    tiempo_min = vehiculos_con_tiempo[0][0]
    tiempo_max = vehiculos_con_tiempo[-1][0]

    print(f'\nVehículo con mayor tiempo de parqueo')
    print('-' * 40)
    print(f'Placa: {vehiculo_max['Placa']}')
    print(f'Tiempo: {tiempo_max // 3600}h {(tiempo_max % 3600) // 60}min')
    print(f'Ingreso: {vehiculo_max['Hora ingreso impresión']}')
    print(f'Salida: {vehiculo_max['Hora salida impresión']}')
    
    print(f'\nVehículo con menor tiempo de parqueo')
    print('-' * 40)
    print(f'Placa: {vehiculo_min['Placa']}')
    print(f'Tiempo: {tiempo_min // 3600}h {(tiempo_min % 3600) // 60}min')
    print(f'Ingreso: {vehiculo_min['Hora ingreso impresión']}')
    print(f'Salida: {vehiculo_min['Hora salida impresión']}')

#Función final
def administrador():
    if validar_admin():
        while True:
            imprimir_menu_admin()
            opcion = input('Seleccione una opción (1-8) --> ')
            
            match opcion:
                case '1':
                    total_vehiculos_registrados()
                    
                case '2':
                    total_retirados()
                    
                case '3':
                    total_sin_retirar()
                    
                case '4':
                    total_pago()
                    
                case '5':
                    tiempo_promedio()
                    
                case '6':
                    lista_usuarios()
                    
                case '7':
                    vehiculo_max_min_tiempo()
                    
                case '8':
                    print('\nSaliendo del panel de administrador...')
                    break
                    
                case _:
                    print('Opción inválida --> Seleccione 1-8')

            input('Presiona Enter para continuar')