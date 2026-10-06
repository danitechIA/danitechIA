#!/usr/bin/env python3
"""Genera los gráficos del perfil de GitHub de danitechIA (SVG animados + PNG para redes).
Uso: python3 assets/generar.py   →  assets/*.svg  y  ~/Escritorio/GitHub-imagenes-redes/*.png"""
import html, os, subprocess

AQUI = os.path.dirname(os.path.abspath(__file__))
FUENTE = "'Segoe UI', Ubuntu, 'Helvetica Neue', Arial, sans-serif"
MONO = "'JetBrains Mono', 'Fira Code', Consolas, 'Courier New', monospace"
V, C, R = "#8B5CF6", "#22D3EE", "#F43F5E"          # violeta, cian, carmesí

TEMAS = {
    "oscuro": dict(fondo="#0D1117", panel="#161B22", borde="#30363D", texto="#E6EDF3", suave="#8B949E", rejilla="#21262D"),
    "claro":  dict(fondo="#FFFFFF", panel="#F6F8FA", borde="#D0D7DE", texto="#1F2328", suave="#59636E", rejilla="#EAEEF2"),
}


def e(t):
    return html.escape(t, quote=True)


# ───────────────────────── banner del perfil ─────────────────────────
def banner(tema):
    t = TEMAS[tema]
    W, H = 1200, 320
    lineas = [("$", "whoami", ""), ("", "Daniel Dans · Full-Stack & AI Developer", t["texto"]),
              ("$", "uptime --servicios", ""), ("", "VPS Linux 24/7 · Docker · systemd · SSL", t["texto"]),
              ("$", "ls ~/proyectos", ""), ("", "irokai  tiktokai  skill-creator  n8n", C)]
    term = ""
    for i, (p, txt, col) in enumerate(lineas):
        y = 128 + i * 26
        d = 0.6 + i * 0.55
        color = col or t["suave"]
        pre = f'<tspan fill="{R}">{p}&#160;</tspan>' if p else ""
        term += (f'<text x="742" y="{y}" class="mono" fill="{color}" style="animation-delay:{d:.2f}s" opacity="0">'
                 f'<animate attributeName="opacity" from="0" to="1" begin="{d:.2f}s" dur=".35s" fill="freeze"/>{pre}{e(txt)}</text>')
    particulas = "".join(
        f'<circle cx="{x}" cy="{H + 10}" r="{r}" fill="{col}" opacity=".55"><animate attributeName="cy" from="{H + 10}" to="-10" dur="{dur}s" begin="{b}s" repeatCount="indefinite"/>'
        f'<animate attributeName="opacity" values="0;.7;0" dur="{dur}s" begin="{b}s" repeatCount="indefinite"/></circle>'
        for x, r, col, dur, b in [(60, 2, V, 9, 0), (180, 1.5, C, 11, 2), (330, 2.5, V, 13, 4), (470, 1.5, C, 8, 1),
                                  (610, 2, R, 12, 3), (1140, 2, C, 10, 5), (1060, 1.5, V, 14, 6), (690, 1.5, C, 9, 7)])
    rejilla = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="{t["rejilla"]}" stroke-width="1"/>' for x in range(0, W, 40)) + \
              "".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="{t["rejilla"]}" stroke-width="1"/>' for y in range(0, H, 40))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Daniel Dans — Full-Stack &amp; AI Developer">
