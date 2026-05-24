---
date: 2026-05-22
type: meta
tags: [meta, critical]
ai-first: true
---

# Hechos Críticos — Cargar Siempre

> Este archivo se carga en cada sesión. Solo contiene hechos urgentes y de alto impacto que Claude necesita saber antes de cualquier conversación.

---

## 🔴 URGENTE — Reunión Aromaria el 27 de Mayo (en 5 días)

- Diego tiene una reunión con Rodrigo (dueño de Aromaria) el **martes 27 de mayo de 2026**
- En esa reunión **se decide si Diego es promovido** al nuevo equipo de IA de Aromaria
- Actualmente Diego es **Analista y Auditor de Calidad** en la nave operativa
- La promoción lo trasladaría a la **oficina administrativa**
- Diego debe presentar: qué ha hecho con IA + su visión para hacer Aromaria AI-first
- Ver plan completo en `[[Aromaria — Reunión 27 Mayo]]`

## 🔴 MVP — Workflow B casi listo (continuar el 24 de mayo)

- Workflow A (crear entradas PT) ✅ funciona end-to-end
- Workflow B (actualizar Ubicación actual) 🟡 CASI — un nodo falta configurar correctamente
- Apps Script ✅ dispara correctamente (fix: nueva URL del tunnel)
- Webhook n8n ✅ recibe los datos
- Nodo "Get items by column value" ✅ encuentra el contenedor (CONT-001 confirmado, id: `12091594700`)
- Nodo "Change a column value" ❌ da error — configuración incorrecta del valor
- **Próximo paso (INMEDIATO):** configurar el nodo "Change a column value" con exactamente:
  - Board ID: `18412458512`
  - Item ID: `{{ $json.id }}`
  - Column ID: `color_mm36nssa`
  - Value: `{"label": "Almacén PT"}` ← el formato JSON con "label" es crítico para columnas status
- **Tunnel activo:** `https://whenever-skill-pose-atom.trycloudflare.com` — levantar antes de probar
- 3 contenedores de prueba en Monday: CONT-001, CONT-002, CONT-003 (todos en "Producción")
- Ver spec completa y URLs en `[[Aromaria — MVP QR Form Monday]]`

---

## Contexto permanente

- Diego es **empleado de Aromaria**, no consultor externo
- Rodrigo es uno de los **dueños** de Aromaria Y el evaluador de la promoción
- Advanx y NearStream son proyectos paralelos **fuera** de Aromaria
- Lorena (pareja) — no crear notas en el vault, decisión explícita
