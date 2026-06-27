from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

# ── Paleta Bosque Encantado ────────────────────────────────────────────────────
PERGAMINO  = RGBColor(0xFA, 0xF3, 0xE0)  # fondo principal
BOSQUE     = RGBColor(0x4A, 0x7C, 0x59)  # primario
DORADO     = RGBColor(0xD4, 0xA8, 0x43)  # acento
NOCHE      = RGBColor(0x1E, 0x2A, 0x1A)  # texto oscuro
CORAL      = RGBColor(0xE8, 0x83, 0x6A)  # pop
CREMA      = RGBColor(0xED, 0xE0, 0xC8)  # secundario claro
BLANCO     = RGBColor(0xFF, 0xFF, 0xFF)
BOSQUE_MED = RGBColor(0x6A, 0xA8, 0x7C)  # bosque más claro para variaciones

W = Inches(13.33)
H = Inches(7.5)
prs = Presentation()
prs.slide_width  = W
prs.slide_height = H
BLANK = prs.slide_layouts[6]

# ── Helpers ────────────────────────────────────────────────────────────────────
def rect(slide, l, t, w, h, fill=None, line=None):
    s = slide.shapes.add_shape(1, Inches(l), Inches(t), Inches(w), Inches(h))
    s.fill.solid() if fill else s.fill.background()
    if fill: s.fill.fore_color.rgb = fill
    s.line.fill.background() if not line else None
    if line: s.line.color.rgb = line
    else: s.line.fill.background()
    return s

def txt(slide, text, l, t, w, h, size=20, bold=False, color=NOCHE,
        align=PP_ALIGN.LEFT, italic=False):
    tb = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tb.word_wrap = True
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    r = p.add_run()
    r.text = text
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = color
    return tb

def bg(slide):
    rect(slide, 0, 0, 13.33, 7.5, fill=PERGAMINO)

def header(slide, title, subtitle=None):
    rect(slide, 0, 0, 13.33, 1.0, fill=BOSQUE)
    txt(slide, title, 0.5, 0.12, 10, 0.75,
        size=28, bold=True, color=DORADO)
    if subtitle:
        txt(slide, subtitle, 0.5, 0.68, 12.5, 0.35,
            size=14, color=CREMA, italic=True)
    # línea dorada decorativa
    rect(slide, 0, 1.0, 13.33, 0.06, fill=DORADO)

def chapter_tag(slide, label, l, t):
    rect(slide, l, t, 3.2, 0.42, fill=DORADO)
    txt(slide, label, l+0.1, t+0.04, 3.0, 0.34,
        size=14, bold=True, color=NOCHE, align=PP_ALIGN.CENTER)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 1 — Portada
# ══════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
bg(s)
rect(s, 0, 0, 0.22, 7.5, fill=BOSQUE)
rect(s, 0.22, 3.55, 13.11, 0.05, fill=DORADO)

txt(s, "ADVANX", 0.5, 0.8, 12, 1.8,
    size=110, bold=True, color=NOCHE)
txt(s, "Ordena.  Mide.  Escala.", 0.5, 2.5, 12, 0.65,
    size=26, color=BOSQUE, bold=True)
txt(s,
    '"Las PyMEs en Mexico no mueren por falta de clientes.\nMueren porque no pueden con los que ya tienen."',
    0.5, 3.75, 11.5, 1.3, size=20, italic=True, color=NOCHE)
txt(s, "El Gremio Advanx  ·  Sesion de alineacion  ·  Junio 2026",
    0.5, 6.85, 12.5, 0.45, size=13, color=BOSQUE)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 2 — El problema
# ══════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
bg(s)
header(s, "El problema que resolvemos")

puntos = [
    "No sabe que hay en inventario sin preguntarle a alguien",
    "Un reporte le toma 2 horas hacerlo a mano",
    "Cuando un empleado clave se va, el conocimiento se va con el",
    "Las decisiones se toman por intuicion, no por datos",
]
for i, p in enumerate(puntos):
    y = 1.2 + i * 1.28
    rect(s, 0.5, y, 0.08, 0.85, fill=CORAL)
    rect(s, 0.7, y, 11.9, 0.85, fill=CREMA)
    txt(s, p, 0.9, y+0.18, 11.5, 0.55, size=19, color=NOCHE)

