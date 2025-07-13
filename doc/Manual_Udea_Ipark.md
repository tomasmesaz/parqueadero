Manual de usuario - Udea Ipark
Sistema de gestión de parqueadero

Control de versiones

Contenido
Introducción
## 1. Objetivo
## 2. Alcance
## 3. Funcionalidad
Funciones y utilización del sistema
## 4. Prerrequisitos
## 5. Mapa de navegación
## 6. Paso a paso de cada opción del sistema

## 7. Solución de problemas

Manual de usuario

I. Introducción

El presente manual de usuario describe el funcionamiento del sistema UdeA iPark, una aplicación de consola desarrollada en Python para gestionar de manera eficiente un parqueadero universitario. En este documento se explica cómo interactuar con el sistema paso a paso, detallando sus funcionalidades, los requerimientos para su uso, y las instrucciones para realizar correctamente las operaciones disponibles.

UdeA iPark está diseñado para asistir de manera real y estructurada la operación diaria del parqueadero, facilitando el registro de usuarios, el control de ingreso y salida de vehículos, el cálculo de tarifas y la generación de reportes administrativos, todo desde un entorno interactivo por consola.

## 1. Objetivo
Brindar a los usuarios una guía práctica y estructurada para el uso correcto del sistema UdeA iPark, detallando sus principales funcionalidades y asegurando una interacción eficiente con el programa.

## 2. Alcance
Este manual está dirigido a los usuarios y administradores del sistema UdeA iPark, e incluye las instrucciones necesarias para su correcta operación desde la consola.

## 3. Funcionalidad
El programa permite gestionar de forma automatizada un parqueadero universitario a través de una interfaz por consola. Sus funcionalidades principales incluyen:
Registro de usuarios con validación de nombre, apellido, documento y placa del vehículo.
Ingreso de vehículos, solo si el usuario está registrado previamente.
Cálculo del tiempo de parqueo y del valor a pagar según horas y fracciones de hora.
Generación de recibos al momento del retiro del vehículo.
### 🔹 Módulo de administración protegido por usuario y contraseña, que permite consultar:
Vehículos registrados, retirados y activos.
Total recaudado.
Tiempo promedio de parqueo.
Usuario con mayor y menor tiempo de permanencia.
Exportación de reportes en formato CSV.
II. Funciones y utilización del sistema

## 4. Prerrequisitos para el uso del sistema
Entorno del sistema
Sistema operativo compatible: Windows, macOS o Linux.
Python instalado: Versión 3.8 o superior.

Este programa utiliza únicamente librerías estándar de Python, por lo tanto, no es necesario instalar paquetes externos.

El sistema está alojado en GitHub. Puedes clonar o descargar el repositorio desde el siguiente enlace:



## 5. Mapa de navegación

La pantalla principal del sistema, muestra el menú de inicio desde donde el usuario puede acceder a todas las funcionalidades del programa mediante un menú numérico interactivo. Cada opción representa un módulo específico del sistema:
## 1. Registro de nuevos usuarios.
## 2. Ingreso de vehículos al parqueadero.
## 3. Retiro de vehículos con cálculo de tarifa.
## 4. Acceso al panel de administración.
## 5. Salida del programa.
## 6. Paso a paso de cada opción del sistema
### 🔹 Módulo 1. Registrar usuario
Esta opción permite crear el registro de un usuario nuevo en el sistema. Para continuar, el sistema le pedirá que digite el nombre, apellido, documento de identidad del usuario y la placa del vehículo.

Al escribir los datos, asegúrese de:
Ingresar un nombre y apellido de al menos tres letras, sin números ni símbolos.
Digitar un documento entre 3 y 15 dígitos (solo números).
Escribir la placa en el formato correcto: tres letras seguidas de tres números (ejemplo: ABC123).
Una vez que todos los datos son válidos, el sistema confirmará que el registro fue exitoso. Después de este paso, podrá ingresar el vehículo al parqueadero usando su documento y placa.

Finalmente, presione ‘Enter’ para salir de este módulo y volver al menú principal.
### 🔹 Módulo 2. Ingresar vehículo

Al seleccionar la opción 2 en el menú principal, se ingresa al módulo de ‘Ingreso de vehículo’, donde se le pedirá el documento del usuario que está registrado en el sistema y la placa de su vehículo

Se le mostrará un mensaje de éxito y un tiquete que muestra la información del ingreso del vehículo

Presione la tecla ‘Enter’ para salir de este módulo, volverá al menú principal.

### 🔹 Módulo 3. Retiro del vehículo
Esta opción le permite retirar el vehículo del parqueadero. Para hacerlo, el sistema le pedirá que digite el documento de identidad del usuario y la placa del vehículo.

Asegúrese de:
Ingresar los mismos datos que usó cuando registró e ingresó el vehículo.
Verificar que el vehículo haya sido ingresado previamente al parqueadero.
El sistema calculará automáticamente el tiempo que el vehículo estuvo en el parqueadero y el valor a pagar. Luego, el sistema mostrará una factura de salida con todos los datos del vehículo, el tiempo total y el valor a pagar. También se liberará automáticamente el espacio que estaba ocupado por el vehículo.

