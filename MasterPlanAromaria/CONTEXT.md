# Contexto del Proyecto — Aromaria

## La Empresa
Aromaria es una empresa de marketing olfativo y aromatización de interiores. Está en una fase activa de profesionalización: ha crecido pero mantiene procesos artesanales e informales que necesitan ser estructurados.

## El Usuario
- **Rol actual:** Analista de Control de Calidad en Aromaria
- **Oportunidad:** Se está formando un equipo interno de Automatización e IA impulsado por el dueño
- **Objetivo personal:** Ser aceptado como miembro de ese equipo presentando un proyecto claro y estructurado

## El Proyecto (Fase 1)
**Meta principal:** Dar trazabilidad e información en tiempo real de las operaciones de la empresa.

### Stack Tecnológico (La Triple Alianza)
- **Monday.com** — Capa de datos y UI. Las tablas funcionan como bases de datos relacionales. Un cambio en insumos actualiza automáticamente costos de producto terminado.
- **n8n** — Capa de integración. El "pegamento". Conecta el escaneo de QR en la nave con Monday en tiempo real sin intervención humana.
- **Claude** — Capa de inteligencia. Analista de operaciones 24/7 que responde preguntas basadas en datos reales.

### 3 Quick Wins (Entregables Clave)
1. **Módulo de Trazabilidad Total:** Flujo entrada/proceso/salida en Monday gestionado por operarios vía n8n (escaneo QR por contenedor, lote, pedido).
2. **Dashboard de Toma de Decisiones:** Panel que muestra "Dinero en Movimiento", no piezas. El dueño ve el margen real de cada Room Spray en tiempo real.
3. **Bot de Consultas Operativas:** Webhook n8n → Monday → Claude. El dueño pregunta por Slack/WhatsApp y recibe respuestas basadas en datos operativos.

### Backlog Estratégico (Dolores priorizados)
| Prioridad | Área | Dolor |
|-----------|------|-------|
| 1 | Estructural | Falta de trazabilidad e inventario |
| 2 | Estratégica | Incertidumbre sobre contrato/integración a nave principal |
| 3 | Organizacional | Caos en organigrama (35 personas, sin accountability) |
| 4 | Operativa | Ausencia de metodología 3F/5S y flujo de nave |
| 5 | Tecnológica | Automatización de room sprays (último paso, no primero) |

### Estructura Organizacional
- La nave tiene ~35 personas sin líneas de reporte claras
- Propuesta: Células Operativas con Team Leaders responsables del KPI de su área
- Ejemplo: Almacén → Team Leader responsable del indicador de stock

## Estado Actual
El proyecto está en fase de definición y documentación. Se está construyendo la propuesta para presentar al dueño y conseguir el ingreso al equipo de IA.