rect(s, 0.5, 6.28, 12.3, 0.72, fill=BOSQUE)
txt(s,
    "Sintoma visible: alguien tiene como trabajo principal actualizar un Excel todos los dias.",
    0.7, 6.36, 12.0, 0.55, size=17, bold=True, color=DORADO)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 3 — Cliente ideal
# ══════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
bg(s)
header(s, "El Fundador ideal  —  a quien guiamos")

criterios = [
    ("Tamano",        "20 a 80 empleados"),
    ("Industrias",    "Manufactura  ·  Distribucion  ·  Alimentos  ·  Servicios con operacion fisica"),
    ("Sintoma",       "Alguien actualiza Excel a diario como su trabajo principal"),
    ("Dolor",         '"No se que pasa en mi negocio sin preguntarle a alguien"'),
    ("Filtro clave",  "No puedo con los clientes que tengo  ->  SI es nuestro Fundador"),
]
for i, (lbl, val) in enumerate(criterios):
    y = 1.18 + i * 1.1
    rect(s, 0.5, y, 2.8, 0.75, fill=BOSQUE)
    txt(s, lbl, 0.62, y+0.14, 2.6, 0.48, size=15, bold=True, color=DORADO)
    rect(s, 3.4, y, 9.5, 0.75, fill=CREMA)
    txt(s, val, 3.55, y+0.14, 9.2, 0.5, size=15, color=NOCHE)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 4 — Que es Advanx
# ══════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
bg(s)
header(s, "Advanx  —  El Gremio que guia expediciones")

txt(s,
    "Diagnostica, ordena y automatiza los procesos clave de una PyME\npara que pueda crecer con datos reales.",
    0.5, 1.18, 12, 0.9, size=21, color=NOCHE)

rect(s, 0.5, 2.22, 12.3, 1.05, fill=DORADO)
txt(s, "El diferenciador:", 0.72, 2.3, 4, 0.38, size=15, bold=True, color=NOCHE)
txt(s, "No hacemos reportes. Construimos sistemas.",
    0.72, 2.65, 12.0, 0.55, size=26, bold=True, color=NOCHE)

versus = [
    ("Contratar TI interno",  "Advanx trae metodo + ejecucion, no solo el recurso"),
    ("Implementar un ERP",    "Primero ordenamos el proceso, luego lo digitalizamos"),
    ("Seguir con Excel",      "El costo de la ineficiencia ya supero el costo del cambio"),
    ("Consultora grande",     "Acceso directo al experto  ·  Precio de PyME, no de corporativo"),
]
txt(s, "Versus las alternativas", 0.5, 3.45, 5, 0.38, size=14, bold=True, color=BOSQUE)
for i, (alt, razon) in enumerate(versus):
    y = 3.88 + i * 0.76
    rect(s, 0.5, y, 3.1, 0.58, fill=BOSQUE)
    txt(s, alt, 0.62, y+0.1, 2.9, 0.4, size=13, bold=True, color=DORADO)
    txt(s, razon, 3.72, y+0.12, 9.1, 0.42, size=14, color=NOCHE)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 5 — Vista general 4 capitulos
# ══════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
bg(s)
header(s, "La Expedicion  —  4 Capitulos  ·  16 Misiones  ·  ~4 meses")

