# 🏨 Sistema de Gestión de Reservas de Hotel

## 📖 Descripción

Sistema desarrollado en Python para administrar reservas de un hotel mediante un menú interactivo.

El programa permite registrar, buscar, actualizar y eliminar reservas, además de mostrar estadísticas generales del sistema.

Este proyecto fue desarrollado como ejercicio práctico para reforzar los contenidos de:

* Listas
* Diccionarios
* Funciones
* Validaciones
* Manejo de excepciones
* Ciclos repetitivos
* Estructuras condicionales

---

## 🚀 Funcionalidades

### 1. Registrar reserva

Permite registrar una nueva reserva solicitando:

* Código de reserva
* Nombre del huésped
* Cantidad de noches
* Valor por noche

El sistema calcula automáticamente:

* Total de la reserva
* Categoría de la reserva

### 2. Buscar reserva

Permite buscar una reserva mediante su código y mostrar todos sus datos.

### 3. Actualizar reserva

Permite modificar:

* Nombre del huésped
* Cantidad de noches
* Valor por noche

Recalculando automáticamente el total y la categoría.

### 4. Eliminar reserva

Permite eliminar una reserva existente mediante su código.

### 5. Mostrar reservas

Muestra todas las reservas registradas en el sistema.

### 6. Mostrar estadísticas

Entrega información general del hotel:

* Cantidad total de reservas
* Ingresos totales
* Reserva de mayor valor
* Promedio de ingresos por reserva

### 7. Salir

Finaliza la ejecución del programa.

---

## 📋 Categorías de Reserva

| Categoría | Condición                       |
| --------- | ------------------------------- |
| Económica | Total menor a $200.000          |
| Estándar  | Total entre $200.000 y $500.000 |
| Premium   | Total superior a $500.000       |

---

## 🛠 Tecnologías Utilizadas

* Python 3
* Diccionarios
* Listas
* Funciones
* Manejo de excepciones

---

## 📂 Estructura de los Datos

Cada reserva se almacena en un diccionario con la siguiente estructura:

```python
{
    "codigo": "R001",
    "nombre": "Juan Pérez",
    "noches": 3,
    "valor_noche": 80000,
    "total": 240000,
    "categoria": "Estándar"
}
```

Todas las reservas se almacenan dentro de una lista.

---

## ▶️ Ejecución

1. Descargar o clonar el proyecto.
2. Abrir una terminal.
3. Ejecutar:

```bash
python main.py
```

---

## 🎯 Objetivo Académico

Proyecto orientado al aprendizaje de estructuras de datos y programación modular utilizando Python.

---

## 👨‍💻 Autor

José Muñoz Núñez <br>
Matias Tranamil

## Colaboracion Docente

Fabian Saldano Perez<br>
Estudiante de Ingeniería en Informática - Duoc UC

