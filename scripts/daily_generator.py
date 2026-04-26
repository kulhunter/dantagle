import os
import json
import requests
import datetime
import re

# --- CONFIGURACIÓN ---
# Necesitarás una API Key de Groq (GRATIS en console.groq.com)
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
MODEL = "llama-3.3-70b-specdec" # Modelo activo y potente en Groq

# Rutas de archivos
BLOG_DIR = "blog/"
INDEX_FILE = "index.html"
BLOG_INDEX = "blog.html"
TEMPLATE_FILE = "blog/template.html"

# Guía de Estilo "Dan Tagle"
STYLE_GUIDE = """
Eres Dan Tagle, un Creative Technologist y Problem Solver experto en SEO IA y Automatización B2B.
Tu tono es:
- Provocativo y directo (ej: "El CM murió", "Unfuck your business").
- Sin filtros, profesional pero con una actitud "hacker".
- Enfocado en resultados de negocio y destrabe de procesos.
- Usas español de Chile/LatAm (evita modismos excesivos, mantén la elegancia profesional).
- Estructura: Subtítulos potentes, frases cortas, negritas estratégicas.
- Visión: La tecnología es un medio para el impacto humano y de negocio.
"""

def get_trending_topics():
    # Simulación de búsqueda de tendencias (puedes expandir esto con RSS)
    # Por ahora, usaremos una lista de temas calientes en 2026
    topics = [
        "El impacto de los Agentes de IA en la atención al cliente B2B",
        "AEO: Cómo optimizar tu marca para ser la respuesta número 1 en ChatGPT",
        "Automatización de ventas con WhatsApp y Google Sheets en 2026",
        "El fin de las landing pages tradicionales ante la compra conversacional",
        "SEO Zero-Click: Cómo ganar visibilidad cuando Google ya no envía tráfico",
        "IA Generativa en el BTL físico: De la activación a la captura de data real",
        "Por qué tu estrategia de marketing de 2024 te está haciendo perder dinero hoy"
    ]
    # Elegimos uno basado en el día del mes para que sea "diario"
    day = datetime.datetime.now().day
    return topics[day % len(topics)]

def generate_content(topic):
    prompt = f"""
    {STYLE_GUIDE}
    
    ESCRIBE UN ARTÍCULO DE BLOG SOBRE: "{topic}"
    
    REQUISITOS:
    1. Título impactante y clickbaiter profesional.
    2. Fecha: {datetime.datetime.now().strftime('%d %b %Y').upper()}
    3. Contenido: Mínimo 400 palabras.
    4. Incluye una sección de "Datos Clave" o "Estrategia Táctica".
    5. Termina con una reflexión potente.
    6. No uses muletillas de IA.
    7. DEVOLVER ÚNICAMENTE UN OBJETO JSON con las claves: 'title', 'date', 'slug', 'content_html', 'meta_description', 'image_keyword'.
    
    El 'content_html' debe usar etiquetas <h2>, <h3>, <p>, <strong>, y <ul>.
    El 'image_keyword' debe ser un término en inglés para buscar una imagen técnica/profesional relacionada (ej: 'artificial intelligence', 'data center', 'creative technology').
    """
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "Eres un experto en marketing y tecnología que responde exclusivamente en formato JSON."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }
    
    print(f"DEBUG: Llamando a la API de Groq con el modelo {MODEL}...")
    try:
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
    except Exception as e:
        print(f"ERROR CRÍTICO en la llamada a la API: {str(e)}")
        if 'response' in locals():
            print(f"Respuesta de la API: {response.text}")
        exit(1)
        
    if 'error' in result:
        print(f"Error devuelto por la API: {result['error']}")
        exit(1)
        
    raw_content = result['choices'][0]['message']['content']
    print(f"DEBUG: Respuesta recibida (primeros 100 caracteres): {raw_content[:100]}...")
    
    # Limpiar posibles bloques de código markdown (```json ... ```)
    clean_json = re.sub(r'```json\s*|\s*```', '', raw_content).strip()
    
    # Extraer solo el contenido entre llaves
    try:
        match = re.search(r'\{.*\}', clean_json, re.DOTALL)
        if match:
            return json.loads(match.group())
        else:
            return json.loads(clean_json)
    except Exception as e:
        print(f"ERROR de parseo JSON: {str(e)}")
        print(f"Contenido crudo que falló: {raw_content}")
        exit(1)