capitulos = [
    ("CAP. I",  "El Horizonte",    "Que eres y hacia\ndonde vas",      "El Pergamino\ndel Fundador", BOSQUE),
    ("CAP. II", "La Fortaleza",    "Como operas y\nquien hace que",    "El Grimorio de\nOperaciones",  CORAL),
    ("CAP. III","La Brujula",      "Como mides\ny decides",            "El Mapa\ndel Mando",         BOSQUE),
    ("CAP. IV", "El Legado",       "Como creces\nsolo",                "El Codice",                  CORAL),
]
bw = 2.88
gap = 0.26
x0 = 0.45
for i, (num, nombre, pregunta, artefacto, color) in enumerate(capitulos):
    x = x0 + i * (bw + gap)
    rect(s, x, 1.12, bw, 4.22, fill=CREMA)
    rect(s, x, 1.12, bw, 0.05, fill=color)
    txt(s, num,     x+0.12, 1.2,  bw-0.2, 0.38, size=13, bold=True, color=color, align=PP_ALIGN.CENTER)
    txt(s, nombre,  x+0.1,  1.58, bw-0.18, 0.72, size=18, bold=True, color=NOCHE, align=PP_ALIGN.CENTER)
    rect(s, x+0.2, 2.32, bw-0.4, 0.04, fill=DORADO)
    txt(s, "16 misiones / 4 por capitulo", x+0.1, 2.42, bw-0.18, 0.38,
        size=11, color=BOSQUE, align=PP_ALIGN.CENTER)
    txt(s, pregunta, x+0.1, 2.84, bw-0.18, 1.0,
        size=14, italic=True, color=NOCHE, align=PP_ALIGN.CENTER)
    if i < 3:
        txt(s, "->", x+bw+0.02, 2.9, gap+0.05, 0.45,
            size=20, bold=True, color=DORADO, align=PP_ALIGN.CENTER)
    rect(s, x, 5.44, bw, 0.7, fill=color)
    txt(s, artefacto, x+0.08, 5.5, bw-0.14, 0.6,
        size=13, bold=True, color=BLANCO if color == BOSQUE else NOCHE,
        align=PP_ALIGN.CENTER)

txt(s, "Artefacto que se gana al cerrar cada capitulo  v",
    0.5, 6.18, 12.3, 0.38, size=12, color=BOSQUE, align=PP_ALIGN.CENTER)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 6 — Cap I El Horizonte
# ══════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
bg(s)
header(s, "Capitulo I  —  El Horizonte", "Que eres, para quien, cuanto cuesta y hacia donde vas")
chapter_tag(s, "CAP. I — EL HORIZONTE", 9.6, 0.08)

misiones = [
    ("M1", "Propuesta de valor + ICP",        "Mensaje claro que no cambia segun con quien hablas"),
    ("M2", "Motivador de compra real",          "Por que te compran de verdad — no lo que asumes"),
    ("M3", "Estructura de costos + obj. SMART","Punto de equilibrio en unidades  ·  metas con fecha"),
    ("M4", "Criterios de crecimiento + BMC",   "Cuando y como escalar  ·  sintesis visual del negocio"),
]
for i, (num, tema, resultado) in enumerate(misiones):
    y = 1.18 + i * 1.3
    rect(s, 0.5, y, 0.72, 0.72, fill=BOSQUE)
    txt(s, num, 0.5, y+0.12, 0.72, 0.48, size=17, bold=True,
        color=DORADO, align=PP_ALIGN.CENTER)
    rect(s, 1.32, y, 11.0, 0.72, fill=CREMA)
    txt(s, tema,      1.48, y+0.04,  10.7, 0.38, size=17, bold=True, color=NOCHE)
    txt(s, resultado, 1.48, y+0.4,   10.7, 0.3,  size=14, color=BOSQUE)

rect(s, 0.5, 6.3, 12.3, 0.72, fill=DORADO)
txt(s, "Artefacto: EL PERGAMINO DEL FUNDADOR  —  propuesta de valor + ICP + costos + objetivos SMART",
    0.68, 6.38, 12.0, 0.56, size=15, bold=True, color=NOCHE)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 7 — Cap II La Fortaleza
# ══════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
bg(s)
header(s, "Capitulo II  —  La Fortaleza", "Como hacemos las cosas y quien es responsable de que")
chapter_tag(s, "CAP. II — LA FORTALEZA", 9.3, 0.08)

misiones = [
    ("M5", "Mapeo de procesos clave",       "Mapa de como fluye el trabajo de punta a punta"),
    ("M6", "Documentacion de SOPs",          "Pasos escritos para los procesos que mas afectan al cliente"),
    ("M7", "Roles y accountability",         "Quien es responsable de que — sin depender de la memoria"),
    ("M8", "Revision de implementacion",     "Ajuste real tras 2 semanas ejecutando en campo"),
]
for i, (num, tema, resultado) in enumerate(misiones):
    y = 1.18 + i * 1.3
    rect(s, 0.5, y, 0.72, 0.72, fill=CORAL)
    txt(s, num, 0.5, y+0.12, 0.72, 0.48, size=17, bold=True,
        color=NOCHE, align=PP_ALIGN.CENTER)
    rect(s, 1.32, y, 11.0, 0.72, fill=CREMA)
    txt(s, tema,      1.48, y+0.04,  10.7, 0.38, size=17, bold=True, color=NOCHE)
    txt(s, resultado, 1.48, y+0.4,   10.7, 0.3,  size=14, color=BOSQUE)

