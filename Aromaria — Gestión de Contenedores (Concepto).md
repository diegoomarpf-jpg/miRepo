---
date: 2026-05-26
type: project
tags: [aromaria, contenedores, trazabilidad, monday, n8n, diseño-operativo]
related-projects:
  - "[[Aromaria — MVP QR Form Monday]]"
  - "[[MasterPlanAromaria/3 Quick Wins técnicos]]"
  - "[[MasterPlanAromaria/Backlog Estrátegico]]"
related-people:
  - "[[Rodrigo]]"
ai-first: true
confidence: high
---

## Para el futuro Claude

Esta nota captura el **diseño conceptual y las historias de usuario** del sistema de gestión de contenedores en la nave de Aromaria (al 2026-05-26). Es distinta de `[[Aromaria — MVP QR Form Monday]]` que es el devlog técnico de construcción. Esta nota responde a: ¿qué problema resuelve el sistema y cómo funciona en el día a día para cada persona en la empresa? Úsala para presentaciones, alineación de expectativas con [[Rodrigo]], o para retomar el proyecto desde cero sin perder la visión.

---

# Gestión de Contenedores — Diseño Conceptual

## El principio de diseño central

> **El operario no "registra en el sistema". Él confirma que terminó su tarea. La trazabilidad es el subproducto automático de esa confirmación.**

La diferencia es crítica: un sistema que le pide al operario "capturar datos" requiere capacitación, genera resistencia y produce errores. Un sistema que le pide al operario "confirmar que hicieron su trabajo" es natural, rápido y no requiere entender nada del backend.

**Consecuencia de diseño:** El punto de contacto entre el operario y el sistema debe ser lo más pequeño posible. Máximo 2-3 campos. Pre-llenados en lo posible. Sin pantallas de login ni menús. Sin entender qué es Monday.

---

## Qué es un "contenedor" en este sistema

Un contenedor es la **unidad de trazabilidad física** de la nave. Cada recipiente, lote o unidad de producción que se mueve entre estaciones tiene un QR pegado. Ese QR es su identidad digital.

El sistema sabe en qué etapa del proceso está cada contenedor porque los propios operarios lo informaron — sin saberlo — al escanear el QR al llegar a cada zona.

---

## Los macroprocesos (etapas del flujo)

Cada etapa del flujo productivo tiene su propio QR físico en la nave. El operario escanea el QR de la **zona donde está trabajando**, no el del contenedor (o viceversa, según el diseño final). Las etapas son:

1. Recepción de Insumos
2. Producción / Mezcla
3. Llenado / Envasado
4. Control de Calidad
5. Almacén de Producto Terminado
6. Despacho

Un contenedor "vive" en una sola etapa a la vez. Cuando avanza, el operario lo registra con un escaneo. El tablero de Monday se actualiza automáticamente.

---

## Historias de usuario

### El operario de nave

> **"No necesito saber qué es Monday para que Monday sepa dónde estoy."**

- **Como operario**, quiero escanear el QR de mi zona de trabajo y ver un formulario que ya sabe qué contenedor estoy moviendo, para no tener que escribir nada o cometer errores de captura.
- **Como operario**, quiero que el formulario tenga máximo 2-3 campos con opciones predefinidas (no texto libre), para poder completarlo en 10 segundos desde mi celular sin pensar.
- **Como operario**, quiero recibir una confirmación visual inmediata de que mi registro fue exitoso, para saber que hice mi parte y seguir con mi trabajo.
- **Como operario**, no quiero necesitar capacitación para usar el sistema — si necesito explicación, el sistema está mal diseñado.

### El supervisor / equipo de producción

> **"Ver el estado de la nave sin preguntar a nadie."**

- **Como supervisor**, quiero ver en tiempo real cuántos contenedores hay en cada etapa del proceso, para saber si hay un cuello de botella sin tener que caminar por la nave.
- **Como supervisor**, quiero que el sistema me alerte si un contenedor lleva más tiempo del normal en una etapa, para intervenir antes de que el retraso afecte la producción.
- **Como supervisor**, quiero ver el historial de movimientos de cualquier contenedor específico, para investigar incidentes de calidad o producción.

### Rodrigo — el dueño

> **"Preguntar en WhatsApp y recibir datos reales."**

- **Como dueño**, quiero poder preguntar "¿cuántos contenedores están en Producción ahorita?" y recibir una respuesta en segundos, sin abrir Monday ni interrumpir a nadie.
- **Como dueño**, quiero que el sistema funcione sin que yo tenga que recordarle a los operarios que lo usen — debe ser tan simple que se convierta en hábito natural.
- **Como dueño**, quiero poder rastrear un lote específico si hay un reclamo de calidad: quién lo trabajó, en qué etapa, en qué fecha.
- **Como dueño**, quiero ver un dashboard que muestre el flujo completo de la nave de un vistazo, sin interpretación — verde es fluido, rojo es atascado.

---

## Lo que el operario VE vs. lo que el sistema HACE

| Lo que el operario ve | Lo que el sistema hace detrás |
|---|---|
| Un QR en la pared de su zona | Codifica la URL del formulario con el ID del contenedor pre-llenado |
| Un formulario de 2 campos en su celular | Dispara un webhook en n8n al enviarse |
| "Registro exitoso ✓" | n8n busca el contenedor en Monday por ID y actualiza su "Ubicación actual" |
| Nada más | Monday actualiza automáticamente tableros relacionados (inventario, costos, dashboard) |

**La complejidad es invisible para quien no la necesita. La información es visible para quien la necesita.**

---

## Por qué este diseño resuelve el problema real de Aromaria

El dolor raíz de Aromaria no es falta de herramientas — es falta de datos confiables. Los procesos existen pero no se registran porque registrarlos es más difícil que no hacerlo.

Este diseño invierte esa ecuación: **registrar debe ser más fácil que no registrar**.

Cuando escanear el QR y enviar el form toma 10 segundos y es parte natural del flujo de trabajo (el operario ya está en esa zona, ya terminó esa tarea), el registro ocurre sin fricción. El sistema se alimenta solo.

---

## Relación con el MVP técnico

La implementación en construcción está documentada en `[[Aromaria — MVP QR Form Monday]]`:
- Workflow A (crear entradas PT): ✅ funcionando
- Workflow B (actualizar ubicación de contenedores CONT-001/002/003): pendiente fix del nodo Monday — solución Code + HTTP Request lista para probar (al 2026-05-26)

Esta nota es el "por qué" y el "qué". El devlog es el "cómo".
