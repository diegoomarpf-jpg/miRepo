# Claude Operating Manual — Diego's Vault

> Lee este archivo antes de hacer cualquier cosa en este vault.
> Es la fuente única de verdad sobre cómo opera Claude aquí.

---

## Section 0 — AI-First Vault Rule (lee primero, aplica a cada nota)

Este vault está diseñado para que **el futuro-Claude** lo lea y razone sobre él, no para revisión humana directa. El dueño raramente abre notas directamente — llama a Claude para recuperar, sintetizar y conectar ideas acumuladas.

**Cada nota que Claude escriba en este vault debe seguir estas reglas:**

1. **Contexto autocontenido** — Cada nota debe explicarse sola. El futuro-Claude puede recuperarla sin contexto circundante. No dependas solo de backlinks.
2. **Preámbulo "Para el futuro Claude"** — Cada nota comienza con un resumen de 2-3 oraciones en español claro bajo `## Para el futuro Claude`.
3. **Frontmatter rico y consistente** — Metadatos filtrables (`type`, `date`, `tags`, `related-people`, `related-projects`, `sources`, `confidence`). Siempre incluye `ai-first: true`.
4. **Marcadores de vigencia por afirmación** — Al declarar hechos externos, adjunta la fecha: "NearStream pivotó a automatización (al 2026-03)" para que el futuro-Claude sepa qué verificar.
5. **Fuentes preservadas verbatim** — Cada afirmación externa tiene su URL fuente inline.
6. **Cross-links obligatorios** — Cada persona, proyecto, idea o decisión referenciada usa wikilinks dobles `[[ ]]`.
7. **Niveles de confianza** — Cuando aplique: `stated | high | medium | speculation`.

---

## Section 0.5 — Verifica el estado real antes de actuar

Antes de declarar un bug, redactar una solución o escribir arquitectura: lee el código, esquema o datos reales. La especulación desde contexto desactualizado quema tiempo.

---

## Identidad del Vault

- **Dueño:** Diego
- **Propósito principal:** OS de emprendedor — NearStream (startup de automatización), Advanx (consultoría), Michi Ahorrador (app fintech), vida personal
- **Idioma principal:** Español (algunas notas en inglés)
- **Última actualización:** 2026-05-22

---

## Mapa del Vault (estructura plana con clusters temáticos)

El vault no usa carpetas tradicionales. Las notas conviven en la raíz agrupadas por prefijo o tag.

| Cluster / Tag | Contenido |
|---|---|
| `#NearStream` | Startup de consultoría/automatización. Iteraciones registradas en `[[NearStream Registro de Iteraciones]]` |
| `#michiahorrador` | App de ahorro gamificada. Mecánicas RPG, estructura SQL |
| `#MasterPlanAromaria` | Cliente Rodrigo / Aromaria — consultoría de inventario y operaciones |
| `#UMAspa` | Cliente Carol — spa en Ocoyoacac, consultoría de precios y estructura |
| `#modelosmentales` | Modelos mentales, frameworks de pensamiento |
| `Excalidraw/` | Diagramas y mapas visuales |
| Notas diarias | Formato `YYYY-MM-DD.md` en raíz |
| `Logs/` | Log operativo del vault (generado por obsidian-second-brain) |

---

## Archivos Clave

- **Iteraciones NearStream:** `[[NearStream Registro de Iteraciones]]`
- **Plan Aromaria:** `[[Backlog Estrátegico]]` (Aromaria Master Plan)
- **App Michi Ahorrador:** `[[Caja de Ahorro (Michi Ahorrador)]]`
- **Consultoría Advanx:** `[[Advanx]]`
- **Diagnóstico UMA SPA:** `[[Diagnóstico UMA]]` · `[[CAROL]]`
- **Stack tecnológico:** `[[El Stack Tecnológico (La Triple Alianza)]]`
- **n8n / Automatización:** `[[N8N]]` · `[[Conectar n8n a internet]]`
- **Índice del vault:** `[[index]]`
- **Log operativo:** `[[log]]` → `Logs/YYYY-MM-DD.md`

---

## Contexto Activo

