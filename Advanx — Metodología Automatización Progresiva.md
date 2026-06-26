---
date: 2026-06-24
type: project
project: advanx
tags:
  - project
  - advanx
  - metodologia
  - automatizacion
ai-first: true
related-projects:
  - "[[Advanx]]"
  - "[[CAROL]]"
  - "[[NearStream Registro de Iteraciones]]"
confidence: medium
status:
---

## Para el futuro Claude
Esta es la Iteración 2 de la metodología de [[Advanx]], generada el 2026-06-24. El norte cambió: de "consultoría estratégica que eventualmente automatiza" a "automatización progresiva que empieza por entender el negocio." La metodología anterior (4 fases / 16 sesiones de consultoría) queda como histórico en [[Advanx — Metodología Completa]]. Esta versión NO reemplaza formalmente a la anterior — es una iteración en exploración. Requiere validarse con un cliente real antes de adoptarse como metodología oficial.

---

# Advanx — Metodología Automatización Progresiva (Iteración 2)

## El Norte

> **No hacemos consultoría que a veces automatiza. Construimos el roadmap de automatización de tu empresa — empezando por entender lo suficiente para automatizar con sentido.**

La diferencia es el punto de llegada. En la metodología anterior, el entregable final era "estructura rentable y escalable." En esta, el entregable final es **operación automatizada con datos en tiempo real.**

El trabajo estratégico (ICP, costos, procesos) no desaparece — se convierte en el paso necesario para saber QUÉ automatizar y en QUÉ orden.

---

## Por qué el trabajo estratégico sigue siendo necesario

No se puede automatizar lo que no se entiende. Antes de construir un flujo de captación automatizado, necesitas saber quién es tu cliente. Antes de automatizar el reporte de rentabilidad, necesitas saber tu estructura de costos. Antes de automatizar el seguimiento post-venta, necesitas tener un proceso de venta.

El reframe es: la planeación estratégica no es el producto — es el **punto de partida del roadmap de automatización.**

---

## Estructura: 4 Meses / Roadmap Progresivo

```
Mes 1 — BASE        → entender para automatizar con sentido
Mes 2 — OPERACIÓN   → automatizar lo que quita tiempo al equipo
Mes 3 — DATOS       → visibilidad en tiempo real sin intervención manual
Mes 4 — CRECIMIENTO → automatizar captación, retención y referidos
```

---

### Mes 1 — Base: Entender para automatizar

**Pregunta que responde:** ¿Qué necesitamos saber para construir tu roadmap de automatización?

| Sesión | Tema                      | Por qué importa para automatizar                           |
| ------ | ------------------------- | ---------------------------------------------------------- |
| 1      | ICP + propuesta de valor  | Para saber qué mensajes y canales automatizar en captación |
| 2      | Proceso más doloroso      | Para identificar el primer quick win de automatización     |
| 3      | Estructura de costos      | Para automatizar reportes de rentabilidad con datos reales |
| 4      | Roadmap de automatización | Priorización: qué automatizamos en qué orden y por qué     |

**Entregable:** Roadmap de automatización personalizado — no genérico. Cada item del roadmap tiene una razón de negocio detrás.

---

### Mes 2 — Operación: Automatizar lo manual

**Pregunta que responde:** ¿Qué hace tu equipo manualmente hoy que una máquina puede hacer?

| Sesión | Tema | Ejemplo de automatización |
|--------|------|--------------------------|
| 1 | Mapeo de procesos operativos | Identificar los 3 procesos que más tiempo consumen |
| 2 | Automatización #1 | Flujo n8n del proceso más doloroso en producción |
| 3 | Automatización #2 | Segundo flujo priorizado del roadmap |
| 4 | Revisión y ajuste | Los flujos corrieron 2 semanas. ¿Qué se rompió? Ajuste final |

**Entregable:** 2 automatizaciones operativas corriendo en producción. El equipo ya no hace esas tareas manualmente.

---

### Mes 3 — Datos: Ver el negocio en tiempo real

**Pregunta que responde:** ¿Cómo sabes si tu negocio va bien sin preguntarle a alguien?

