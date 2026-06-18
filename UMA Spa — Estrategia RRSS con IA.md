---
date: 2026-06-17
type: project
tags:
  - project
  - umaspa
  - advanx
  - rrss
  - automatizacion
  - ia
ai-first: true
related-people:
  - "[[CAROL]]"
related-projects:
  - "[[Diagnóstico UMA]]"
  - "[[Advanx]]"
  - "[[UMA Spa — Tracker de Acompañamiento]]"
confidence: stated
updated: 2026-06-17
---

## Para el futuro Claude
Estrategia de contenido para redes sociales de [[CAROL]] / UMA Spa, diseñada como **piloto del servicio de automatización RRSS con IA de [[Advanx]]**. Incluye: system prompt base de marca, 4 prompts por tipo de post, y 5 posts de prueba listos para validar con Carol. El flujo técnico planeado es: Google Sheets (calendario) → n8n → Claude API (copy) → Ideogram API (imagen) → Buffer API (publicación). Al 2026-06-17: en fase de validación manual — Carol debe aprobar tono y calidad antes de automatizar.

---

#UMAspa #Advanx #RRSS

## Contexto Estratégico

- **Problema de UMA:** Visibilidad — necesita solo 7 masajes adicionales/mes para alcanzar el punto de equilibrio (ver [[Diagnóstico UMA]])
- **Objetivo de RRSS:** Atraer esos 7 clientes mensuales adicionales con contenido que comunique el diferenciador real
- **Diferenciador real (Sesión 2):** Los clientes no compran un masaje — compran la certeza de que alguien estará completamente presente para ellos, sin prisa y con cuidado genuino
- **Canales:** Instagram + Facebook
- **Modelo de publicación:** 4 posts/semana (2 bienestar, 1 servicio, 1 promo/testimonio)

---

## Flujo Técnico Planeado

```
[Google Sheets — Calendario Editorial]
         ↓
[n8n — Trigger semanal]
         ↓
[Claude API — genera caption + hashtags]
         ↓
[Ideogram API — genera imagen de fondo]
         ↓
[Placid API — overlay del logo sobre la imagen]
         ↓
[Buffer API — programa el post]
         ↓
[Google Sheets — log de publicado]
```

**Costo operativo estimado:** ~$50–60 USD/mes para 30 posts  
**Herramienta de imagen:** Ideogram (tiene API real, compatible con n8n. Midjourney descartado — sin API estable)  
**Herramienta de composición:** Placid (~$19 USD/mes) — permite crear una plantilla una sola vez con el logo de UMA ya posicionado; la API recibe la imagen de Ideogram como fondo y devuelve la imagen final lista. Alternativa más potente: Bannerbear (~$49 USD/mes), recomendado si se escala a múltiples clientes en Advanx.

> **Nota:** Ideogram no puede insertar un logo existente en la imagen generada — solo genera desde cero. La composición final (logo + imagen IA) se hace obligatoriamente en una capa separada vía Placid/Bannerbear. Carol sube el logo una vez a la plantilla; el flujo lo aplica automáticamente en cada post.

---

## System Prompt Base (ADN de Marca)

```
Eres el community manager de UMA Spa, un spa de masajes y tratamientos
en Ocoyoacac, Estado de México.

IDENTIDAD DE MARCA:
- Tono: espiritual, holístico, cálido, sin prisa
- Diferenciador real: los clientes no vienen por un masaje,
  vienen por la certeza de que alguien estará completamente
  presente para ellos, sin apuro y con cuidado genuino
- Servicios estrella: masaje relajante, masaje reductivo,
  limpieza facial profunda
- Público: mujeres de 25 a 45 años que priorizan su bienestar

REGLAS:
- Nunca mencionar precios en el caption
- Sin hashtags genéricos como #spa o #masaje — usar específicos
- Máximo 3 emojis por post
- Siempre terminar con una pregunta o invitación a reservar
- Lenguaje: español México, warm pero profesional
```

---

## Prompts por Tipo de Post

### Tipo 1 — Bienestar / Inspiracional (2x semana)

```
TAREA: Escribe un caption para Instagram/Facebook sobre bienestar.

TEMA DEL DÍA: {tema}
(ejemplos: el valor de parar, escucharte a ti misma,
el cuerpo que te carga, darte tiempo sin culpa)

FORMATO:
- Línea 1: gancho emocional (máx 10 palabras)
- Párrafo 2-3: reflexión breve conectada al tema
- Cierre: invitación suave a agendar
- 5-7 hashtags: #UMASpa #BienestarReal #CuidadoFemenino
  #MasajeOcoyoacac #TiempoParaTi #ZonaMetro + 1 del tema

IMAGEN PARA IDEOGRAM:
"Serene spa interior, soft natural light, white linens on
massage table, eucalyptus branches, warm candles,
spiritual and holistic aesthetic, Mexico, photorealistic"
```

