---
date: 2026-05-23
type: devlog
status: in-progress
tags: [devlog, aromaria, n8n, monday, mvp]
related-projects:
  - "[[Aromaria — Reunión 27 Mayo]]"
  - "[[Master plan 2026]]"
ai-first: true
---

## Para el futuro Claude
Estado al 23 de mayo. El MVP evolucionó: ya no crea elementos nuevos sino que **actualiza el status de contenedores existentes** (cambio de Ubicación actual). Hay DOS workflows: Workflow A (crear entradas PT — funciona) y Workflow B (actualizar Ubicación actual — en construcción, bloqueado en Apps Script). El demo del 27 usa el Workflow B. Continuar con: diagnosticar por qué el trigger onFormSubmit del segundo form no dispara el webhook.

---

# MVP — QR → Form → n8n → Monday

## Qué demuestra

Un operario entrega un lote a Almacén de Producto Terminado:
1. Escanea QR pegado en la zona de entrega
2. Se abre Google Form en su celular
3. Llena 8 campos (producto, lote, cantidad, etc.)
4. Envía
5. En 2-3 segundos aparece el elemento en Monday — sin que el operario sepa que Monday existe

**Por qué importa:** Es la prueba de que el personal operativo puede alimentar el sistema de datos sin capacitación en Monday. Resuelve el problema de captura del [[Master plan 2026]].

---

## Arquitectura

```
QR Code
  → Google Form (8 campos)
    → Google Sheets (vinculado automáticamente)
      → Apps Script onFormSubmit
        → n8n Webhook (instantáneo)
          → Monday API
            → Board: Inventario PT
```

**Por qué webhook y no Sheets trigger:**
El trigger de Google Sheets en n8n hace polling cada 1-5 minutos. Para el demo en vivo eso mata el efecto. El webhook dispara en 2-3 segundos.

---

## Campos del Google Form

| # | Campo | Tipo | Notas |
|---|---|---|---|
| 1 | Producto | Desplegable | Usar lista de SKUs existente |
| 2 | Lote Origen | Respuesta corta | Texto libre |
| 3 | Cantidad | Respuesta corta | Validar: solo números |
| 4 | Tipo de Movimiento | Selección múltiple | Entrada PT / Retorno / Ajuste |
| 5 | Categoría | Desplegable | Las categorías B2C existentes |
| 6 | IWO Destino | Respuesta corta | Texto libre |
| 7 | Fecha de Entrega | Fecha | — |
| 8 | Operario | Respuesta corta | Texto libre o dropdown |

**Al crear el form:** Respuestas → Vincular a Sheets (crea la hoja automáticamente)

---

## Apps Script (trigger instantáneo)

En el Google Form: **⋮ → Editor de secuencia de comandos**

```javascript
function onFormSubmit(e) {
  const r = e.namedValues;

  const payload = {
    producto:        (r['Producto']           || [''])[0],
    lote:            (r['Lote Origen']         || [''])[0],
    cantidad:        (r['Cantidad']            || [''])[0],
    tipo_movimiento: (r['Tipo de Movimiento']  || [''])[0],
    categoria:       (r['Categoría']           || [''])[0],
    iwo_destino:     (r['IWO Destino']         || [''])[0],
    fecha:           (r['Fecha de Entrega']    || [''])[0],
    operario:        (r['Operario']            || [''])[0],
    timestamp:       new Date().toISOString()
  };

  UrlFetchApp.fetch('TU_URL_WEBHOOK_N8N', {
    method: 'POST',
    contentType: 'application/json',
    payload: JSON.stringify(payload)
  });
}
```

**Activador:** Apps Script → Activadores → Agregar activador
- Función: `onFormSubmit`
- Fuente: Desde formulario
- Tipo de evento: **Al enviar el formulario**

---

## n8n — Workflow

### Nodo 1: Webhook
- Tipo: `Webhook`
- Method: `POST`
- Path: `/aromaria-pt`
- Authentication: None (para el MVP)
- Response: `Immediately`

**Copiar la URL generada → pegar en Apps Script donde dice `TU_URL_WEBHOOK_N8N`**