| Sesión | Tema                       | Ejemplo de automatización                                                               |
| ------ | -------------------------- | --------------------------------------------------------------------------------------- |
| 1      | KPIs que importan          | 3–5 métricas reales (no vanity metrics)                                                 |
| 2      | Dashboard automático       | Google Sheet / Notion que se actualiza solo con datos de las automatizaciones del Mes 2 |
| 3      | Alertas automáticas        | Si X baja de Y → notificación por WhatsApp/Slack sin intervención humana                |
| 4      | Primera decisión con datos | En vivo, juntos, basada en el dashboard — no en intuición                               |

**Entregable:** Dashboard que el dueño abre en el celular y ve el estado real del negocio. Sin pedirle a nadie.

---

### Mes 4 — Crecimiento: Automatizar la adquisición y retención

**Pregunta que responde:** ¿Cómo haces que el negocio crezca sin que el dueño tenga que estar presente en cada paso?

| Sesión | Tema | Ejemplo de automatización |
|--------|------|--------------------------|
| 1 | Flywheel de crecimiento | ¿Qué hace que un cliente regrese y recomiende? |
| 2 | Sistema de seguimiento automático | Post-venta: recordatorio, encuesta, invitación a regresar — sin intervención |
| 3 | Sistema de referidos | Mecanismo automatizado que activa el referido (mensaje + incentivo) |
| 4 | Playbook completo | Todo lo construido en 4 meses consolidado + roadmap para el siguiente año |

**Entregable:** El negocio crece con menos intervención del dueño. Las automatizaciones trabajan mientras él no está.

---

## Cómo aplica a distintos tipos de cliente

### Cliente desde cero (ej. UMA Spa)
El Mes 1 es más intenso — hay más que entender antes de automatizar. Pero incluso aquí, el Mes 1 termina con una primera automatización simple (ej. recordatorio de cita por WhatsApp). El cliente ve valor desde el primer mes.

### Cliente maduro (ej. manufactura con Excel)
El Mes 1 es más corto — ya saben quiénes son y qué venden. Se puede entrar directamente a mapear procesos y automatizar. El Sprint Express (pre-acompañamiento) probablemente ya resolvió algo en su operación.

---

## El Sprint Express en este contexto

El Sprint Express ($10k, 1–2 semanas) es el **Mes 0** — antes de que empiece el acompañamiento formal. Implementa el quick win identificado en el Diagnóstico Express. Cuando el cliente decide continuar con el acompañamiento, el Sprint ya no se repite: el Mes 1 empieza donde el sprint dejó, aprovechando lo construido.

```
Diagnóstico Express (gratis) → Sprint Express ($10k) → Acompañamiento 4 meses ($18k/mes)
                                        ↑
                              "Mes 0" — lo que se construyó aquí
                              es el punto de partida del Mes 1
```

---

## Diferencia clave vs. Metodología Anterior

| Dimensión | Metodología Anterior | Esta iteración |
|-----------|---------------------|----------------|
| Norte | Estructura rentable y escalable | Operación automatizada con datos |
| Trabajo estratégico | Fin en sí mismo | Habilitador de automatización |
| Automatización | Mencionada, sin lugar explícito | Entregable central en cada mes |
| Caso de éxito modelo | UMA Spa (consultoría estratégica) | Empresa con procesos manuales automatizados |
| Estado | Validada en campo (3/4 sesiones) | No validada aún — iteración en exploración |

---

## Estado de Validación (al 2026-06-24)

| Fase | Estado |
|------|--------|
| Mes 1 — Base | Parcialmente validado vía [[CAROL]] / UMA Spa (con framing anterior) |
| Mes 2 — Operación | Sin validar |
| Mes 3 — Datos | Sin validar |
| Mes 4 — Crecimiento | Sin validar |

**Siguiente paso de validación:** Ejecutar un cliente completo bajo este framing. El primer cliente que entre con el Diagnóstico Express + Sprint Express será el caso de prueba.

---

*Iteración 2 generada en conversación con Claude el 2026-06-24.*
*Metodología anterior preservada en [[Advanx — Metodología Completa]].*