def create_article_page(article):
    print(f"DEBUG: Creando página para '{article['title']}'...")
    if not os.path.exists(TEMPLATE_FILE):
        print(f"ERROR: No se encuentra el template en {TEMPLATE_FILE}")
        exit(1)
        
    with open(TEMPLATE_FILE, 'r') as f:
        template = f.read()
    
    page_content = template.replace("{{TITLE}}", article['title'])
    page_content = page_content.replace("{{DATE}}", article['date'])
    page_content = page_content.replace("{{DESCRIPTION}}", article['meta_description'])
    page_content = page_content.replace("{{CONTENT}}", article['content_html'])
    
    keyword = article.get('image_keyword', 'technology')
    cover_img = f"https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=1200&sig={article['slug']}"
    # Si queremos algo más dinámico basado en el keyword:
    cover_img = f"https://source.unsplash.com/featured/1200x675?{keyword.replace(' ', ',')}"
    title = article['title']
    description = article['meta_description']
    content = article['content_html']
    image_url = "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&q=80&w=1200"

    html_content = f"""<!DOCTYPE html>
<html lang="es-CL">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Dan Tagle Blog</title>
    <meta name="description" content="{description}">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;900&display=swap" rel="stylesheet">
    
    <!-- AEO: Article Schema -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{title}",
      "description": "{description}",
      "image": "{image_url}",
      "author": {{
        "@type": "Person",
        "name": "Dan Tagle",
        "url": "https://dantagle.cl"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "Dan Tagle",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://dantagle.cl/creativepool.png"
        }}
      }},
      "datePublished": "{datetime.datetime.now().strftime('%Y-%m-%d')}"
    }}
    </script>

    <style>
        :root {{ --accent: #06b6d4; }}
        body {{ font-family: 'Outfit', sans-serif; background-color: #050505; color: #f4f4f5; }}
        .bg-mesh {{ background: radial-gradient(circle at 50% 0%, rgba(6, 182, 212, 0.05) 0%, transparent 50%); }}
        .glass-panel {{ background: rgba(255,255,255,0.03); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.08); border-radius: 2.5rem; }}
        article p {{ margin-bottom: 1.5rem; line-height: 1.8; color: #a1a1aa; font-weight: 300; }}
        article h2 {{ font-size: 2rem; font-weight: 900; color: #fff; margin-top: 3rem; margin-bottom: 1rem; text-transform: uppercase; letter-spacing: -0.02em; }}
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
            <span class="text-[10px] font-mono text-cyan-500 tracking-[0.4em] uppercase mb-4 block">PENSAMIENTO ESTRATÉGICO / {datetime.datetime.now().strftime('%d %b %Y')}</span>
            <h1 class="text-4xl md:text-6xl font-black mb-8 leading-tight text-white uppercase tracking-tighter">{title}</h1>
            <div class="rounded-[2.5rem] overflow-hidden aspect-video mb-12 grayscale hover:grayscale-0 transition-all duration-700 border border-white/10">
                <img src="{image_url}" class="w-full h-full object-cover">
            </div>
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
    with open(filename, 'w') as f:
        f.write(html_content)
    return filename

def update_indices(article, filename):
    print(f"DEBUG: Actualizando índices {BLOG_INDEX} e {INDEX_FILE}...")
    
    # Actualizar blog.html
    img_url = f"https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&q=80&w=1200"
    
    new_entry = f"""
            <a href="blog/{article['slug']}.html" class="glass-panel p-6 flex flex-col group">
                <div class="rounded-[2rem] overflow-hidden aspect-video mb-8 grayscale group-hover:grayscale-0 transition-all duration-700">
                    <img src="{img_url}" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                </div>
                <span class="text-cyan-500 font-mono text-[10px] mb-3 uppercase tracking-widest">{datetime.datetime.now().strftime('%d %b %Y')}</span>
                <h3 class="text-2xl font-black mb-4 group-hover:text-cyan-400 transition-colors uppercase leading-tight tracking-tight">{article['title']}</h3>
                <p class="text-zinc-500 text-sm mb-8 line-clamp-3 font-light">{article['meta_description']}</p>
                <span class="mt-auto text-[9px] font-black uppercase tracking-widest text-zinc-700 group-hover:text-white transition-colors">Leer más →</span>
            </a>
            <!-- NEXT_POST_HERE -->
"""
    
    if os.path.exists(BLOG_INDEX):
        with open(BLOG_INDEX, 'r') as f:
            content = f.read()
        if '<!-- NEXT_POST_HERE -->' in content:
            updated_content = content.replace('<!-- NEXT_POST_HERE -->', new_entry)
            with open(BLOG_INDEX, 'w') as f:
                f.write(updated_content)
        else:
            print(f"WARNING: No se encontró el marcador <!-- NEXT_POST_HERE --> en {BLOG_INDEX}")
    else:
        print(f"WARNING: No se encontró {BLOG_INDEX}")

    # Actualizar index.html
    new_home_entry = f"""
                <a href="{filename}" class="glass-panel p-6 group reveal">
                    <div class="rounded-2xl overflow-hidden aspect-video mb-6 grayscale group-hover:grayscale-0 transition-all duration-500">
                        <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=1200" class="w-full h-full object-cover">
                    </div>
                    <h3 class="text-xl font-bold mb-4 group-hover:text-cyan-400 transition-colors uppercase">{article['title']}</h3>
                    <p class="text-zinc-500 text-xs mb-4 line-clamp-2">{article['meta_description']}</p>
                    <span class="text-[10px] font-black uppercase tracking-widest text-zinc-700 group-hover:text-white transition-colors">Leer más</span>
                </a>
    """
    
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, 'r') as f:
            home_content = f.read()
        if '<!-- NEXT_POST_HERE -->' in home_content:
            home_updated = home_content.replace('<!-- NEXT_POST_HERE -->', new_home_entry)
            with open(INDEX_FILE, 'w') as f:
                f.write(home_updated)
        else:
            # Fallback a la grid si no hay marcador
            home_updated = home_content.replace('<div class="grid grid-cols-1 md:grid-cols-3 gap-8">', f'<div class="grid grid-cols-1 md:grid-cols-3 gap-8">\n{new_home_entry}')
            with open(INDEX_FILE, 'w') as f:
                f.write(home_updated)
    else:
        print(f"WARNING: No se encontró {INDEX_FILE}")

if __name__ == "__main__":
    if not GROQ_API_KEY:
        print("ERROR: Define GROQ_API_KEY en el entorno.")
        exit(1)
        
    print("> Investigando tendencia...")
    topic = get_trending_topics()
    
    print(f"> Generando artículo sobre: {topic}...")
    article_data = generate_content(topic)
    
    print("> Creando archivo HTML...")
    filepath = create_article_page(article_data)
    
    print("> Actualizando índices...")
    update_indices(article_data, filepath.replace(BLOG_DIR, 'blog/'))
    
    print(f"✅ ¡Éxito! Nuevo artículo: {article_data['title']}")
