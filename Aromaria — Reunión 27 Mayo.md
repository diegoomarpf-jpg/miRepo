---
date: 2026-05-22
type: project
project: aromaria
status: active
tags: [project, aromaria, reunion, promocion, urgente]
related-people:
  - "[[Rodrigo]]"
related-projects:
  - "[[Master plan 2026]]"
  - "[[Aromaria — MVP QR Form Monday]]"
deadline: 2026-05-27
ai-first: true
---

## Para el futuro Claude
Nota de batalla para la reunión del 27 de mayo con Rodrigo. Diego es empleado de Aromaria (nave operativa, Analista de Calidad) y esta reunión decide si lo promueven al nuevo equipo de IA. Contiene: contexto, estrategia de presentación, estructura de la hora, estado del MVP y lo que falta. **Leer antes de cualquier conversación sobre Aromaria o la reunión.**

---

# Reunión con Rodrigo — 27 de Mayo 2026

## Contexto

- **Diego:** Analista y Auditor de Calidad en la nave operativa de Aromaria
- **Rodrigo:** Uno de los dueños. Está implementando IA en la empresa. Quiere formar un equipo nuevo.
- **La apuesta:** Si Diego impresiona en esta reunión → promoción al equipo de IA + traslado a oficina administrativa
- **Duración:** 1 hora
- **Asistentes:** Solo Rodrigo como tomador de decisión
- **Lo que sabe Rodrigo de Diego:** Que es bueno en Monday.com y en IA. Nada más específico.

---

## Por qué Diego tiene ventaja

1. Conoce los problemas desde adentro (nave operativa) — ningún consultor externo tiene eso
2. Ya tiene el [[Master plan 2026]] completo: 5 macroprocesos, arquitectura Monday, KPIs, 4 fases
3. Tiene el MVP funcionando parcialmente: Google Sheets → n8n → Monday
4. El stack que propone (Monday + n8n + Claude) es exactamente lo que Rodrigo sueña
5. Rodrigo valora a quien **hace**, no solo habla — Diego tiene pruebas concretas

---

## Perfil de Rodrigo (del podcast)

Ver nota completa: [[PODCAST RODRIGO]]

**Frases clave que revelan su mente:**
- *"Si no estás usando AI bien, no nada más escribiéndole a ChatGPT, estás atrás"*
- *"¿Cómo convertirnos en un AI-enabled company? ¿Cómo abres las puertas a tus colaboradores?"*
- *"Puedes traer a alguien con la mitad de experiencia pero con un conocimiento amplísimo de IA y se lo va a chingar"*

**Lo que ya hace Rodrigo con IA:**
- Codea con Claude Code
- Tiene un agente personal que le manda brief de emails y juntas cada mañana a las 6:30am
- Conectó APIs de Shopify
- Se encerró 3 días sin dormir para aprender — aprecia ese mismo esfuerzo en otros

**Conector emocional para el pitch:**
> *"Vi lo que haces con tu agente de mails — yo quiero construir eso para la operación entera de Aromaria."*

---

## Estructura de la presentación (1 hora)

### Bloque 1 — El diagnóstico desde adentro (5 min)
- Hablar como alguien que conoce la nave, no como consultor
- Nombrar los dolores reales que Rodrigo ya conoce pero sin datos: inventario ciego, movimientos sin registro, producto detenido sin visibilidad
- Gancho: *"Llevo tiempo observando esto y diseñando la solución"*

### Bloque 2 — El plan (10 min)
- Mostrar [[Master plan 2026]] en UNA sola slide de resumen
- El principio rector: **Ordenar → Estandarizar → Integrar → Automatizar**
- Las 4 fases con tiempos (0-30d / 30-90d / 90-180d / 180-365d)
- NO entrar en detalle por macroproceso — solo la foto completa

### Bloque 3 — El MVP en vivo (20 min) ← MOMENTO CLAVE
- Narración: *"Mientras diseñaba el plan, ya construí la primera pieza"*
- Demo: sacar el celular → escanear QR → llenar el form → enviar → Monday se actualiza en 2-3 segundos
- El proceso demostrado: **Entrega de lote de producción a Almacén PT**
- Impacto: el personal operativo registra en Monday sin saber que existe Monday
- Conectar con el principio GIGO: *"Primero datos limpios, luego la IA funciona"*

### Bloque 4 — La visión AI-first (15 min)
- Mostrar el segundo cerebro: así es como Claude conoce toda la empresa
- El stack: Monday (datos) + n8n (integración) + Claude (inteligencia)
- La pregunta que Rodrigo podrá hacerle a Claude: *"¿Cuánto stock de lavanda tenemos hoy y cuándo debo pedir más?"*
- Conectar con SU agente personal: lo mismo, pero para la operación entera
- Meta: **Aromaria como AI-first company** — sus propias palabras del podcast

### Bloque 5 — El ask (10 min)
- Claro y directo: quiero liderar esto
- Proponer los primeros 15 días (ya están documentados en [[Master plan 2026]])
- Pedir: definición del nuevo rol + acceso a recursos para ejecutar

---

## Estado al 24 de mayo

**Completado:**
- ✅ Deck PPTX generado — `C:\Users\1544\Documents\Rediseño de tableros\Deck Rodrigo — 27 Mayo 2026.pptx` (16 slides)
- ✅ Vault en GitHub (`diegoomarpf-jpg/miRepo`) + obsidian-git + agente ops-diego activo
- ✅ Workflow A (crear entradas PT) funcionando end-to-end
- ✅ Workflow B: 3 de 4 nodos funcionan — Webhook ✅, Apps Script ✅, Get items ✅

**Pendiente crítico:**
- ❌ Workflow B — nodo "Change a column value" mal configurado (fix: Board ID `18412458512`, Item ID `{{ $json.id }}`, Column ID `color_mm36nssa`, Value `{"label": "Almacén PT"}`)
- ⬜ Prueba end-to-end del Workflow B con CONT-001
- ⬜ QR codes impresos (URLs listas en [[Aromaria — MVP QR Form Monday]])
- ⬜ Video de respaldo grabado
- ⬜ Board Monday limpio para el demo
- ⬜ Ensayo de la presentación en voz alta

---

## Plan de días hasta el 27

| Día | Foco | Entregable |
|---|---|---|
| Jue 22 | Dormir — documentar en vault | ✅ Vault documentado |
| Vie 23 | Construir MVP completo | ✅ Workflows construidos |
| Sáb 24 | Deck PPTX + fix nodo n8n | ✅ Deck listo · ❌ Fix pendiente |
| Dom 25 | Fix n8n + prueba + QRs + video | Demo estable + video de respaldo |
| Lun 26 | Ensayo completo en voz alta | Timing dominado |
| Mar 27 | **LA REUNIÓN** | Promoción |

---

## Archivos relacionados

- [[Master plan 2026]] — El plan completo de transformación operativa
- [[Aromaria — MVP QR Form Monday]] — Spec técnica del MVP
- [[PODCAST RODRIGO]] — Transcripción con insights de Rodrigo
- [[Rodrigo]] — Perfil del dueño/evaluador
- [[Backlog Estrátegico]] — Los 5 dolores prioritarios de Aromaria
- [[El Stack Tecnológico (La Triple Alianza)]] — Monday + n8n + Claude