Presione la tecla ‘Enter’ para salir de este módulo, volverá al menú principal.

### 🔹 Módulo 4. Administrador
Al seleccionar la opción 4 en el menú principal, se ingresa al módulo de ‘Administrador’, donde se solicita el nombre de usuario y la contraseña para validar el acceso.

Al ingresar correctamente el nombre de usuario y la contraseña en el módulo de Administrador, se accede a un panel exclusivo con funciones de consulta para la gestión del parqueadero UdeA iPark.

Al seleccionar la opción 1 en el menú del administrador, el sistema muestra el total de vehículos registrados en UdeA iPark hasta el momento.

Al seleccionar la opción 2 en el menú del administrador, el sistema muestra el total de vehículos retirados del parqueadero.

Al seleccionar la opción 3 en el menú del administrador, el sistema muestra el total de vehículos que aún no han sido retirados del parqueadero UdeA iPark.

Al seleccionar la opción 4 en el menú del administrador, el sistema muestra el total de dinero recaudado por concepto de parqueo, así como el número de pagos procesados.

Al seleccionar la opción 5 en el menú del administrador, el sistema muestra el tiempo promedio de estancia de los vehículos en el parqueadero UdeA iPark, calculado a partir de los registros de ingreso y retiro.

Al seleccionar la opción 6 en el menú del administrador, el sistema muestra la lista completa de usuarios registrados en el parqueadero, junto con su número de documento, nombre completo, placa del vehículo y estado actual (en parqueadero, retirado o solo registrado).

Al seleccionar la opción 7 en el menú del administrador, el sistema muestra los datos del vehículo con mayor y menor tiempo de parqueo en UdeA iPark. Para cada caso, se informa la placa, el tiempo total de permanencia, la fecha y hora de ingreso y salida.

Al seleccionar la opción 8 en el menú del administrador, el sistema finaliza la sesión administrativa y retorna al menú principal de UdeA iPark.

III. Información final

## 7. Solución de problemas

### 🔹 Módulo 1. Registrar usuario


### 🔹 Módulo 2. Ingresar vehículo


### 🔹 Módulo 3. Retirar vehículo


### 🔹 Módulo 4. Administrador




### 🔹 Módulo 1. Registrar usuario

Al seleccionar la opción 1 en el menú principal, se ingresa al módulo de Registro de usuario, donde el sistema le pedirá ingresar los siguientes datos:

- Nombre

- Apellido

- Documento de identidad

- Placa del vehículo



Para completar el registro correctamente, asegúrese de:

- Ingresar un nombre y apellido con al menos tres letras, sin números ni símbolos.

- Digitar un documento compuesto solo por números, con una longitud entre 3 y 15 dígitos.

- Escribir una placa de vehículo con el formato correcto: tres letras seguidas de tres números (por ejemplo: ABC123).



Si alguno de los datos no cumple con los requisitos, el sistema mostrará un mensaje de error y deberá volver a intentarlo.

Una vez el registro sea exitoso, podrá proceder con el ingreso del vehículo.



Presione la tecla Enter para salir de este módulo y volver al menú principal.



### 🔹 Módulo 2. Ingresar vehículo

Al seleccionar la opción 2 en el menú principal, se accede al módulo de Ingreso de vehículo. El sistema solicitará los siguientes datos:

- Documento de identidad del usuario registrado

- Placa del vehículo



Si los datos coinciden con un registro existente y hay espacio disponible, el vehículo será ingresado al parqueadero.

A continuación, se mostrará un tiquete en pantalla con la información del ingreso, incluyendo hora, placa, nombre del usuario y número del espacio asignado.



Si no hay espacios disponibles o los datos no coinciden, se mostrará un mensaje de advertencia.



Presione la tecla Enter para salir de este módulo y volver al menú principal.



### 🔹 Módulo 3. Retirar vehículo

Al seleccionar la opción 3 en el menú principal, se accede al módulo de Retiro de vehículo. Para continuar, el sistema le pedirá:

- Documento del usuario

- Placa del vehículo



Asegúrese de ingresar los mismos datos utilizados al momento del ingreso.

Si los datos son correctos, el sistema calculará automáticamente el tiempo que el vehículo estuvo en el parqueadero y mostrará una factura con:

- Datos del usuario

- Tiempo total de permanencia

- Valor a pagar

- Espacio liberado



Presione la tecla Enter para salir de este módulo y volver al menú principal.



### 🔹 Módulo 4. Administrador

Al seleccionar la opción 4 en el menú principal, se accede al módulo de Administrador. El sistema le solicitará un nombre de usuario y una contraseña.



Si los datos ingresados son válidos, se mostrará un menú exclusivo con las siguientes opciones:

## 1. Ver el total de vehículos registrados.

## 2. Ver el total de vehículos retirados.

## 3. Ver el total de vehículos aún en el parqueadero.

## 4. Ver el total recaudado por parqueo.

## 5. Ver el tiempo promedio de permanencia.

## 6. Ver la lista de usuarios registrados.

## 7. Ver el vehículo con mayor y menor tiempo de parqueo.

8. Salir del panel de administración.



Seleccione la opción deseada según su consulta.

Presione la tecla Enter para continuar o regresar al menú principal.