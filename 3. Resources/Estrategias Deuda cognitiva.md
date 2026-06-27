### Estrategia 1: No cerrar una fase hasta poder explicarla

Una regla útil es:

> Si no puedo explicar una decisión sin consultar a la IA, la fase aún no está terminada.

Por ejemplo, después de generar un análisis de riesgos, no avanzar inmediatamente al plan de mitigación.

Antes:

- Pedir a la IA que te interrogue.
- Explicar con tus palabras los riesgos identificados.
- Justificar por qué son importantes.

Si no puedes hacerlo, todavía existe deuda de comprensión.

### Estrategia 2: Generar artefactos de comprensión, no solo de ejecución

Normalmente pedimos:

- "Genera un procedimiento."
- "Genera un plan."
- "Genera un análisis."

Pero también puedes pedir:

- "Resume las 5 decisiones más importantes."
- "¿Qué supuestos estamos haciendo?"
- "¿Qué partes de este documento debo entender obligatoriamente?"
- "¿Qué decisiones impactarán fases futuras?"

Esto reduce enormemente el conocimiento oculto.

### Estrategia 3: Mantener un registro de decisiones

En arquitectura de software existe el concepto de ADR (Architecture Decision Record).

La idea es documentar:

- Qué decisión se tomó.
- Por qué se tomó.
- Qué alternativas se descartaron.
- Qué consecuencias tendrá.

Puedes hacer algo parecido en cualquier proyecto.

Por ejemplo:

|Decisión|Motivo|Impacto futuro|
|---|---|---|
|Usar conteos cíclicos semanales|Recursos limitados|KPI de inventario dependerá de ello|

La IA puede generar y mantener este registro automáticamente.

### Estrategia 4: Usar la IA como auditor del proyecto

Cada cierto tiempo preguntarle:

- "¿Qué supuestos no hemos validado?"
- "¿Qué decisiones podrían generar retrabajo?"
- "¿Qué elementos del proyecto parecen poco entendidos?"
- "¿Dónde existe dependencia de conocimiento implícito?"

Esto es similar a una auditoría de calidad, pero aplicada al entendimiento.

### Estrategia 5: La regla del ratio comprensión-producción

Una práctica que está empezando a aparecer entre usuarios avanzados es dedicar tiempo explícito a comprender.

Por ejemplo:

- 60% producir.
- 40% comprender.

O incluso:

- Por cada hora generando contenido con IA.
- 20 minutos revisando, cuestionando y consolidando.

Sin esa disciplina, la velocidad de generación suele superar la capacidad de absorción.

### Estrategia 6: Crear un "gemelo explicativo"

Cuando la IA genera un entregable importante, pedir simultáneamente:

1. El documento completo.
2. Una versión ejecutiva de una página.
3. Un mapa conceptual.
4. Una lista de decisiones clave.
5. Una lista de riesgos por malentender el documento.

Así cada artefacto tiene su propia documentación de comprensión.