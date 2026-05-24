---
date: 2026-04-24
type: idea
tags:
  - idea
  - modelos-mentales
ai-first: true
---


#modelosmentales 
### Planeación

- Mision
- Objetivos
- Estrategias
- Procedimientos
- Programas
- Reglamento
- Presupuestos
- Politicas

## Organización

- Organigrama
- Descripción de puestos
- Instructivos Especiales

## Integración

- Reclutamiento
- Selección
- Contratación
- Inducción

## Dirección

- Contratación
- Motivación
- Liderazgo

## Control

- Fijación de Estandares
- Supervisión
- Instructivos Especiales.


=IF(E2=0, F2 - G2, REDUCE(F2, SEQUENCE(E2), LAMBDA(saldo_acumulado, mes, (saldo_acumulado * 1,05) - SUMIFS('Historial de Abonos'!D:D, 'Historial de Abonos'!A:A, A2, 'Historial de Abonos'!C:C, ">="&EDATE(D2, mes-1), 'Historial de Abonos'!C:C, "<"&EDATE(D2, mes)))))



=SI(E2=0; F2 - G2; REDUCE(F2; SECUENCIA(E2); LAMBDA(saldo_acumulado; mes; (saldo_acumulado * 1,05) - SUMAR.SI.CONJUNTO('Historial de Abonos'!D:D; 'Historial de Abonos'!A:A; A2; 'Historial de Abonos'!C:C; ">="&FECHA.MES(D2; mes-1); 'Historial de Abonos'!C:C; "<"&FECHA.MES(D2; mes)))))