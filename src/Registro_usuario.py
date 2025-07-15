import time
import Datos

def validar_datos(nombre:str, apellido:str, documento:str, placa:str)->bool:
    validar = True
    global error
    error = ""

    # Validación nombre
    if isinstance(nombre, str):
        if len(nombre) < 3:
            validar = False
            error += 'Error, el nombre es muy corto|\n'
        if not nombre.isalpha():
            validar = False
            error += 'Error, el nombre no debe contener números ni caracteres especiales|\n'
    else:
        validar = False
        error += 'Error, el nombre no es correcto|\n'
    
    # Validación apellido
    if isinstance(apellido, str):
        if len(apellido) < 3:
            validar = False
            error += 'Error, el apellido es muy corto|\n'
        if not apellido.isalpha():
            validar = False
            error += 'Error, el apellido no debe contener números ni caracteres especiales|\n'
    else:
        validar = False
        error += 'Error, el apellido no es correcto|\n'

    # Validación documento
    if isinstance(documento, str):
        if len(documento) < 3 or len(documento) > 15:
            validar = False
            error += 'Error, el documento es muy corto o muy largo|\n'
        if not documento.isdigit():
            validar = False
            error += 'Error, el documento solo permite números|\n'
    else:
        validar = False
        error += 'Error, el documento no es correcto|\n'

    # Validación placa 
    if isinstance(placa, str):
        if len(placa) != 6:
            validar = False
            error += 'Error, la placa debe tener exactamente 6 caracteres|\n'
        if not placa[0:3].isalpha() or not placa[3:6].isdigit():
            validar = False
            error += 'Error, la placa debe tener 3 letras y luego 3 números|\n'
    else:
        validar = False
        error += 'Error, la placa no es correcta|\n'

    return validar

def guardar_usuario (dic:dict, nombre: str, apellido:str, documento:str, placa:str):
    global error

    if isinstance(dic,dict):
        llaves = list(dic.keys())
        if documento in llaves:
            error += 'Error, el documento ya está registrado en el sistema|\n' 
            return False
        else:
            dic[documento] = {
                'Nombre': nombre,
                'Apellido': apellido,
                'Documento': documento,
                'Placa': placa.lower() 
            }
            return True
    else:
        error += 'Error en la base de datos|\n' 
        return False

def registrar_usuario():
    

    # Pedir datos
    nombre = input('Ingresar nombre'.ljust(18)+'--> ')
    apellido = input('Ingresar apellido'.ljust(18)+'--> ')
    documento = input('Ingresar documento'.ljust(18)+'--> ')
    placa = input('Ingresar placa'.ljust(18)+'--> ')

    # Validar datos
    if validar_datos(nombre, apellido, documento, placa):
        print('\nValidación correcta')

        # Guardar datos
        resultado = guardar_usuario(Datos.dicUsuarios, nombre, apellido, documento, placa)
        if resultado:
            for i in range(3):
                print('Guardando datos' + '.' * (i + 1), end = '\r')
                time.sleep(0.5)
            print('Datos guardados')
        else:
            print('Error, usuario ya registrado, vuelve a intentarlo')
            pass
    else:
        print(error)
        print('Favor corregir los datos, vuelve y registra los datos')
