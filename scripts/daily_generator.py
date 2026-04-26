import os
import json
import requests
import datetime
import re

# --- CONFIGURACIÓN ---
# Necesitarás una API Key de Groq (GRATIS en console.groq.com)
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
MODEL = "deepseek-r1-distill-llama-70b" # Modelo DeepSeek gratuito en Groq

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
    7. DEVOLVER ÚNICAMENTE UN OBJETO JSON con las claves: 'title', 'date', 'slug', 'content_html', 'meta_description'.
    
    El 'content_html' debe usar etiquetas <h2>, <h3>, <p>, <strong>, y <ul>.
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
    
    cover_img = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=1200"
    page_content = page_content.replace("{{COVER_IMAGE}}", cover_img)
    
    filename = f"{BLOG_DIR}{article['slug']}.html"
    with open(filename, 'w') as f:
        f.write(page_content)
    return filename

def update_indices(article, filename):
    print(f"DEBUG: Actualizando índices {BLOG_INDEX} e {INDEX_FILE}...")
    
    # Actualizar blog.html
    new_entry = f"""
            <!-- Auto-generated entry: {article['title']} -->
            <a href="{filename}" class="glass-panel p-6 flex flex-col group">
                <div class="rounded-2xl overflow-hidden aspect-video mb-6 grayscale group-hover:grayscale-0 transition-all duration-500">
                    <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=1200" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                </div>
                <span class="text-cyan-500 font-mono text-[10px] mb-2 uppercase">{article['date']}</span>
                <h3 class="text-2xl font-black mb-4 group-hover:text-cyan-400 transition-colors uppercase">{article['title']}</h3>
                <p class="text-zinc-500 text-sm mb-6 line-clamp-3">{article['meta_description']}</p>
                <span class="mt-auto text-[10px] font-black uppercase tracking-widest text-zinc-700 group-hover:text-white transition-colors">Leer más →</span>
            </a>
    """
    
    if os.path.exists(BLOG_INDEX):
        with open(BLOG_INDEX, 'r') as f:
            content = f.read()
        updated_content = content.replace('<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">', f'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">\n{new_entry}')
        with open(BLOG_INDEX, 'w') as f:
            f.write(updated_content)
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
