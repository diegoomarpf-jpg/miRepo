---
date: 2026-05-18
type: devlog
tags:
  - devlog
  - michiahorrador
ai-first: true
---

#michiahorrador 

# Documentación del Proyecto: Motor de Intereses sobre Saldos Insolutos (Python + Google Sheets)

## 1. Objetivo del Proyecto

Automatizar el cálculo de deuda para una cartera de préstamos, aplicando dos reglas de negocio específicas:

- **Interés de Apertura:** Cargo único del **5%** sobre el capital base al momento de originar el préstamo.
- **Interés sobre Saldos Insolutos:** Cargo mensual recurrente del **5%** aplicado sobre el saldo pendiente del mes anterior, después de haber descontado los abonos realizados.

## 2. Requisitos del Sistema y Herramientas

Para ejecutar este script, se requieren las siguientes herramientas:

- **Entorno de Ejecución:** Python 3.9 o superior.
- **Bibliotecas (Libraries):**
    
    - `pandas`: Para la manipulación y estructuración de los datos en DataFrames.
    - `gspread`: Para la conexión y escritura/lectura directa con la API de Google Sheets.
    - `google-auth`: Para gestionar las credenciales de servicio de Google Cloud.
    
- **Google Cloud Console:** Es necesario un archivo `credentials.json` (Service Account) con permisos de edición sobre las hojas de cálculo.

## 3. Estructura de Datos (Inputs)

El script espera encontrar un libro de Google Sheets con al menos dos pestañas:

| Tabla         | Columnas Requeridas                                        | Propósito                     |
| ------------- | ---------------------------------------------------------- | ----------------------------- |
| **Préstamos** | `ID_Prestamo`, `Miembro`, `Monto_Original`, `Fecha_Inicio` | Registro maestro del crédito. |
| **Abonos**    | `ID_Abono`, `ID_Prestamo`, `Monto_Abono`, `Fecha_Abono`    | Historial de pagos recibidos. |

Exportar a Hojas de cálculo

## 4. Lógica de Negocio y Algoritmo

El script seguirá un proceso recursivo para cada préstamo individual:

1. **Inicialización (Mes0​):**
    Saldo0​=Capital×1.05
2. **Iteración Mensual (Mesn​):** El script detectará los meses transcurridos entre `Fecha_Inicio` y la fecha actual. Para cada mes:
    
    - Identifica abonos realizados en ese periodo de tiempo.
    - Calcula el interés del periodo: In​=Saldon−1​×0.05.
    - Calcula el nuevo saldo: Saldon​=(Saldon−1​+In​)−Abonosn​.

3. **Corte de Datos:** El proceso se repite hasta llegar al mes presente o hasta que el saldo sea ≤0.


## 5. Salida del Proceso (Outputs)

El script generará una nueva pestaña en Google Sheets llamada **"Estado_Cuenta_Maestro"**. Esta tabla tendrá un formato de **Libro Diario**, donde cada fila será un "evento" (un cargo de interés o un abono), permitiendo que Power BI simplemente sume la columna `Monto` para obtener la deuda real a cualquier fecha.



Las insignias si se pueden otrogar mas de una vez a un miembro.

Detecté una diferencia en el archivo de modelado de datos. Y es que está haciendo los cálculos de intereses sobre los préstamos considerar que cada préstamo nace ya con un 5% de interés. Es como la taza de apertura. El aumento en el que se le presta ya debe el 5% de interés más. A partir de ahí cada mes se aumenta un 5% de interés a los saldos insolutos. Aclarar esta cuestión en el modelado. 

Para la insignia Michi Alcancía. Se debe tomar en cuenta la meta anual de ahorro de cada miembro, la cual yo les pregunté al inicio de la caja. Y se otorga la insignia de michi alcancía en cuanto el miembro alcance ese monto de ahorro. Puede ser hasta el final del año o puede ser antes si aporta más. Si por alguna razón un miembro no definió cuánto es este monto anual de ahorro tomará por defecto su monto michi multiplicado por el total de las semanas del ciclo.

La insignia de Michi Fertilizador se otorga a aquellos miembros que han aportado intereses por su préstamo por más de 3 meses consecutivos. 

Para la vista corte de caja, también es útil añadir el total de intereses que se han generado. 



Listo solo le añadi un valor de 10 XP a michi alcancia y 5 XP a michi fertilizador.



 allow_origins=[

        "http://localhost:3000",   # Panel web en desarrollo

        "http://localhost:5173",   # Vite dev server (alternativo)

    ]



python -m uvicorn main:app --reload --port 8000


npm run dev


cd C:\Users\1544\Documents\michi-ahorrador\michi-api
.\venv\Scripts\python.exe -m uvicorn main:app --reload

cd C:\Users\1544\Documents\michi-ahorrador\michi-panel 
npm run dev












