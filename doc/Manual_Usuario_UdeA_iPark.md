
# Manual de Usuario - UdeA iPark 

Sistema de gestión de parqueadero

---

## Control de versiones

| Versión | Fecha             | Descripción       | Responsable(s)                      |
|---------|-------------------|-------------------|--------------------------------------|
| 1.0     | 12 de julio de 2025 | Versión inicial del manual | Tomás Mesa, Sebastián Ríos, Rebeca Rodríguez |

---

## Contenido

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