<defs>
 <linearGradient id="nombre" x1="0" x2="1" y1="0" y2="0">
  <stop offset="0" stop-color="{V}"><animate attributeName="stop-color" values="{V};{C};{R};{V}" dur="8s" repeatCount="indefinite"/></stop>
  <stop offset="1" stop-color="{C}"><animate attributeName="stop-color" values="{C};{R};{V};{C}" dur="8s" repeatCount="indefinite"/></stop>
 </linearGradient>
 <radialGradient id="luzV"><stop offset="0" stop-color="{V}" stop-opacity=".45"/><stop offset="1" stop-color="{V}" stop-opacity="0"/></radialGradient>
 <radialGradient id="luzC"><stop offset="0" stop-color="{C}" stop-opacity=".35"/><stop offset="1" stop-color="{C}" stop-opacity="0"/></radialGradient>
 <clipPath id="marco"><rect width="{W}" height="{H}" rx="18"/></clipPath>
 <clipPath id="escribe"><rect x="60" y="168" width="0" height="40"><animate attributeName="width" from="0" to="620" begin=".4s" dur="2.2s" fill="freeze" calcMode="spline" keySplines=".4 0 .2 1" keyTimes="0;1"/></rect></clipPath>
 <style>.mono{{font-family:{MONO};font-size:16px}}.sans{{font-family:{FUENTE}}}</style>
</defs>
<g clip-path="url(#marco)">
 <rect width="{W}" height="{H}" fill="{t["fondo"]}"/>
 <g opacity=".6">{rejilla}</g>
 <circle cx="230" cy="90" r="260" fill="url(#luzV)"><animate attributeName="r" values="240;290;240" dur="7s" repeatCount="indefinite"/></circle>
 <circle cx="1000" cy="260" r="240" fill="url(#luzC)"><animate attributeName="r" values="260;210;260" dur="9s" repeatCount="indefinite"/></circle>
 {particulas}
 <text x="60" y="78" class="sans" font-size="18" font-weight="600" fill="{t["suave"]}" letter-spacing="4">HOLA, SOY</text>
 <text x="56" y="152" class="sans" font-size="76" font-weight="800" fill="url(#nombre)" letter-spacing="-1.5">Daniel Dans</text>
 <g clip-path="url(#escribe)"><text x="60" y="198" class="sans" font-size="26" font-weight="600" fill="{t["texto"]}">Full-Stack &amp; AI Developer · Barcelona</text></g>
 <text x="60" y="246" class="sans" font-size="17" fill="{t["suave"]}">Apps con IA, automatización y Linux que funcionan en producción, de verdad.</text>
 <g transform="translate(60 268)">
  {"".join(f'<g transform="translate({i * 132} 0)"><rect width="122" height="30" rx="15" fill="{t["panel"]}" stroke="{t["borde"]}"/><circle cx="18" cy="15" r="5" fill="{col}"><animate attributeName="opacity" values="1;.35;1" dur="2.4s" begin="{i * .4}s" repeatCount="indefinite"/></circle><text x="32" y="20" class="sans" font-size="13" font-weight="600" fill="{t["texto"]}">{txt}</text></g>' for i, (txt, col) in enumerate([("Python", V), ("JavaScript", C), ("Rust", R), ("Linux", V)]))}
 </g>
 <g>
  <rect x="720" y="56" width="440" height="228" rx="12" fill="{t["panel"]}" stroke="{t["borde"]}"/>
  <circle cx="742" cy="78" r="6" fill="#FF5F57"/><circle cx="762" cy="78" r="6" fill="#FEBC2E"/><circle cx="782" cy="78" r="6" fill="#28C840"/>
  <text x="940" y="83" class="mono" font-size="13" fill="{t["suave"]}" text-anchor="middle">dani@vps: ~</text>
  {term}
  <rect x="742" y="276" width="10" height="3" fill="{C}"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>
 </g>
 <rect width="{W}" height="{H}" rx="18" fill="none" stroke="{t["borde"]}"/>
