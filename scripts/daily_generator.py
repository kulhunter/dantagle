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
INDEX_FILE = "index.html"
BLOG_INDEX = "blog.html"

# CONTEXTO MAESTRO (Data para la IA)
CASES = [
    "Tikk.cl: E-commerce Automation", "CriptoBot: AI Trading", "Neural Eye: AI Heatmap UX", 
    "Ley Responsable: Legal SaaS", "Maps with Memory: Award-winning Tech", "Duoc UC Strategy",
    "The Factory: Agency Growth", "Obsolescencia del CM: Strategy", "Como dijo que dijo: Viral Branding",
    "FIAP 2016: Creative Marathon", "El Ojo de Iberoamérica Jury", "Flyer to SaaS Spectrum",
    "SEO AEO Optimization", "WhatsApp Sales Engine", "Real-time Finance Suite",
    "Creativepool #1 Global Ranking", "UDD Masterclass", "B2B Automation Hub", "Personal Branding V3",
    "Teve: Stream Platform Strategy"
]

DEVELOPMENTS = ["Tikk", "Saben", "LeyResponsable", "Teve", "Criptobot", "Calculadora UTM", "Validador RUT", "UF Real-time"]

# Guía de Estilo "Dan Tagle" V4.0 (High Value)
STYLE_GUIDE = f"""
Eres Dan Tagle, #1 Global Creative Technologist (Creativepool).
Tu misión es DESTROZAR la mediocridad digital y orquestar crecimiento real.
Tono: Provocativo, experto, hacker, B2B senior.
Contexto: Tienes 19 casos de éxito (ej: {", ".join(CASES[:5])}) y desarrollos como {", ".join(DEVELOPMENTS[:4])}.

REGLAS DE CONTENIDO:
1. No vendas "humo". Vende ingeniería creativa.
2. Cada artículo debe citar al menos uno de tus CASOS o DESARROLLOS como ejemplo de solución.
3. El enfoque es AEO (Answer Engine Optimization): responde preguntas que un CEO o CMO se haría en 2026.
4. Habla de retorno de inversión, automatización y destrabe de procesos.
"""

def get_trending_topics():
    topics = [
        "Por qué tu estrategia de marketing 2025 es obsoleta frente a los Agentes de IA",
        "AEO: El fin del SEO tradicional y cómo ser la respuesta única en Perplexity",
        "Orquestación Digital: De un flyer a un SaaS, el espectro total del crecimiento",
        "WhatsApp Business API: Cómo Tikk está automatizando el 90% de las ventas en Chile",
        "El costo invisible de la fricción: Cómo Neural Eye predice la fuga de usuarios",
        "Finanzas Tácticas: Por qué las empresas que no usan data en tiempo real están perdiendo contra la inflación",
        "De Creativo a Technologist: El camino para dominar el ranking global de Creativepool"
    ]
    day = datetime.datetime.now().day
    return topics[day % len(topics)]

def generate_content(topic):
    prompt = f"""
    {STYLE_GUIDE}
    
    ESCRIBE UN ARTÍCULO DE ALTO VALOR ESTRATÉGICO SOBRE: "{topic}"
    
    REQUISITOS TÉCNICOS:
    1. Título quirúrgico para SEO y CTR.
    2. Fecha: {datetime.datetime.now().strftime('%d %b %Y').upper()}
    3. Contenido: +500 palabras de valor puro.
    4. Estructura: Intro provocativa, 3 pilares tácticos, Cita a un Caso/Desarrollo real tuyo, Conclusión de impacto.
    5. DEVOLVER ÚNICAMENTE UN OBJETO JSON: 'title', 'date', 'slug', 'content_html', 'meta_description', 'image_keyword'.
    """
    
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "Eres un orquestador de crecimiento digital que responde solo en JSON."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.6
    }
    
    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    result = response.json()
    
    if 'choices' not in result:
        print(f"ERROR DE API: La respuesta no contiene 'choices'.")
        print(f"Respuesta completa: {json.dumps(result, indent=2)}")
        exit(1)
        
    raw_content = result['choices'][0]['message']['content']
    clean_json = re.sub(r'```json\s*|\s*```', '', raw_content).strip()
    return json.loads(re.search(r'\{.*\}', clean_json, re.DOTALL).group())

