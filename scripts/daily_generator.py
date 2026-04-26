import os
import json
import requests
import datetime
import re

# --- CONFIGURACIÓN ---
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
MODEL = "llama-3.3-70b-versatile"

# Rutas de archivos
BLOG_DIR = "blog/"
BLOG_INDEX = "blog.html"

# DATOS REALES DE DAN TAGLE (Rescatados)
CASES = [
    "Ssangyong: DOOH Reactivo y Pincel Robótico Gigante",
    "CorreosChile: Tinder de cartas navideñas automatizado",
    "Tenpo: Ruleta BTL conectada a Data en tiempo real",
    "Bupa: App Maps with Memory para pacientes con Alzheimer",
    "MIDEA: Lanzamiento 360 con Effie de Oro",
    "Oracle NetSuite Partner: Dominación de SEO/AEO B2B",
    "KidZania: GiftCard de Tiempo digital",
    "Sexshop Chile: Publicidad creativa evadiendo censura (Oro WINA)"
]

DEVELOPMENTS = [
    "Tikk: Vende por WhatsApp con una tienda completa en el chat",
    "Neural Eye: IA que predice focos de atención en diseño y UX",
    "Saben: Trivia IA para gamificación de marcas",
    "LeyResponsable: Automatización de trámites legales",
    "Criptobot: Señales de trading automáticas",
    "Teve: Plataforma de video y streaming profesional"
]

STYLE_GUIDE = f"""
Eres Dan Tagle, un consultor de software y automatización enfocado en RESULTADOS, no en palabras bonitas.
Tu tono es directo, experto y utilitario.
Cuentas con casos reales como: {", ".join(CASES[:4])}.
Tus herramientas son: {", ".join(DEVELOPMENTS[:4])}.

REGLAS DE ORO:
1. NO USES conceptos rebuscados como 'orquestación holística'. Habla de ventas, tiempo y eficiencia.
2. Cada artículo debe resolver un PROBLEMA REAL (ej: 'Cómo vender más en WhatsApp').
3. Cita siempre uno de tus CASOS o APPS como la solución probada.
4. El objetivo es que el lector diga: 'Esto me sirve, voy a contactar a Dan'.
"""

def get_topics():
    topics = [
        "Cómo vender en WhatsApp sin perder la cabeza: La guía de Tikk",
        "IA Predictiva: Cómo saber dónde mirarán tus clientes antes de lanzar tu web",
        "Matchmaking Digital: Lo que aprendimos automatizando CorreosChile",
        "SEO vs AEO: Por qué aparecer en Google ya no es suficiente en 2026",
        "Automatización B2B: Cómo hackear el alcance orgánico en nichos difíciles",
        "Gamificación Real: Por qué una trivia IA vende más que un banner"
    ]
    day = datetime.datetime.now().day
    return topics[day % len(topics)]

def generate_content(topic):
    prompt = f"""
    {STYLE_GUIDE}
    
    ESCRIBE UN ARTÍCULO UTILITARIO SOBRE: "{topic}"
    
    REQUISITOS:
    1. Título directo y con beneficio claro.
    2. Contenido de +500 palabras con pasos accionables.
    3. Cita un caso real de Dan Tagle para validar el punto.
    4. DEVOLVER ÚNICAMENTE UN OBJETO JSON: 'title', 'date', 'slug', 'content_html', 'meta_description'.
    """
    
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "Eres un experto en software que solo responde en JSON técnico."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5
    }
    
    try:
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
        result = response.json()
        if 'choices' not in result:
            print(f"Error de API: {result}")
            return None
        raw_content = result['choices'][0]['message']['content']
        clean_json = re.sub(r'```json\s*|\s*```', '', raw_content).strip()
        return json.loads(re.search(r'\{.*\}', clean_json, re.DOTALL).group())
    except Exception as e:
        print(f"Error: {e}")
        return None

def create_page(article):
    if not article: return
    html = f"""<!DOCTYPE html>
<html lang="es-CL">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{article['title']} | Dan Tagle</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;900&display=swap" rel="stylesheet">
    <style>body {{ font-family: 'Outfit', sans-serif; background: #050505; color: #f4f4f5; }}</style>
</head>
<body class="p-8 md:p-20">
    <nav class="mb-20"><a href="../index.html" class="font-black uppercase tracking-tighter">DAN TAGLE .</a></nav>
    <main class="max-w-3xl mx-auto">
        <h1 class="text-4xl md:text-6xl font-black mb-10 uppercase leading-none">{article['title']}</h1>
        <div class="prose prose-invert max-w-none text-zinc-400 leading-relaxed">
            {article['content_html']}
        </div>
        <footer class="mt-20 pt-10 border-t border-white/5">
            <a href="../blog.html" class="text-xs font-black uppercase tracking-widest">← Volver al Blog</a>
        </footer>
    </main>
</body>
</html>"""
    filename = f"{BLOG_DIR}{article['slug']}.html"
    with open(filename, 'w') as f: f.write(html)
    print(f"✅ Artículo creado: {filename}")

if __name__ == "__main__":
    if GROQ_API_KEY:
        topic = get_topics()
        data = generate_content(topic)
        create_page(data)