rect(s, 0.5, 6.3, 12.3, 0.72, fill=CORAL)
txt(s, "Artefacto: EL GRIMORIO DE OPERACIONES  —  mapa de procesos + SOPs + roles",
    0.68, 6.38, 12.0, 0.56, size=15, bold=True, color=NOCHE)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 8 — Cap III La Brujula
# ══════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
bg(s)
header(s, "Capitulo III  —  La Brujula", "Como se si voy bien y que hago cuando algo no va")
chapter_tag(s, "CAP. III — LA BRUJULA", 9.4, 0.08)

misiones = [
    ("M9",  "Definicion de KPIs",            "3 a 5 metricas que realmente importan (no vanity metrics)"),
    ("M10", "Dashboard simple",               "Google Sheet que se actualiza en 10 min por semana"),
    ("M11", "Protocolo de decisiones",        "Reglas escritas: si X baja de Y -> hago Z"),
    ("M12", "Primera revision con datos",     "Primera decision tomada con datos reales — en vivo"),
]
for i, (num, tema, resultado) in enumerate(misiones):
    y = 1.18 + i * 1.3
    rect(s, 0.5, y, 0.72, 0.72, fill=BOSQUE)
    txt(s, num, 0.5, y+0.12, 0.72, 0.48, size=17, bold=True,
        color=DORADO, align=PP_ALIGN.CENTER)
    rect(s, 1.32, y, 11.0, 0.72, fill=CREMA)
    txt(s, tema,      1.48, y+0.04,  10.7, 0.38, size=17, bold=True, color=NOCHE)
    txt(s, resultado, 1.48, y+0.4,   10.7, 0.3,  size=14, color=BOSQUE)

rect(s, 0.5, 6.3, 12.3, 0.72, fill=DORADO)
txt(s, "Artefacto: EL MAPA DEL MANDO  —  dashboard + KPIs + protocolo de decisiones",
    0.68, 6.38, 12.0, 0.56, size=15, bold=True, color=NOCHE)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 9 — Cap IV El Legado
# ══════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
bg(s)
header(s, "Capitulo IV  —  El Legado", "Como hago que el crecimiento se sostenga solo")
chapter_tag(s, "CAP. IV — EL LEGADO", 9.5, 0.08)

misiones = [
    ("M13", "Diseno del flywheel",            "Mapa del ciclo de crecimiento propio del negocio"),
    ("M14", "Sistema de retencion y referidos","Mecanismo concreto que activa el flywheel"),
    ("M15", "Criterios de escalamiento",       "Cuando contratar, abrir turno, subir precios — con datos"),
    ("M16", "Documento maestro + roadmap",     "Todo consolidado + hoja de ruta para el siguiente ano"),
]
for i, (num, tema, resultado) in enumerate(misiones):
    y = 1.18 + i * 1.3
    rect(s, 0.5, y, 0.72, 0.72, fill=CORAL)
    txt(s, num, 0.5, y+0.12, 0.72, 0.48, size=17, bold=True,
        color=NOCHE, align=PP_ALIGN.CENTER)
    rect(s, 1.32, y, 11.0, 0.72, fill=CREMA)
    txt(s, tema,      1.48, y+0.04,  10.7, 0.38, size=17, bold=True, color=NOCHE)
    txt(s, resultado, 1.48, y+0.4,   10.7, 0.3,  size=14, color=BOSQUE)

rect(s, 0.5, 6.3, 12.3, 0.72, fill=BOSQUE)
txt(s, "Artefacto: EL CODICE  —  consolida los 3 artefactos anteriores + flywheel + roadmap 12 meses",
    0.68, 6.38, 12.0, 0.56, size=15, bold=True, color=DORADO)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 10 — Caso UMA Spa