</g>
</svg>'''


# ───────────────────────── tarjetas de proyecto ─────────────────────────
PROYECTOS = {
    "carme": dict(nombre="Estética Carme Cots", estado="Cliente real · en producción", color="#C9A227",
                  desc=["Web de un centro de estética Skeyndor en", "Barcelona: tratamientos, productos y reservas."],
                  chips=["React", "Vite", "GSAP", "SEO"], icono="✦"),
    "akane": dict(nombre="AKANE 茜", estado="Prototipo · animaciones cinematográficas", color="#DC2626",
                  desc=["Entrada 3D por scroll: la cámara atraviesa", "el pórtico de un templo. Sin librerías."],
                  chips=["HTML", "CSS", "JavaScript", "Vercel"], icono="茜"),
    "irokai": dict(nombre="Irokai 色界", estado="Producto · en venta pronto", color=R,
                   desc=["Personalización para Linux: cada fondo de pantalla", "genera su propia estética y lo viste todo a juego."],
                   chips=["Bash", "Python", "Lua", "Hyprland"], icono="色"),
    "tiktokai": dict(nombre="TikTokAI", estado="Editor web con IA", color=V,
                     desc=["Subtítulos karaoke palabra a palabra con Whisper", "y un editor con timeline estilo CapCut."],
                     chips=["FastAPI", "Groq Whisper", "ffmpeg", "JS"], icono="▶"),
    "skill": dict(nombre="AI Skill Creator", estado="App de escritorio · release", color=C,
                  desc=["Crea y gestiona skills para agentes de código IA", "y chatea con el agente, sin usar la terminal."],
                  chips=["Tauri 2", "Rust", "Tokio", "JS"], icono="⚡"),
    "tikets": dict(nombre="Analizador de Tickets", estado="Automatización en producción", color="#F59E0B",
                   desc=["Extrae importe, IVA y fecha de una foto de un", "ticket con IA y lo guarda en MySQL y Sheets."],
                   chips=["n8n", "Docker", "MySQL", "OpenAI"], icono="🧾"),
    "portafolio": dict(nombre="Portafolio", estado="Web · CI/CD en Vercel", color="#10B981",
                       desc=["Mi portafolio: React + Vite, animaciones GSAP,", "bilingüe y con chatbot integrado."],
                       chips=["React", "Vite", "GSAP", "Vercel"], icono="◆"),
    "littlelemon": dict(nombre="Little Lemon API", estado="Capstone · Meta Back-End", color="#EAB308",
                        desc=["API REST de reservas y menú de un restaurante", "con Django REST Framework y MySQL."],
                        chips=["Django", "DRF", "MySQL", "Tests"], icono="🍋"),
}


def tarjeta(p):
    d = PROYECTOS[p]; t = TEMAS["oscuro"]; W, H = 880, 380; col = d["color"]
    chips = "".join(f'<g transform="translate({sum(len(c) * 10 + 46 for c in d["chips"][:i])} 0)"><rect width="{len(c) * 10 + 34}" height="34" rx="17" fill="{col}" fill-opacity=".14" stroke="{col}" stroke-opacity=".5"/>'
                    f'<text x="{(len(c) * 10 + 34) / 2}" y="23" text-anchor="middle" class="s" font-size="15" font-weight="600" fill="{t["texto"]}">{e(c)}</text></g>' for i, c in enumerate(d["chips"]))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{e(d["nombre"])}">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{col}" stop-opacity=".22"/><stop offset=".55" stop-color="{t["panel"]}" stop-opacity="0"/></linearGradient>
<style>.s{{font-family:{FUENTE}}}</style></defs>
<rect width="{W}" height="{H}" rx="22" fill="{t["panel"]}"/>
<rect width="{W}" height="{H}" rx="22" fill="url(#g)"/>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="21" fill="none" stroke="{t["borde"]}" stroke-width="2"/>
<rect x="0" y="0" width="{W}" height="6" rx="3" fill="{col}"><animate attributeName="opacity" values="1;.55;1" dur="3s" repeatCount="indefinite"/></rect>
<g transform="translate(48 64)">
 <rect width="78" height="78" rx="20" fill="{col}" fill-opacity=".16" stroke="{col}" stroke-opacity=".6"/>
 <text x="39" y="53" text-anchor="middle" font-size="40" class="s" fill="{t["texto"]}">{e(d["icono"])}</text>
</g>
<text x="150" y="98" class="s" font-size="38" font-weight="800" fill="{t["texto"]}">{e(d["nombre"])}</text>
<g transform="translate(150 116)"><circle cx="7" cy="9" r="6" fill="{col}"><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle>
<text x="22" y="15" class="s" font-size="17" font-weight="600" fill="{t["suave"]}">{e(d["estado"])}</text></g>
<text x="48" y="208" class="s" font-size="22" fill="{t["texto"]}">{e(d["desc"][0])}</text>
<text x="48" y="240" class="s" font-size="22" fill="{t["texto"]}">{e(d["desc"][1])}</text>
<g transform="translate(48 292)">{chips}</g>
<text x="{W - 48}" y="98" text-anchor="end" class="s" font-size="26" fill="{col}">↗</text>
</svg>'''


