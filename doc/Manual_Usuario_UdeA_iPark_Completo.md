
# Manual de Usuario - UdeA iPark 🚗

Sistema de gestión de parqueadero

---

## 📌 Control de versiones

| Versión | Fecha             | Descripción       | Responsable(s)                      |
|---------|-------------------|-------------------|--------------------------------------|
| 1.0     | 12 de julio de 2025 | Versión inicial del manual | Tomás Mesa, Sebastián Ríos, Rebeca Rodríguez |

---

## 📚 Contenido

1. [Introducción](#1-introducción)
2. [Funciones y utilización del sistema](#2-funciones-y-utilización-del-sistema)
3. [Información final](#3-información-final)

---

## 1. Introducción

UdeA iPark es una aplicación de consola desarrollada en Python para gestionar eficientemente un parqueadero universitario.

### 1.1 Objetivo

Brindar a los usuarios una guía práctica para el uso del sistema, detallando sus funcionalidades.

### 1.2 Alcance

Dirigido a usuarios y administradores, con instrucciones para operar el sistema desde la consola.

### 1.3 Funcionalidad

- Registro de usuarios
- Ingreso y salida de vehículos
- Cálculo de tarifas
- Módulo administrativo con estadísticas y exportación de reportes

---

## 2. Funciones y utilización del sistema

### 2.1 Prerrequisitos

- Sistema operativo: Windows, macOS o Linux
- Python 3.8 o superior
- Librerías estándar de Python

Repositorio oficial: [GitHub - tomasmesaz/parqueadero](https://github.com/tomasmesaz/parqueadero)

### 2.2 Mapa de navegación

1. Registro de nuevos usuarios  
2. Ingreso de vehículos  
3. Retiro de vehículos  
4. Acceso al panel de administración  
5. Salida del programa

### 2.3 Paso a paso de cada módulo

#### 🔹 Módulo 1: Registrar usuario

Datos requeridos:
- Nombre
- Apellido
- Documento
- Placa

Validaciones:
- Nombre/Apellido ≥ 3 letras, sin números
- Documento: 3 a 15 dígitos
- Placa: formato `ABC123`

#### 🔹 Módulo 2: Ingresar vehículo

Datos requeridos:
- Documento
- Placa

El sistema verifica si el usuario está registrado y hay cupo disponible.

#### 🔹 Módulo 3: Retirar vehículo

Datos requeridos:
- Documento
- Placa

Se calcula el tiempo de parqueo y se muestra la factura con valor a pagar.

#### 🔹 Módulo 4: Panel del administrador

Se requiere autenticación (usuario y contraseña).  
Opciones disponibles:
1. Total registrados  
2. Total retirados  
3. Vehículos activos  
4. Total recaudado  
5. Tiempo promedio de permanencia  
6. Lista de usuarios  
7. Mayor y menor tiempo de parqueo  
8. Salir

---

## 3. Información final

### 3.1 Solución de problemas

Consulta la tabla de errores en el PDF original para mensajes comunes como:

- `"Error, el nombre es muy corto"` → Usa mínimo 3 letras  
- `"El documento ya está registrado"` → Usa un número no duplicado  
- `"El parqueadero está lleno"` → Espera que haya un espacio disponible  
- `"Usuario o contraseña incorrectos"` → Verifica las credenciales

---

> Manual generado para el sistema UdeA iPark por Tomás Mesa, Sebastián Ríos y Rebeca Rodríguez.

---

## 🛠️ Tabla de errores y solución de problemas

### 🔹 Módulo 1: Registrar usuario

| Mensaje de error | Razón | Solución sugerida |
|------------------|-------|-------------------|
| Error, el nombre es muy corto | El nombre tiene menos de 3 letras | Escriba un nombre con mínimo 3 letras |
| Error, el nombre no debe contener números ni caracteres especiales | El nombre contiene símbolos o números | Ingrese solo letras |
| Error, el nombre no es correcto | El valor ingresado no es texto válido | Asegúrese de digitar un texto válido como nombre |
| Error, el apellido es muy corto | El apellido tiene menos de 3 letras | Escriba un apellido con mínimo 3 letras |
| Error, el apellido no debe contener números ni caracteres especiales | El apellido contiene símbolos o números | Ingrese solo letras |
| Error, el apellido no es correcto | El valor ingresado no es texto válido | Asegúrese de digitar un texto válido como apellido |
| Error, el documento es muy corto o muy largo | El documento tiene menos de 3 o más de 15 caracteres | Ingrese un número de documento entre 3 y 15 dígitos |
| Error, el documento sólo permite números | El documento contiene letras o símbolos | Ingrese solo números |
| Error, el documento no es correcto | El valor ingresado no es texto válido | Asegúrese de digitar un número válido |
| Error, la placa debe tener exactamente 6 caracteres | La placa no tiene 6 caracteres | Asegúrese de que la placa tenga exactamente 6 caracteres |
| Error, la placa debe tener 3 letras y luego 3 números | La placa no cumple con el formato LLLNNN | Ingrese una placa como ABC123 |
| Error, la placa no es correcta | El valor ingresado no es una cadena válida | Verifique que la placa cumpla el formato requerido |
| Error, el documento ya está registrado en el sistema | Documento duplicado | Ingrese uno que no esté registrado |

---

### 🔹 Módulo 2: Ingresar vehículo

| Mensaje de error | Razón | Solución sugerida |
|------------------|-------|-------------------|
| Error, el documento no se encuentra registrado en el sistema | Documento no está en la base de datos | Regístrese primero |
| Error, la placa no se encuentra en el sistema | La placa no coincide con la registrada para el documento | Verifique que haya escrito correctamente la placa |
| El parqueadero está lleno. No hay espacios disponibles | Todos los espacios están ocupados | Espere a que se libere un espacio |

---

### 🔹 Módulo 3: Retirar vehículo

| Mensaje de error | Razón | Solución sugerida |
|------------------|-------|-------------------|
| Error, el documento no se encuentra registrado en el sistema | El documento no existe en la base de datos | Verifique si el usuario fue registrado e ingresado |
| Error, la placa no se encuentra en el sistema | La placa no coincide con el documento | Ingrese la placa correctamente |
| Favor verificar los datos | Documento o placa inválidos | Revise los datos y vuelva a intentarlo |

---

### 🔹 Módulo 4: Administrador

| Mensaje de error | Razón | Solución sugerida |
|------------------|-------|-------------------|
| Usuario o contraseña incorrectos | Credenciales inválidas | Verifique que estén bien escritos |
| Opción inválida --> Seleccione 1-8 | Número fuera de rango o caracter inválido | Ingrese solo un número entre 1 y 8 |
| No hay vehículos retirados para calcular promedio | No hay registros de salida | Retire al menos un vehículo antes de usar esta opción |

---