# ══════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
bg(s)
header(s, "Primera Expedicion: UMA Spa", "Capitulo I en curso — 3 de 4 misiones completadas")

rect(s, 0.5, 1.12, 5.9, 5.0, fill=CREMA)
txt(s, "ANTES DE ADVANX", 0.65, 1.2, 5.6, 0.42, size=15, bold=True, color=CORAL)
antes = [
    "Sin propuesta de valor consistente",
    "Sin saber por que le compraban",
    "Precios definidos por intuicion",
    "Sin estructura de costos",
    "Sin punto de equilibrio conocido",
]
for i, l in enumerate(antes):
    txt(s, "x   " + l, 0.72, 1.72 + i*0.72, 5.5, 0.6, size=15, color=NOCHE)

rect(s, 6.6, 1.12, 6.2, 5.0, fill=BOSQUE)
txt(s, "HALLAZGOS EN 3 MISIONES", 6.75, 1.2, 6.0, 0.42,
    size=15, bold=True, color=DORADO)
hallazgos = [
    "No compran un masaje — compran la\ncerteza de presencia total sin prisa.",
    "Punto de equilibrio: 34 masajes/mes",
    "Capacidad instalada: 96 masajes/mes",
    "Mes tipico actual: 27 masajes",
    "Brecha a rentabilidad: 7 masajes mas\n(menos de 2 por semana)",
]
for i, h in enumerate(hallazgos):
    txt(s, "->  " + h, 6.78, 1.72 + i*0.84, 5.9, 0.78, size=14, color=BLANCO)

rect(s, 0.5, 6.25, 12.3, 0.82, fill=DORADO)
txt(s,
    "El problema no era capacidad. Era visibilidad.\nEso es lo que solo da la metodologia.",
    0.68, 6.32, 12.0, 0.7, size=17, bold=True, color=NOCHE, align=PP_ALIGN.CENTER)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 11 — Modelo de negocio
# ══════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
bg(s)
header(s, "Como se paga la Expedicion")

servicios = [
    ("Diagnostico",            "$25,000 MXN",  "2 a 3 semanas",
     "El Fundador ve el mapa completo antes de comprometerse."),
    ("Sprint 1 mes",           "$22,000 MXN",  "4 semanas",
     "1 proceso automatizado de punta a punta. Resultados rapidos."),
    ("Acompanamiento\n3 meses","$18,000/mes",  "12 semanas",
     "La Expedicion completa. 1 Fundador activo cubre la meta."),
]
for i, (nombre, precio, dur, desc) in enumerate(servicios):
    x = 0.5 + i * 4.28
    rect(s, x, 1.1, 3.98, 4.6, fill=CREMA)
    rect(s, x, 1.1, 3.98, 0.06, fill=BOSQUE if i != 1 else CORAL)
    txt(s, nombre, x+0.15, 1.22, 3.7, 0.72,
        size=18, bold=True, color=NOCHE, align=PP_ALIGN.CENTER)
    txt(s, precio, x+0.1,  2.0,  3.8, 0.72,
        size=30, bold=True, color=BOSQUE if i != 1 else CORAL,
        align=PP_ALIGN.CENTER)
    txt(s, dur,    x+0.1,  2.78, 3.8, 0.42,
        size=14, color=BOSQUE, align=PP_ALIGN.CENTER)
    txt(s, desc,   x+0.18, 3.28, 3.65, 1.3,
        size=14, color=NOCHE, align=PP_ALIGN.CENTER)

rect(s, 0.5, 5.88, 12.3, 0.52, fill=BOSQUE)
txt(s,
    "Gancho: si el Fundador contrata acompanamiento tras el diagnostico -> $10,000 de credito.",
    0.68, 5.96, 12.0, 0.38, size=14, bold=True, color=DORADO, align=PP_ALIGN.CENTER)
txt(s, "1 Fundador en acompanamiento = $18,000/mes = meta minima cubierta",
    0.5, 6.52, 12.3, 0.46, size=16, bold=True, color=BOSQUE, align=PP_ALIGN.CENTER)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 12 — Mercado
# ══════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
bg(s)
header(s, "Por que el momento es ahora")

