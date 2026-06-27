---
type: sistema
---

# Pipeline de Inbox

## Flujo

```
Captura (cualquier momento)
        ↓
   0. Inbox/        ← cae aquí sin pensar en dónde va
        ↓
  Procesamiento     ← una vez por semana, ~15 min
        ↓
  Lugar final       ← Projects / Areas / Resources / Archive
```

## Regla de oro
**Nunca crear una nota directamente en su carpeta final.**  
Todo pasa por Inbox primero. El costo de moverla después es cero. El costo de no capturarla es permanente.

---

## Sesión de procesamiento semanal

Para cada nota en Inbox, responder en orden:

### 1. ¿Requiere acción con deadline?
→ **Sí** — va a `1. Projects/<proyecto>/` con `status: activo`  
→ **No** — siguiente pregunta

### 2. ¿Es una responsabilidad permanente?
→ **Sí** — va a `2. Areas/<área>/`  
→ **No** — siguiente pregunta

### 3. ¿Es referencia o conocimiento?
→ **Sí** — va a `3. Resources/` (o `/Metodología/` o `/Técnico/`)  
→ **No** — siguiente pregunta

### 4. ¿Ya no es relevante pero vale guardar?
→ `4. Archive/`  
→ Si no vale nada: **eliminar sin culpa**

---

## Tipos de nota y su template

| Si es... | Usa template | Va a |
|----------|-------------|------|
| Proyecto nuevo o nota de proyecto | `Templates/Proyecto.md` | `1. Projects/<nombre>/` |
| Responsabilidad continua | `Templates/Área.md` | `2. Areas/<área>/` |
| Libro / video / artículo | `Templates/Fuente.md` | `3. Resources/` |
| Idea o marco conceptual | `Templates/Concepto.md` | `3. Resources/` |
| Persona / contacto | `Templates/Persona.md` | `People/` |

---

## Señales de que el Inbox está sano
- Menos de 10 notas al procesar
- Ninguna nota tiene más de 7 días sin procesar
- Cada nota procesada tiene `type:` en el frontmatter
