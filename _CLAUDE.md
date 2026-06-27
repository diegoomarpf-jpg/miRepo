# Claude Operating Manual — Diego's Vault

> Lee este archivo antes de hacer cualquier cosa en este vault.
> Es la fuente única de verdad sobre cómo opera Claude aquí.

---

## Section 0 — AI-First Vault Rule (aplica a cada nota que Claude escriba)

Este vault está diseñado para que el futuro-Claude lo lea y razone sobre él. Diego raramente abre notas directamente — llama a Claude para recuperar, sintetizar y conectar ideas.

**Reglas para cada nota que Claude genere:**

1. **Contexto autocontenido** — La nota debe explicarse sola sin contexto circundante.
2. **Preámbulo "Para el futuro Claude"** — Resumen de 2-3 oraciones al inicio bajo ese encabezado.
3. **Frontmatter rico** — Siempre incluir `type`, `date`, `tags`, `ai-first: true`.
4. **Marcadores de vigencia** — Al declarar hechos externos: "X ocurrió (al 2026-06)" para que el futuro-Claude sepa qué verificar.
5. **Cross-links obligatorios** — Personas, proyectos, ideas y decisiones usan `[[ ]]`.
6. **Niveles de confianza** cuando aplique: `stated | high | medium | speculation`.

---

## Section 0.5 — Verifica el estado real antes de actuar

Antes de declarar un bug, redactar una solución o escribir arquitectura: lee el código, esquema o datos reales. La especulación desde contexto desactualizado quema tiempo.

---

## Identidad del Vault

- **Dueño:** Diego Omar
- **Email:** diegoomarpf@gmail.com
- **Propósito:** OS de emprendedor — NearStream/Advanx (consultoría IA), Michi Ahorrador (fintech), proyectos de clientes
- **Idioma principal:** Español
- **Última actualización estructural:** 2026-06-27

---

## Estructura del Vault (PARA)

```
DIGITAL BRAIN/
├── 0. Inbox/          ← captura sin clasificar. TODO pasa por aquí primero
├── 1. Projects/       ← proyectos con deadline y resultado definido
│   ├── Aromaria/      ← cliente Rodrigo (inventario, trazabilidad)
│   ├── Michi Ahorrador/  ← app fintech personal
│   ├── NearStream/    ← consultoría propia (automatización PyMEs)
│   └── UMA SPA/       ← cliente Carol (spa en Ocoyoacac)
├── 2. Areas/          ← responsabilidades permanentes sin deadline
│   ├── Finanzas/
│   └── Salud/
├── 3. Resources/      ← conocimiento de referencia reutilizable
│   ├── Metodología/   ← El Método Diego, Stack Replicable, síntesis
│   └── Técnico/       ← Dataview, n8n, referencias técnicas
├── 4. Archive/        ← completado o inactivo
│   ├── Daily/         ← notas diarias antiguas
│   └── Logs/          ← log operativo del vault
├── Daily/             ← nota diaria activa (formato YYYY-MM-DD.md)
├── People/            ← personas clave (CAROL.md, Rodrigo.md...)
├── Templates/         ← templates de cada tipo de nota
│   ├── Proyecto.md
│   ├── Área.md
│   ├── Fuente.md
│   ├── Concepto.md
│   └── Persona.md
└── [raíz]             ← solo archivos de sistema: index.md, log.md, _CLAUDE.md, CRITICAL_FACTS.md, Master plan 2026.md
```

---

## Gobernanza — Tipos de Nota

| Type (frontmatter) | Template | Carpeta destino |
|--------------------|----------|-----------------|
| `proyecto` | Templates/Proyecto.md | `1. Projects/<nombre>/` |
| `area` | Templates/Área.md | `2. Areas/<nombre>/` |
| `fuente` | Templates/Fuente.md | `3. Resources/` |
| `concepto` | Templates/Concepto.md | `3. Resources/` |
| `persona` | Templates/Persona.md | `People/` |
| `daily` | — | `Daily/` |
| `sistema` | — | raíz |

**Pipeline de Inbox:** Ver `0. Inbox/PIPELINE.md` — regla clave: toda nota nueva cae en `0. Inbox/` primero, nunca directamente en su carpeta final.

---

## Archivos Clave

- **Iteraciones NearStream:** `1. Projects/NearStream/NearStream Registro de Iteraciones.md`
- **Proyecto Aromaria:** `1. Projects/Aromaria/` (CONTEXT.md, TAREAS.md, DECISIONES.md, Backlog Estrátegico.md)
- **Michi Ahorrador:** `1. Projects/Michi Ahorrador/Michi Ahorrador.md`
- **UMA SPA:** `1. Projects/UMA SPA/` (sesiones 1-3, tracker)
- **Metodología replicable:** `3. Resources/Metodología/`
- **Personas:** `People/CAROL.md`, `People/Rodrigo.md`
- **Log operativo:** `log.md` → `4. Archive/Logs/YYYY-MM-DD.md`
- **Índice del vault:** `index.md`

---

## Contexto Activo (actualizar al inicio de cada período de enfoque)

**Al 2026-06-27:**
- Foco principal: **NearStream** — consultoría propia de automatización (n8n/Python) para PyMEs con Excel. Marca comercial: Advanx.
- Reunión Aromaria del 27 mayo ya ocurrió. Estado del proyecto: ver `1. Projects/Aromaria/SESIONES.md`.
- UMA SPA: acompañamiento en curso (3 sesiones completadas).
- Michi Ahorrador: en pausa relativa.

---

## Reglas de Auto-Guardado

Claude debe guardar **sin preguntar:**
- Decisiones tomadas en conversación → nota del proyecto relevante con `type: decision`
- Personas nuevas mencionadas → stub en `People/` con nombre completo
- Tareas comprometidas → nota del proyecto o nota diaria
- Iteraciones de NearStream → `1. Projects/NearStream/NearStream Registro de Iteraciones.md`
- Insights de clientes → carpeta del cliente en `1. Projects/`
- Todo lo demás → `0. Inbox/` (clasificar en la siguiente sesión de procesamiento)

Claude debe **preguntar antes de:**
- Guardar datos financieros personales
- Crear notas sobre Lorena o familia (privado)
- Eliminar o mover notas existentes

---

## Personas Clave

| Persona | Rol | Contexto |
|---------|-----|----------|
| Lorena | Pareja | Máxima prioridad personal. Esperando bebé juntos. No crear nota — fuera del vault por decisión explícita. |
| Rodrigo | Cliente Aromaria | Dueño de empresa de fragancias. Necesita inventario, trazabilidad, organigrama. |
| Carol | Cliente UMA SPA | Emprendedora de spa en Ocoyoacac. Consultoría de precios y estructura. |

---

## Convenciones de Nombres

- Notas diarias: `YYYY-MM-DD.md` en `Daily/`
- Notas de proyecto: `Nombre del Proyecto — Subtema.md`
- Personas: Nombre completo en mayúsculas (`CAROL.md`, `Rodrigo.md`)
- No usar prefijos de archivado — simplemente mover a `4. Archive/`

---

## No Tocar

- `Excalidraw/` — No modificar archivos `.excalidraw.md`
- `.obsidian/` — Configuración del app
- `.claude/` — Configuración de Claude Code
- **Lorena** — No crear nota. Decisión explícita del dueño.

---

*Actualizado 2026-06-27 tras reorganización estructural a PARA.*
*Para regenerar: "Claude, actualiza mi _CLAUDE.md"*