# ───────────────────────── cabeceras de repositorio ─────────────────────────
def cabecera(p, subtitulo):
    d = PROYECTOS[p]; t = TEMAS["oscuro"]; W, H = 1280, 300; col = d["color"]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{e(d["nombre"])}">
<defs><radialGradient id="l"><stop offset="0" stop-color="{col}" stop-opacity=".45"/><stop offset="1" stop-color="{col}" stop-opacity="0"/></radialGradient>
<clipPath id="m"><rect width="{W}" height="{H}" rx="20"/></clipPath><style>.s{{font-family:{FUENTE}}}</style></defs>
<g clip-path="url(#m)"><rect width="{W}" height="{H}" fill="{t["fondo"]}"/>
{"".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="{t["rejilla"]}"/>' for x in range(0, W, 48))}
<circle cx="{W - 220}" cy="150" r="300" fill="url(#l)"><animate attributeName="r" values="280;330;280" dur="8s" repeatCount="indefinite"/></circle>
<text x="{W - 210}" y="205" text-anchor="middle" font-size="170" class="s" fill="{col}" fill-opacity=".9">{e(d["icono"])}</text>
<text x="70" y="140" class="s" font-size="64" font-weight="800" fill="{t["texto"]}" letter-spacing="-1">{e(d["nombre"])}</text>
<text x="72" y="190" class="s" font-size="26" fill="{t["suave"]}">{e(subtitulo)}</text>
<rect x="72" y="222" width="180" height="6" rx="3" fill="{col}"/>
<rect width="{W}" height="{H}" rx="20" fill="none" stroke="{t["borde"]}" stroke-width="2"/></g></svg>'''


def png(svg_txt, ruta, w, h):
    tmp = ruta + ".svg"; open(tmp, "w", encoding="utf-8").write(svg_txt)
    subprocess.run(["rsvg-convert", "-w", str(w), "-h", str(h), "-o", ruta, tmp], check=True); os.remove(tmp)


if __name__ == "__main__":
    for tema in TEMAS:
        open(f"{AQUI}/banner-{tema}.svg", "w", encoding="utf-8").write(banner(tema))
    for p in PROYECTOS:
        open(f"{AQUI}/card-{p}.svg", "w", encoding="utf-8").write(tarjeta(p))
    SUB = {"carme": "Web de un centro de estética en Barcelona", "akane": "Prototipo de animaciones cinematográficas por scroll",
           "tiktokai": "Subtítulos karaoke con IA para vídeo vertical", "skill": "Skills para agentes de código IA, sin terminal",
           "tikets": "Tickets y facturas a datos con IA y n8n", "portafolio": "React · Vite · GSAP · bilingüe",
           "littlelemon": "Django REST Framework · MySQL · tests", "irokai": "Una estética para cada fondo"}
    for p, s in SUB.items():
        open(f"{AQUI}/header-{p}.svg", "w", encoding="utf-8").write(cabecera(p, s))
    esc = subprocess.run(["xdg-user-dir", "DESKTOP"], capture_output=True, text=True).stdout.strip() or os.path.expanduser("~/Escritorio")
    redes = os.path.join(esc, "GitHub-imagenes-redes"); os.makedirs(redes, exist_ok=True)
    for p, s in SUB.items():   # imagen «social preview» 1280×640 para subir a mano en cada repo
        svg = cabecera(p, s).replace('height="300" viewBox="0 0 1280 300"', 'height="640" viewBox="0 -170 1280 640"')
        png(svg, os.path.join(redes, f"{p}.png"), 1280, 640)
    print("gráficos generados")