> Actualiza esta sección al inicio de cada proyecto o período de enfoque.

## 🔴 URGENTE — Reunión Aromaria el 27 de Mayo

Diego es **empleado** de Aromaria (Analista de Calidad, nave operativa). El 27 de mayo presenta ante Rodrigo (dueño) para ser promovido al equipo de IA. Ver `[[Aromaria — Reunión 27 Mayo]]` y `[[CRITICAL_FACTS]]` para el plan completo. El MVP (QR → Form → n8n → Monday) está en construcción — ver `[[Aromaria — MVP QR Form Monday]]`.

---

**Empleo principal:** Aromaria — Analista y Auditor de Calidad en nave operativa
**Consultoría paralela:** Advanx — consultoría generalista data-driven para PyMEs (~50 personas). NearStream es una vertical nicho dentro de Advanx.
**NearStream (vertical de Advanx):** PyMEs que buscan ser Tier 2/3 en nearshoring. 3a iteración: automatización n8n/Python para empresas con Excel.
**Proyecto personal:** Michi Ahorrador — app de ahorro gamificada (mecánicas RPG)

---

## Reglas de Auto-Guardado

Claude debe guardar **sin preguntar:**
- Decisiones tomadas en conversación → nota del proyecto relevante
- Personas nuevas mencionadas → crear stub en raíz con nombre completo
- Tareas comprometidas → nota de tarea o nota diaria
- Iteraciones de NearStream → `[[NearStream Registro de Iteraciones]]`
- Insights de clientes → nota del cliente correspondiente

Claude debe **preguntar antes de guardar:**
- Cualquier dato financiero personal
- Notas sobre Lorena o familia (privado)
- Eliminar o archivar notas existentes

---

## Convenciones de Nombres

- Notas diarias: `YYYY-MM-DD.md`
- Notas de cliente: `Nombre del cliente` o descripción del trabajo
- Iteraciones de proyecto: describir la iteración, no numerarla en el nombre de archivo
- Personas: Nombre completo (ej. `Lorena.md`, no `Lo.md`)
- Prefijo de archivado: `_archivado_`

---

## Frontmatter Mínimo Requerido

```yaml
---
date: YYYY-MM-DD
type: <tipo>
tags: [tipo, proyecto]
ai-first: true
---
```

Tipos: `daily` | `project` | `task` | `person` | `idea` | `devlog` | `research` | `synthesis` | `decision`

---

## Personas Clave

| Persona | Rol | Contexto |
|---|---|---|
| Lorena | Pareja | Máxima prioridad personal. Esperando bebé juntos. |
| Rodrigo | Cliente Aromaria | Dueño de empresa de fragancias/home. Necesita inventario, trazabilidad y organigrama. |
| Carol | Cliente UMA SPA | Emprendedora de spa en Ocoyoacac. Consultoría de precios y estructura operativa. |

---

## Proyectos Activos

- `[[Advanx]]` — Consultoría generalista para PyMEs. Paraguas de todo lo de consultoría.
  - `[[NearStream Registro de Iteraciones]]` — Vertical nicho de Advanx: PyMEs que buscan ser Tier 2/3 en nearshoring. 3a iteración: automatización n8n/Python.
  - `[[Backlog Estrátegico]]` — Cliente Aromaria (Rodrigo): inventario, trazabilidad, organigrama
  - `[[CAROL]]` / `[[Diagnóstico UMA]]` — Cliente UMA SPA (Carol): estructura financiera y protocolo
- `[[Caja de Ahorro (Michi Ahorrador)]]` — App de ahorro gamificada (proyecto personal, no consultoría)

---

## No Tocar

- `Excalidraw/` — No modificar archivos `.excalidraw.md` durante operaciones normales
- `.obsidian/` — Configuración del app, no editar manualmente
- `.claude/` — Configuración de Claude Code, no editar manualmente
- **Lorena** — No crear nota de persona. Mantener fuera del vault por decisión explícita del dueño.

---

*Generado por obsidian-second-brain el 2026-05-22.*
*Regenerar con: "Claude, actualiza mi _CLAUDE.md"*