datos = [
    ("7.7%",  "crecimiento anual\nconsultoria PyME"),
    ("12.8%", "crecimiento anual\nconsultoria tecnologica"),
    ("76%",   "de PyMEs mexicanas\naun sin digitalizar"),
]
for i, (num, label) in enumerate(datos):
    x = 0.6 + i * 4.15
    rect(s, x, 1.1, 3.7, 2.5, fill=CREMA)
    rect(s, x, 1.1, 3.7, 0.06, fill=DORADO)
    txt(s, num,   x+0.1, 1.22, 3.5, 1.1,
        size=56, bold=True, color=BOSQUE, align=PP_ALIGN.CENTER)
    txt(s, label, x+0.1, 2.35, 3.5, 0.9,
        size=15, color=NOCHE, align=PP_ALIGN.CENTER)

rect(s, 0.5, 3.82, 12.3, 1.52, fill=BOSQUE)
txt(s, "El espacio integrado en el Valle de Toluca esta vacio.",
    0.68, 3.9, 12.0, 0.52, size=21, bold=True, color=DORADO)
txt(s,
    "Nadie combina procesos + personas + datos + IA con presencia local. "
    "Los competidores atacan cada eje por separado.",
    0.68, 4.45, 12.0, 0.76, size=15, color=BLANCO)

rect(s, 0.5, 5.48, 12.3, 1.58, fill=DORADO)
txt(s,
    "La demanda existe. El mercado es inmaduro.\nQuien llega primero con metodologia probada define el estandar.",
    0.68, 5.6, 12.0, 1.2, size=20, bold=True, color=NOCHE, align=PP_ALIGN.CENTER)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 13 — Por que nosotros
# ══════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
bg(s)
header(s, "Por que El Gremio Advanx")

razones = [
    ("Expedicion real validada", "UMA Spa — metodologia ejecutada en campo, no disenada en papel"),
    ("Sin intermediarios",       "El Fundador habla directo con quien implementa y entrega"),
    ("Enfoque correcto",         "Primero ordenamos, luego automatizamos — no se automatiza el caos"),
    ("Experiencia unica",        "La unica consultoria que convierte el crecimiento en una aventura"),
]
for i, (titulo, desc) in enumerate(razones):
    y = 1.2 + i * 1.4
    rect(s, 0.5, y, 0.1, 1.05, fill=DORADO)
    rect(s, 0.72, y, 12.1, 1.05, fill=CREMA)
    txt(s, titulo, 0.88, y+0.1,  11.7, 0.45, size=19, bold=True, color=BOSQUE)
    txt(s, desc,   0.88, y+0.55, 11.7, 0.45, size=16, color=NOCHE)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 14 — Conversacion con la socia
# ══════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
bg(s)
header(s, "La conversacion que necesitamos tener")

preguntas = [
    "Que capacidades traes tu que complementan las mias?",
    "Como dividimos roles dentro de una Expedicion con un Fundador?",
    "Cual seria el primer Fundador que abordaríamos juntos?",
    "Que necesitas ver o entender antes de comprometerte?",
]
for i, p in enumerate(preguntas):
    y = 1.2 + i * 1.42
    rect(s, 0.5, y, 1.0, 1.0, fill=BOSQUE)
    txt(s, str(i+1), 0.5, y+0.16, 1.0, 0.68,
        size=34, bold=True, color=DORADO, align=PP_ALIGN.CENTER)
    rect(s, 1.62, y, 11.2, 1.0, fill=CREMA)
    txt(s, p, 1.8, y+0.26, 10.8, 0.55, size=20, color=NOCHE)

rect(s, 0.5, 6.7, 12.3, 0.58, fill=BOSQUE)
txt(s, "Advanx  ·  Ordena. Mide. Escala.  ·  El Gremio que guia expediciones",
    0.65, 6.78, 12.0, 0.42, size=14, bold=True, color=DORADO, align=PP_ALIGN.CENTER)

# ══════════════════════════════════════════════════════════════════════════════
# Guardar
# ══════════════════════════════════════════════════════════════════════════════
output = r"C:\Users\1544\Documents\GOOGLE DRIVE RECOVERY\OBSIDIAN\DIGITAL BRAIN\Advanx — Presentación para Socia.pptx"
prs.save(output)
print("Guardado:", output)