> ⚠️ n8n debe estar expuesto a internet para que Apps Script lo alcance.
> Ya tienes Cloudflare Tunnel configurado (ver [[N8N]]). Verifica que el tunnel esté activo antes del demo.

---

### Nodo 2: Set (formatear datos)
Crea estas variables limpias:

```
nombre_item  → {{ $json.producto }} - Lote {{ $json.lote }} - {{ $json.fecha }}
cantidad     → {{ parseInt($json.cantidad) }}
producto     → {{ $json.producto }}
lote         → {{ $json.lote }}
tipo         → {{ $json.tipo_movimiento }}
categoria    → {{ $json.categoria }}
iwo          → {{ $json.iwo_destino }}
fecha        → {{ $json.fecha }}
operario     → {{ $json.operario }}
```

---

### Nodo 3: Monday — Create Item
- **Board ID:** [obtener del board Inventario PT]
- **Group:** [el grupo de entradas — verificar nombre]
- **Item Name:** `{{ $json.nombre_item }}`

**Column Values** (reemplazar IDs con los reales del board):

```json
{
  "ID_PRODUCTO":   { "text": "{{ $json.producto }}" },
  "ID_LOTE":       { "text": "{{ $json.lote }}" },
  "ID_CANTIDAD":   { "number": "{{ $json.cantidad }}" },
  "ID_TIPO":       { "label": "{{ $json.tipo }}" },
  "ID_CATEGORIA":  { "text": "{{ $json.categoria }}" },
  "ID_IWO":        { "text": "{{ $json.iwo }}" },
  "ID_FECHA":      { "date": "{{ $json.fecha }}" },
  "ID_OPERARIO":   { "text": "{{ $json.operario }}" }
}
```

---

## Cómo obtener los IDs de columna de Monday

**Opción A (UI):**
Abrir el board → clic en cualquier columna → **⋮ → Configuración de columna → copiar el ID**

**Opción B (API):**
```graphql
query {
  boards(ids: [TU_BOARD_ID]) {
    columns {
      id
      title
      type
    }
  }
}
```
Ejecutar en: `https://api.monday.com/v2` con tu API token en el header `Authorization`.

---

## Checklist de construcción

- [ ] Crear Google Form con 8 campos
- [ ] Vincular Form a Google Sheets
- [ ] Pegar Apps Script y activar trigger onFormSubmit
- [ ] Crear nodo Webhook en n8n — copiar URL al script
- [ ] Obtener Board ID del board Inventario PT en Monday
- [ ] Obtener IDs de las 8 columnas del board
- [ ] Configurar nodo Set con el mapeo
- [ ] Configurar nodo Monday Create Item con column_values
- [ ] Prueba completa: Form → verificar que aparece en Monday
- [ ] Ajustar formato de fecha si es necesario (DD/MM/YYYY vs YYYY-MM-DD)
- [ ] Preparar board Monday limpio para el demo (sin basura de pruebas)
- [ ] Generar QR Code con URL del Form
- [ ] Grabar video de respaldo del demo funcionando

---

## Estado al 23 de mayo

### Workflow A — Crear entradas PT (Board ID: 18397320051)
| Componente | Estado |
|---|---|
| Google Form (5 campos: Producto, Lote Origen, Cantidad, Fecha, Operario) | ✅ Creado y vinculado a Sheets |
| Apps Script trigger onFormSubmit | ✅ Activo |
| n8n Webhook → Set → Monday Create Item | ✅ Funciona end-to-end |
| Columnas mapeadas: Lote (text_mm1ad0z0), Cantidad (numeric_mkzzzdc4), Fecha (date_mkzzsg5j) | ✅ |
| Item Name: `producto - Lote lote - fecha` | ✅ |
| Webhook URL producción | ✅ `https://parties-taking-rose-working.trycloudflare.com/webhook/aromaria-pt` |

