import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_seo_article():
    if not GROQ_API_KEY:
        print("❌ Error: GROQ_API_KEY no configurada.")
        return

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    # PROMPT ESTRATÉGICO: Pensamiento Neil Patel + Innovación Tech
    prompt = """
    Actúa como un Global Creative Technologist de élite. 
    Escribe un artículo de blog de ALTO VALOR ESTRATÉGICO (Neil Patel Style) sobre TENDENCIAS TECNOLÓGICAS, IA, RETAIL MEDIA o INNOVACIÓN DIGITAL.
    
    REGLAS CRÍTICAS:
    1. NO hables de los casos de Dan Tagle como tema principal. Habla del FUTURO y de cómo las empresas deben adaptarse hoy.
    2. Usa un tono provocador, profesional y visionario.
    3. Enfócate en conceptos como: IA Generativa, Automatización B2B, El fin de las cookies, Retail Media, E-commerce conversacional.
    4. Estructura SEO Perfecta: H1 potente, H2s estratégicos, párrafos cortos y directos.
    5. Idioma: Español.
    6. Formato: JSON con 'title', 'excerpt', 'category', 'content' (HTML) y 'slug'.
    
    El objetivo es que un CEO o Gerente de Marketing lo lea y piense: "Este tipo entiende hacia dónde va el mundo".
    """

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "response_format": {"type": "json_object"}
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        
        if 'choices' not in result:
            print(f"❌ Error de API: {result}")
            return

        article_data = json.loads(result['choices'][0]['message']['content'])
        
        # Validar campos
        title = article_data.get('title', 'Tendencia Tecnológica 2026')
        excerpt = article_data.get('excerpt', 'Descubre el futuro de la innovación.')
        category = article_data.get('category', 'Tecnología')
        content_html = article_data.get('content', '<p>Contenido en desarrollo.</p>')
        slug = article_data.get('slug', f"tendencia-{datetime.now().strftime('%Y%m%d')}")

        # Template HTML con diseño Prolam
        template = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Dan Tagle Blog</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;900&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Outfit', sans-serif; background: #050505; color: #fff; }}
        .article-content h2 {{ font-size: 2.5rem; font-weight: 900; margin-top: 3rem; margin-bottom: 1.5rem; color: #06b6d4; text-transform: uppercase; letter-spacing: -0.02em; }}
        .article-content p {{ font-size: 1.25rem; line-height: 1.8; color: #a1a1aa; margin-bottom: 2rem; font-weight: 300; }}
        .hero-glow {{ background: radial-gradient(circle at 50% 50%, rgba(6, 182, 212, 0.15) 0%, transparent 70%); }}
    </style>
</head>
<body class="py-20 px-6">
    <nav class="max-w-4xl mx-auto mb-20 flex justify-between items-center">
        <a href="../index.html" class="font-black text-xl tracking-tighter">DAN TAGLE <span class="text-cyan-500">.</span></a>
        <a href="../blog.html" class="text-xs font-black uppercase tracking-widest border-b border-white pb-1">Volver al Blog</a>
    </nav>

    <article class="max-w-4xl mx-auto hero-glow p-10 rounded-[3rem]">
        <span class="text-cyan-500 font-mono text-sm tracking-[0.4em] uppercase mb-8 block">// {category}</span>
        <h1 class="text-6xl md:text-8xl font-black uppercase tracking-tighter leading-none mb-12">{title}</h1>
        <p class="text-2xl text-white font-light italic mb-16 leading-relaxed border-l-4 border-cyan-500 pl-8">{excerpt}</p>
        
        <div class="article-content">
            {content_html}
        </div>
        
        <footer class="mt-32 pt-20 border-t border-white/10">
            <h3 class="text-4xl font-black uppercase mb-8">¿Listo para el futuro?</h3>
            <p class="text-zinc-500 mb-12">Hablemos sobre cómo implementar estas tendencias en tu negocio hoy.</p>
            <a href="https://wa.me/56930219665" class="inline-block bg-white text-black px-12 py-5 rounded-full font-black uppercase tracking-widest hover:bg-cyan-500 transition-all">Consultoría Táctica</a>
        </footer>
    </article>
</body>
</html>"""

        filename = f"blog/{slug}.html"
        os.makedirs("blog", exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(template)
        
        print(f"✅ Artículo de VALOR creado: {filename}")

    except Exception as e:
        print(f"❌ Error crítico: {str(e)}")

if __name__ == "__main__":
    generate_seo_article()