### Tipo 2 — Servicio Destacado (1x semana)

```
TAREA: Escribe un caption para destacar un servicio de UMA Spa.

SERVICIO: {servicio}
BENEFICIO PRINCIPAL: {beneficio}

FORMATO:
- Línea 1: beneficio como resultado visible
- Párrafo: qué experimenta la clienta durante el servicio
  (sensaciones, no técnicas)
- Datos: duración aproximada si aplica
- CTA: "Agenda tu cita por DM o WhatsApp"
- 5 hashtags específicos del servicio

IMAGEN PARA IDEOGRAM:
"Professional spa treatment [nombre del servicio],
warm atmosphere, skilled hands, relaxed client, soft
lighting, holistic wellness aesthetic, photorealistic"
```

### Tipo 3 — Promoción / CTA Directo (1x semana)

```
TAREA: Escribe un post de promoción o paquete para UMA Spa.

PROMOCIÓN: {descripción de la promo}
URGENCIA: {límite} (usar disponibilidad real, no inventada)

FORMATO:
- Línea 1: oferta clara y directa
- Párrafo: qué incluye + qué va a sentir
- Urgencia genuina (disponibilidad real de agenda)
- CTA directo: DM / WhatsApp / Link en bio
- 4-5 hashtags + #Ocoyoacac #LermaEdomex

IMAGEN PARA IDEOGRAM:
"Spa promotional graphic, elegant minimalist design,
UMA Spa text treatment, warm neutral palette,
rose gold accents, professional aesthetic"
```

### Tipo 4 — Testimonio / Prueba Social (1x cada 2 semanas)

```
TAREA: Convierte este testimonio real en un post atractivo.

TESTIMONIO ORIGINAL: "{texto de la clienta}"
SERVICIO QUE RECIBIÓ: {servicio}

FORMATO:
- Cita en comillas como apertura (ajustar redacción, no significado)
- Línea de contexto: "— Clienta de masaje relajante"
- 2-3 líneas sobre por qué este resultado es posible en UMA
- CTA: "¿Quieres vivir esto? Agenda tu sesión"
- Hashtags: #ExperienciaUMA #TestimonioReal + 3 más

IMAGEN PARA IDEOGRAM:
"Peaceful woman after spa treatment, eyes closed, serene
expression, wrapped in white towel, soft natural lighting,
wellness and self-care aesthetic, photorealistic portrait"
```

---

## 5 Posts de Prueba (generados 2026-06-17)

> Estos posts están pendientes de validación por [[CAROL]]. Ver sección de preguntas de validación al final.

### Post 1 — Bienestar: El valor de parar

**Caption:**
> Parar no es perder el tiempo. Es recuperarte para seguir.
>
> Vivimos en modo automático: trabajo, casa, pendientes, familia. El cuerpo aguanta porque no tiene de otra. Pero hay un momento en que te dice basta — con una contractura, con el insomnio, con ese cansancio que no se va ni durmiendo.
>
> En UMA ese momento se convierte en un espacio solo tuyo. Sin prisa. Sin pantallas. Con alguien completamente presente para ti.
>
> ¿Cuándo fue la última vez que te diste eso? 🌿
>
> Agenda tu sesión por DM o WhatsApp.

**Hashtags:** #UMASpa #BienestarFemenino #TiempoParaTi #MasajeOcoyoacac #CuidadoPersonal #SaludMental #DescansoReal

**Imagen Ideogram:** `Peaceful woman lying on white massage table, eyes closed, serene expression, eucalyptus and candles in background, soft warm natural lighting, spiritual holistic spa aesthetic, Ocoyoacac Mexico, photorealistic`

---

### Post 2 — Servicio: Masaje Relajante

**Caption:**
> Tu cuerpo lleva semanas cargando más de lo que debería. 💆‍♀️
>
> El masaje relajante de UMA no es solo técnica — es una hora en la que alguien pone toda su atención en ti. Sin interrupciones. Sin apuro. Solo tú y el silencio que tanto necesitas.
>
> Mientras más tensión acumulas, más diferencia sientes. Las clientas salen con los hombros abajo, la respiración profunda y esa sensación de que el mundo puede esperar.
>
> Sesiones disponibles martes, jueves y sábado.
>
> ¿Te agendamos esta semana?