def create_article_page(article):
    title, description, content = article['title'], article['meta_description'], article['content_html']
    image_url = f"https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&q=80&w=1200"

    html_content = f"""<!DOCTYPE html>
<html lang="es-CL">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Dan Tagle</title>
    <meta name="description" content="{description}">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{ --accent: #06b6d4; }}
        body {{ font-family: 'Outfit', sans-serif; background-color: #050505; color: #f4f4f5; }}
        .bg-mesh {{ background-image: radial-gradient(circle at 50% 0%, rgba(6, 182, 212, 0.05) 0%, transparent 50%); }}
        article p {{ margin-bottom: 1.5rem; line-height: 1.8; color: #a1a1aa; font-weight: 300; }}
        article h2 {{ font-size: 2rem; font-weight: 900; color: #fff; margin-top: 3rem; margin-bottom: 1rem; text-transform: uppercase; letter-spacing: -0.02em; }}
        article ul {{ margin-bottom: 2rem; list-style: disc; padding-left: 1.5rem; color: #a1a1aa; }}
    </style>
</head>
<body class="bg-mesh">
    <nav class="fixed top-0 w-full z-50 py-6 px-10 flex justify-between items-center bg-black/40 backdrop-blur-2xl border-b border-white/5">
        <a href="../index.html" class="text-2xl font-black tracking-tighter uppercase">DAN TAGLE <span class="text-cyan-500">.</span></a>
        <div class="hidden lg:flex gap-14 text-[10px] font-black uppercase tracking-[0.4em] text-zinc-500">
            <a href="../casos.html" class="hover:text-white transition-colors">Casos</a>
            <a href="../desarrollos.html" class="hover:text-white transition-colors">Desarrollos</a>
            <a href="../blog.html" class="text-white transition-colors">Blog</a>
        </div>
        <a href="https://calendly.com/dan-tagle/30min" target="_blank" class="px-10 py-3 bg-white text-black font-black text-[10px] uppercase tracking-[0.2em] rounded-full">Agendar</a>
    </nav>
    <main class="pt-48 pb-20 px-6 container mx-auto max-w-3xl">
        <header class="mb-16">
            <span class="text-[10px] font-mono text-cyan-500 tracking-[0.4em] uppercase mb-4 block">PENSAMIENTO ESTRATÉGICO / {article['date']}</span>
            <h1 class="text-4xl md:text-6xl font-black mb-8 leading-tight text-white uppercase tracking-tighter">{title}</h1>
        </header>
        <article class="prose prose-invert prose-cyan max-w-none">
            {content}
        </article>
        <footer class="mt-20 pt-10 border-t border-white/5 flex justify-between items-center">
            <a href="../blog.html" class="text-xs font-black uppercase tracking-widest text-zinc-500 hover:text-white transition-colors">← Volver al Blog</a>
            <span class="text-[10px] text-zinc-700 font-bold uppercase tracking-widest">© 2026 Dan Tagle</span>
        </footer>
    </main>
</body>
</html>"""
    
    filename = f"{BLOG_DIR}{article['slug']}.html"
    with open(filename, 'w') as f: f.write(html_content)
    return filename

def update_indices(article, filename):
    img_url = f"https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&q=80&w=1200"
    new_entry = f"""
            <a href="blog/{article['slug']}.html" class="glass-panel p-6 flex flex-col group">
                <div class="rounded-[2rem] overflow-hidden aspect-video mb-8 grayscale group-hover:grayscale-0 transition-all duration-700">
                    <img src="{img_url}" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                </div>
                <span class="text-cyan-500 font-mono text-[10px] mb-3 uppercase tracking-widest">{article['date']}</span>
                <h3 class="text-2xl font-black mb-4 group-hover:text-cyan-400 transition-colors uppercase leading-tight tracking-tight">{article['title']}</h3>
                <p class="text-zinc-500 text-sm mb-8 line-clamp-3 font-light">{article['meta_description']}</p>
                <span class="mt-auto text-[9px] font-black uppercase tracking-widest text-zinc-700 group-hover:text-white transition-colors">Leer más →</span>
            </a>
            <!-- NEXT_POST_HERE -->
"""
    if os.path.exists(BLOG_INDEX):
        with open(BLOG_INDEX, 'r') as f: content = f.read()
        if '<!-- NEXT_POST_HERE -->' in content:
            with open(BLOG_INDEX, 'w') as f: f.write(content.replace('<!-- NEXT_POST_HERE -->', new_entry))

if __name__ == "__main__":
    if GROQ_API_KEY:
        topic = get_trending_topics()
        article_data = generate_content(topic)
        filepath = create_article_page(article_data)
        update_indices(article_data, filepath)
        print(f"✅ Nuevo artículo de alto valor: {article_data['title']}")
