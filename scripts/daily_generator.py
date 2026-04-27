import os
import requests
import json
import re
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def update_blog_index(new_post):
    index_path = "blog/blog_index.json"
    os.makedirs("blog", exist_ok=True)
    
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            index = json.load(f)
    else:
        index = []
    
    index.insert(0, new_post)
    index = index[:50]
    
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=4, ensure_ascii=False)

def update_sitemap(slug):
    sitemap_path = "sitemap.xml"
    if not os.path.exists(sitemap_path): return
    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()
    today = datetime.now().strftime("%Y-%m-%d")
    new_url = f'  <url><loc>https://dantagle.cl/blog/{slug}.html</loc><lastmod>{today}</lastmod><priority>0.7</priority></url>\n'
    if f"/blog/{slug}.html" in content: return
    updated_content = content.replace("</urlset>", f"{new_url}</urlset>")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

def generate_seo_article():
    if not GROQ_API_KEY:
        print("❌ Error: GROQ_API_KEY no configurada.")
        return

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    # PROMPT DE ELITE: Storytelling + Estrategia + Conversión
    prompt = """
    Actúa como un Global Creative Technologist de élite. 
    Escribe un artículo de blog sobre TENDENCIAS TECNOLÓGICAS (IA, Retail Media, E-commerce, Automatización).
    
    REGLAS DE ORO DE COPYWRITING:
    1. TONO: Provocador, inteligente, minimalista. Piensa en una mezcla entre Wired y una consultora boutique de Londres.
    2. ESTRUCTURA: 
       - Un 'Hook' inicial potente que rompa el status quo.
       - Desarrollo lógico-creativo: Por qué esto importa HOY para un CEO.
       - 'Call to Action' integrado: Menciona cómo la tecnología (sin marcas) resuelve este problema.
    3. SEO: Usa palabras clave semánticas. Crea un título que genere curiosidad (Click-worthy).
    4. INTERLINKING: Referencia sutilmente que para implementar esto se requiere infraestructura táctica (Suite Pro) o una trayectoria probada.
    5. IDIOMA: Español de negocios (neutro/profesional).
    
    Formato: JSON con 'title', 'excerpt', 'category', 'content' (HTML), 'slug' y 'meta_desc'.
    """

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "response_format": {"type": "json_object"}
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        article_data = json.loads(result['choices'][0]['message']['content'])
        
        title = article_data['title']
        slug = article_data['slug']
        excerpt = article_data['excerpt']
        meta_desc = article_data.get('meta_desc', excerpt)

        # HTML Template (Integrated with Site Navigation and Footer)
        template = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Dan Tagle</title>
    <meta name="description" content="{meta_desc}">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@0.473.0/dist/umd/lucide.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;900&display=swap" rel="stylesheet">
    <style>
        :root {{ --accent: #06b6d4; --bg: #050505; }}
        body {{ font-family: 'Outfit', sans-serif; background: var(--bg); color: #fff; overflow-x: hidden; }}
        .glass-nav {{ background: rgba(5, 5, 5, 0.85); backdrop-filter: blur(20px); border-bottom: 1px solid rgba(255,255,255,0.08); }}
        .article-body h2 {{ font-size: 2.5rem; font-weight: 900; color: var(--accent); margin-top: 4rem; margin-bottom: 1.5rem; text-transform: uppercase; letter-spacing: -0.02em; }}
        .article-body p {{ font-size: 1.3rem; line-height: 1.8; color: #a1a1aa; margin-bottom: 2rem; font-weight: 300; }}
        .article-body strong {{ color: #fff; font-weight: 700; }}
    </style>
</head>
<body class="bg-mesh">
    <!-- Sticky Navigation -->
    <nav class="fixed top-0 w-full z-[100] glass-nav py-6 px-6 md:px-12 flex justify-between items-center">
        <a href="../index.html" class="text-2xl font-black tracking-tighter uppercase">DAN TAGLE <span class="text-cyan-500">.</span></a>
        <div class="hidden lg:flex gap-10 text-[10px] font-black uppercase tracking-[0.3em] text-zinc-500">
            <a href="../casos.html" class="hover:text-white transition-all">Trayectoria</a>
            <a href="../desarrollos.html" class="hover:text-white transition-all">Suite Pro</a>
            <a href="../blog.html" class="text-white">Tendencias</a>
        </div>
        <a href="https://wa.me/56930219665" class="hidden lg:block text-[10px] font-black uppercase tracking-widest bg-white text-black px-8 py-3 rounded-md hover:bg-cyan-500 transition-all">Consultoría</a>
    </nav>

    <main class="pt-48 pb-20 px-6 md:px-20 container mx-auto max-w-4xl">
        <span class="text-cyan-500 font-mono text-sm tracking-[0.4em] uppercase mb-8 block">// {article_data['category']}</span>
        <h1 class="text-6xl md:text-8xl font-black uppercase tracking-tighter leading-[0.9] mb-16">{title}</h1>
        
        <div class="article-body">
            {article_data['content']}
        </div>

        <div class="mt-20 p-12 bg-zinc-900/40 rounded-[3rem] border border-white/5 text-center">
            <h3 class="text-3xl font-black uppercase mb-6">¿Tu infraestructura está lista?</h3>
            <p class="text-zinc-400 mb-10">Implementamos estas tendencias con ingeniería táctica de alto impacto.</p>
            <a href="../desarrollos.html" class="inline-block bg-cyan-500 text-black px-12 py-5 rounded-full font-black uppercase tracking-widest hover:bg-white transition-all">Explorar Suite Pro</a>
        </div>
    </main>

    <!-- Footer -->
    <footer class="py-40 px-6 md:px-20 border-t border-white/10">
        <div class="container mx-auto text-center">
            <span class="text-4xl font-black uppercase tracking-tighter block mb-10">DAN TAGLE <span class="text-cyan-500">.</span></span>
            <p class="text-zinc-500 text-lg max-w-2xl mx-auto mb-12">Consultoría estratégica y desarrollo de software centrado en resultados de negocio.</p>
            <div class="flex justify-center gap-10">
                <a href="https://www.linkedin.com/in/taglecl/" class="text-zinc-600 hover:text-white transition-colors"><i data-lucide="linkedin" class="w-8 h-8"></i></a>
                <a href="https://github.com/kulhunter" class="text-zinc-600 hover:text-white transition-colors"><i data-lucide="github" class="w-8 h-8"></i></a>
            </div>
        </div>
    </footer>

    <script>lucide.createIcons();</script>
</body>
</html>"""

        filename = f"blog/{slug}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(template)
            
        update_blog_index({
            "title": title, "excerpt": excerpt, "slug": slug,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "category": article_data['category']
        })
        update_sitemap(slug)
        print(f"✅ Artículo Conectado Creado: {filename}")

    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    generate_seo_article()