**Hashtags:** #MasajeRelajante #UMASpa #Ocoyoacac #BienestarReal #MasajesEdomex #RelajaciónProfunda

**Imagen Ideogram:** `Professional relaxation massage in serene spa, warm lighting, white linens, therapist hands on client shoulders, eucalyptus and aromatic candles, holistic wellness atmosphere, photorealistic`

---

### Post 3 — Bienestar: Darte tiempo sin culpa

**Caption:**
> Cuidarte no es egoísta. Es necesario.
>
> Hay una creencia muy arraigada en muchas mujeres: que atenderse a una misma va después. Después de los hijos, después del trabajo, después de que todo esté en orden.
>
> El problema es que ese "después" nunca llega.
>
> Darte una hora para ti no le quita nada a nadie. Al contrario — regresas más presente, más paciente, más tú. ✨
>
> En UMA te esperamos cuando estés lista.

**Hashtags:** #UMASpa #CuidadoFemenino #SinCulpa #TiempoParaMi #BienestarHolístico #Autocuidado #MasajeOcoyoacac

**Imagen Ideogram:** `Woman in peaceful meditation in spa, wrapped in white robe, cup of herbal tea, morning light through window, spiritual and feminine wellness aesthetic, warm tones, photorealistic`

---

### Post 4 — Servicio: Masaje Reductivo

**Caption:**
> Moldear contornos requiere constancia — y el apoyo correcto. 🌸
>
> El masaje reductivo de UMA combina técnica manual con aparatología especializada: cavitación, radiofrecuencia y maderoterapia. Trabajamos juntas en un plan real, no en una promesa de una sola sesión.
>
> Lo que sienten las clientas después: la zona más firme, mejor circulación y ese alivio de saber que están haciendo algo por ellas.
>
> Los resultados se construyen sesión a sesión. ¿Empezamos?
>
> Escríbenos por DM para conocer opciones de paquetes.

**Hashtags:** #MasajeReductivo #UMASpa #Cavitación #Maderoterapia #CuerpoSano #Ocoyoacac #TratamientosReductivos #BienestarEdomex

**Imagen Ideogram:** `Professional body contouring spa treatment, warm professional atmosphere, maderotherapy wooden tools, skilled therapist, relaxed client, holistic wellness center, soft lighting, photorealistic`

---

### Post 5 — Promoción CTA

**Caption:**
> Esta semana tenemos 4 lugares disponibles. 📅
>
> Si llevas tiempo diciéndote "voy a ir al spa" — este es el momento.
>
> Una hora de masaje relajante en UMA: sin ruido, sin apuro, con atención completa de principio a fin. El tipo de pausa que te recuerda cómo se siente estar bien de verdad.
>
> Martes, jueves o sábado en Ocoyoacac.
>
> Escríbenos por DM o WhatsApp y te confirmamos tu lugar hoy. ✉️

**Hashtags:** #UMASpa #AgendaTuCita #MasajeOcoyoacac #LugaresDisponibles #BienestarFemenino #Ocoyoacac #EdomexSpa

**Imagen Ideogram:** `Elegant spa appointment booking concept, calendar and white orchids on wooden desk, warm candlelight, UMA Spa text, minimalist wellness aesthetic, soft rose and cream tones, photorealistic`

---

## Validación con Carol

Preguntas para la sesión de validación de tono:

1. **¿El tono se siente tuyo?** (si suena demasiado formal o demasiado relajado)
2. **¿Cambiarías algo de cómo describes los servicios?**
3. **¿Hay palabras que nunca usarías para hablar de UMA?**

Criterio para automatizar: cuando el 80% de los posts salgan aprobados sin edición mayor → conectar flujo n8n.

---

## Como Servicio Advanx (modelo de precios)

| Concepto | Monto |
|---|---|
| Setup (configuración + prompts + voz de marca) | $3,000–$5,000 MXN único |
| Retención mensual (operación + ajustes + reporte) | $2,500–$4,000 MXN/mes |
| Campañas especiales / temporadas | por proyecto |

**Costo operativo real para Advanx:** ~$50–60 USD/mes por cliente (Ideogram + Placid + Buffer)  
**Diferenciador del servicio:** No se venden "posts" — se vende un sistema que aprende la voz de la marca y produce sin intervención del cliente.