### Workflow B — Actualizar Ubicación actual de contenedores (Board ID: 18412458512)
| Componente | Estado |
|---|---|
| Tablero maestro de contenedores | ✅ Existe con CONT-001, CONT-002, CONT-003 en estado "Producción" |
| Google Form (2 campos: ID Contenedor, Operario) | ✅ Creado, título: "Transferencia a Almacén PT" |
| Vinculado a Google Sheets | ✅ |
| Apps Script con código correcto | ✅ Funciona — URL actualizada a tunnel activo |
| Trigger onFormSubmit activado | ✅ Activado y disparando |
| Webhook URL n8n | ✅ `https://whenever-skill-pose-atom.trycloudflare.com/webhook/aromaria-contenedores` (tunnel activo al 23 may) |
| n8n recibe datos del form | ✅ Confirmado — executions muestran Success |
| Nodo Monday "Get items by column value" | ✅ Funciona — encontró CONT-001 (id: `12091594700`) correctamente |
| Nodo "Change a column value" (Ubicación actual → Almacén PT) | ❌ Error de configuración — fix pendiente |
| QR codes pre-llenados (3 contenedores) | ⬜ URLs generadas, QRs pendientes de imprimir |
| Video de respaldo | ⬜ Pendiente |

---

## IDs de columnas — Tablero de contenedores (18412458512)
| Columna | ID |
|---|---|
| ID Contenedor | `text_mm36zms5` |
| Ubicación actual | `color_mm36nssa` |
| Cantidad | `numeric_mm36hde4` |
| Tipo | `color_mm36aez0` |

## URLs pre-llenadas para QR (Workflow B)
- CONT-001: `https://docs.google.com/forms/d/e/1FAIpQLScPTmXmIoSIbK8rFXufpAqHgaAUTy7o0m92Y1frJLwGVXNVdw/viewform?usp=pp_url&entry.1987577938=CONT-001`
- CONT-002: `https://docs.google.com/forms/d/e/1FAIpQLScPTmXmIoSIbK8rFXufpAqHgaAUTy7o0m92Y1frJLwGVXNVdw/viewform?usp=pp_url&entry.1987577938=CONT-002`
- CONT-003: `https://docs.google.com/forms/d/e/1FAIpQLScPTmXmIoSIbK8rFXufpAqHgaAUTy7o0m92Y1frJLwGVXNVdw/viewform?usp=pp_url&entry.1987577938=CONT-003`

---

## Estado al 2026-05-25 — Solución pendiente de probar (lunes 26)

El nodo Monday nativo v1 tiene un bug confirmado: convierte `itemId` a string internamente sin importar el tipo que pases. Se descartaron estas opciones:
- `{{ $json.id }}` → null (array, necesita índice)
- `{{ $json[0].id }}` → invalid type string
- `{{ parseInt($json[0].id) }}` → invalid type (bug del nodo)
- HTTP Request con JSON body → escaping doble rompe el JSON

### ✅ Solución definitiva — Nodo Code + HTTP Request

**Paso 1: Nodo Code** (insertar entre "Get items by column value" y HTTP Request)
```javascript
const mondayItems = $input.first().json;
const itemId = mondayItems[0].id;

return [{
  json: {
    query: `mutation { change_column_value(board_id: 18412458512, item_id: ${itemId}, column_id: "color_mm36nssa", value: "{\\"label\\": \\"Almacén PT\\"}") { id } }`
  }
}];
```

**Paso 2: HTTP Request**
- Method: POST
- URL: `https://api.monday.com/v2`
- Headers: `Content-Type: application/json`, `Authorization: Bearer TU_API_TOKEN`
- Body: JSON → Using Fields Below
  - Name: `query`
  - Value (modo expresión `=`): `={{ $json.query }}`

**Tunnel:** debe estar activo antes de cualquier prueba. URL puede cambiar al reiniciar cloudflared.

---

## Notas para el demo en vivo

- Tener el board Monday abierto en una pantalla/proyector antes del demo
- Tener el QR impreso O en pantalla para escanear con celular
- Tener el Cloudflare Tunnel activo y verificado
- Tener un elemento de prueba ya en el board (no mostrarlo vacío)
- Timing esperado: Form enviado → Monday actualizado en 2-3 segundos
- Tener video de respaldo listo por si algo falla en vivo
