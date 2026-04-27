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
    # Keep only latest 50 to avoid bloat
    index = index[:50]
    
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=4, ensure_ascii=False)

def update_sitemap(slug):
    sitemap_path = "sitemap.xml"
    if not os.path.exists(sitemap_path):
        return
        
    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    today = datetime.now().strftime("%Y-%m-%d")
    new_url = f'  <url><loc>https://dantagle.cl/blog/{slug}.html</loc><lastmod>{today}</lastmod><priority>0.7</priority></url>\n'
    
    if f"/blog/{slug}.html" in content:
        return
        
    updated_content = content.replace("</urlset>", f"{new_url}</urlset>")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

def update_ai_configs(title, excerpt):
    # Update llms.txt (Standard for AI agents)
    llms_path = "llms.txt"
    today = datetime.now().strftime("%Y-%m-%d")
    new_entry = f"- [{today}] {title}: {excerpt}\n"
    
    mode = "a" if os.path.exists(llms_path) else "w"
    with open(llms_path, mode, encoding="utf-8") as f:
        f.write(new_entry)
        
    # Update ai-config.json
    config_path = "ai-config.json"
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
    else:
        config = {"latest_insights": []}
        
    config["latest_insights"].insert(0, {"date": today, "title": title, "insight": excerpt})
    config["latest_insights"] = config["latest_insights"][:10]
    
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

def generate_seo_article():
    if not GROQ_API_KEY:
        print("❌ Error: GROQ_API_KEY no configurada.")
        return

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = """
    Actúa como un Global Creative Technologist de élite. 
    Escribe un artículo de blog de ALTO VALOR ESTRATÉGICO sobre TENDENCIAS TECNOLÓGICAS, IA, RETAIL MEDIA o INNOVACIÓN DIGITAL.
    
    REGLAS CRÍTICAS:
    1. NO menciones marcas comerciales específicas (Ssangyong, Tenpo, etc.). Habla de INDUSTRIAS.
    2. Usa un tono directo, técnico y visionario. Cero humo.
    3. Enfócate en resolver dolores comunes de CEOs: Eficiencia operativa, visibilidad en la era de la IA, automatización de ventas.
    4. Estructura: H1 audaz, H2s técnicos, párrafos cortos.
    5. Formato: JSON con 'title', 'excerpt', 'category', 'content' (HTML) y 'slug'.
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
        
        # HTML Template (Minimalist/Impactful)
        template = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Dan Tagle</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;900&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Outfit', sans-serif; background: #050505; color: #fff; }}
        .content h2 {{ font-size: 2rem; font-weight: 900; color: #06b6d4; margin-top: 3rem; text-transform: uppercase; }}
        .content p {{ font-size: 1.2rem; line-height: 1.8; color: #a1a1aa; margin-bottom: 1.5rem; }}
    </style>
</head>
<body class="py-20 px-6">
    <div class="max-w-3xl mx-auto">
        <a href="../blog.html" class="text-zinc-500 uppercase tracking-widest text-xs border-b border-zinc-800 pb-1 hover:text-white transition-all">← Volver</a>
        <h1 class="text-6xl md:text-8xl font-black uppercase tracking-tighter leading-none my-12">{title}</h1>
        <div class="content">
            {article_data['content']}
        </div>
        <footer class="mt-20 pt-10 border-t border-white/10">
            <p class="text-zinc-500 italic">Estrategia Táctica por Dan Tagle</p>
        </footer>
    </div>
</body>
</html>"""

        filename = f"blog/{slug}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(template)
            
        # Orquestación SEO/AI
        update_blog_index({
            "title": title,
            "excerpt": excerpt,
            "slug": slug,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "category": article_data['category']
        })
        update_sitemap(slug)
        update_ai_configs(title, excerpt)
        
        print(f"✅ Orquestación exitosa: {filename}")

    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    generate_seo_article()
