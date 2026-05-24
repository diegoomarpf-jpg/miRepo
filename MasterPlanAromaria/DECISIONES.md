# Registro de Decisiones — Aromaria

> Este archivo documenta las decisiones importantes del proyecto, con su contexto y razonamiento.
> Formato: **Decisión** → Por qué → Alternativas descartadas

---

## 2026-05-09 — Stack Tecnológico: La Triple Alianza

**Decisión:** Usar Monday.com + n8n + Claude como stack principal.

**Por qué:**
- Monday actúa como base de datos relacional con UI visual, accesible para no-técnicos
- n8n conecta las operaciones físicas (escaneo QR) con Monday sin intervención humana
- Claude funciona como analista 24/7 que interpreta los datos y responde preguntas en lenguaje natural

**Alternativas descartadas:**
- Zapier en lugar de n8n: más caro y menos flexible para automatizaciones complejas
-  Monday: Es la plataforma ya usada en la empresa. 
- Dashboard estático: no permite consultas dinámicas ni respuestas en tiempo real

---

## 2026-05-09 — Orden de prioridades: primero estructura, luego automatización

**Decisión:** No automatizar room sprays (Prioridad 5) antes de resolver trazabilidad (Prioridad 1).

**Por qué:**
- "No puedes poner un motor de Ferrari en un chasis oxidado"
- Sin inventario trazable, cualquier automatización opera sobre datos incorrectos
- El Quick Win 1 (Trazabilidad Total) es el cimiento de todo lo demás

---

## 2026-05-09 — Enfoque de presentación: Quick Wins, no Big Bang

**Decisión:** Presentar el proyecto al dueño en base a 3 entregables concretos y medibles, no como una transformación digital completa.

**Por qué:**
- Reduce el riesgo percibido para el dueño
- Permite demostrar valor rápido antes de escalar
- Cada Quick Win es independiente y puede ejecutarse aunque los otros fallen
