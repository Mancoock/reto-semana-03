# 📊 Analizador de Ventas — Reto Semana 3

> **Programación para Ciencia de Datos · IPN ESCOM · Grupo 3AM1**

Pipeline de análisis financiero en **Python puro** que consume transacciones en CSV desde `stdin`, consolida métricas por producto y genera un reporte ordenado por ingreso total.

---

## 🗂️ Tabla de Contenidos

1. [Descripción](#-descripción)
2. [Características](#️-características)
3. [Estructura del Proyecto](#-estructura-del-proyecto)
4. [Formato de Datos](#-formato-de-datos)
5. [Instrucciones de Ejecución](#-instrucciones-de-ejecución)
6. [Ejemplo Completo](#-ejemplo-completo)
7. [Reglas de Validación](#-reglas-de-validación)
8. [Arquitectura del Código](#️-arquitectura-del-código)
9. [Datos Académicos](#-datos-académicos)

---

## 📋 Descripción

Este script procesa un flujo de transacciones de ventas en formato CSV a través de la entrada estándar (`stdin`). Agrupa los registros por producto usando diccionarios, calcula métricas financieras clave y presenta un reporte consolidado ordenado de mayor a menor ingreso.

El diseño prioriza la **robustez ante datos sucios**: el programa nunca colapsa por registros mal formateados; los filtra silenciosamente y continúa el procesamiento.

---

## ⚙️ Características

| Característica | Detalle |
|---|---|
| **Agrupación** | Consolida múltiples transacciones del mismo producto en un solo registro |
| **Métricas calculadas** | Unidades vendidas, ingreso bruto total y precio promedio ponderado |
| **Ordenamiento** | Reporte de mayor a menor ingreso total |
| **Tolerancia a fallos** | Descarta filas con valores no numéricos o estructura incorrecta |
| **Seguridad aritmética** | Previene `ZeroDivisionError` cuando las unidades válidas suman cero |

---

## 📁 Estructura del Proyecto

```
reto-semana3/
├── main.py              # Script principal
└── tests/
    └── entrada1.txt     # Archivo de prueba con datos mixtos (válidos e inválidos)
```

---

## 📐 Formato de Datos

### Entrada (`stdin`) — CSV con encabezado

```
fecha,producto,cantidad,precio_unitario
2026-04-01,Laptop,2,15000.00
2026-04-05,Teclado,10,800.00
```

| Columna | Tipo | Descripción |
|---|---|---|
| `fecha` | `string` | Fecha de la transacción (no se valida) |
| `producto` | `string` | Nombre del producto |
| `cantidad` | `int` | Unidades vendidas (debe ser entero) |
| `precio_unitario` | `float` | Precio por unidad |

### Salida (`stdout`) — CSV con reporte consolidado

```
producto,unidades_vendidas,ingreso_total,precio_promedio
Laptop,2,30000.00,15000.00
Teclado,10,8000.00,800.00
```

---

## 🚀 Instrucciones de Ejecución

> **Requisito:** Python 3.x instalado. No se necesitan dependencias externas.

### Ver el reporte en consola

```bash
python3 main.py < tests/entrada1.txt
```

### Exportar el reporte a un archivo CSV

```bash
python3 main.py < tests/entrada1.txt > reporte_salida.csv
```

### Pasar datos directamente desde la terminal

```bash
echo -e "fecha,producto,cantidad,precio_unitario\n2026-04-01,Laptop,2,15000.00" | python3 main.py
```

---

## 🧪 Ejemplo Completo

**Archivo de entrada (`tests/entrada1.txt`):**

```
fecha,producto,cantidad,precio_unitario
2026-04-01,Laptop,2,15000.00
2026-04-01,Mouse,,250.00          ← cantidad vacía → DESCARTADO
,,,,,                              ← 6 columnas → DESCARTADO
2026-04-02,Teclado,cinco,800.00   ← cantidad no numérica → DESCARTADO
2026-04-02,Monitor,1,             ← precio vacío → DESCARTADO
2026-04-03,Silla Gamer,2,4500.00,extra  ← 5 columnas → DESCARTADO
2026-04-04,Audifonos,Ocho,300.00  ← cantidad no numérica → DESCARTADO
2026-04-05,Teclado,10,800.00
2026-04-06,Monitor,3.5,6000.00   ← cantidad decimal → DESCARTADO
2026-04-08,Cable HDMI,0,150.00
```

**Salida esperada:**

```
producto,unidades_vendidas,ingreso_total,precio_promedio
Laptop,2,30000.00,15000.00
Teclado,10,8000.00,800.00
Cable HDMI,0,0.00,0.00
```

---

## 🛡️ Reglas de Validación

El programa aplica las siguientes reglas en orden al procesar cada línea:

```
1. ¿Tiene exactamente 4 columnas?  →  NO → DESCARTAR
2. ¿`cantidad` es un entero válido?  →  NO → DESCARTAR
3. ¿`precio_unitario` es un flotante válido?  →  NO → DESCARTAR
4. ¿`unidades` > 0?  →  NO → precio_promedio = 0.00 (evita ZeroDivisionError)
```

---

## 🏗️ Arquitectura del Código

El script sigue el principio de **responsabilidad única**: cada función hace una sola cosa.

```
main()
 ├── sys.stdin.readlines()       # Lectura de datos
 ├── agrupar_dic(lineas)
 │    └── parsear_linea(linea)   # Validación y parseo de cada fila
 ├── calcular_promedios(dic)     # Agrega precio_promedio al diccionario
 ├── ordenar_por_ingreso(dic)    # Retorna lista ordenada por ingreso desc.
 └── imprimir_reporte(lista)     # Imprime el CSV de salida
```

| Función | Entrada | Salida |
|---|---|---|
| `parsear_linea` | `str` (una línea CSV) | `tuple` o `None` |
| `agrupar_dic` | `list[str]` | `dict` con totales |
| `calcular_promedios` | `dict` | Modifica el dict in-place |
| `ordenar_por_ingreso` | `dict` | `list` ordenada desc. |
| `imprimir_reporte` | `list` | Imprime a `stdout` |

---

## 🎓 Datos Académicos

| | |
|---|---|
| **Autor** | Diego Jehu Bustamante Villanueva |
| **Institución** | Instituto Politécnico Nacional (IPN) |
| **Escuela** | Escuela Superior de Cómputo (ESCOM) |
| **Unidad de Aprendizaje** | Programación para Ciencia de Datos (PCD) |
| **Grupo** | 3AM1 |

---

<p align="center">
  Hecho con Python 🐍 · IPN ESCOM · 2026
</p>
