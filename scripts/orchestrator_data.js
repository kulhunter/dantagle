const MASTER_DATA = {
    cases: [
        { client: "Global ERP Partner", title: "Hackeando el B2B Orgánico", prob: "Bases saturadas de SPAM y nula visibilidad en Google.", sol: "Arquitectura SEO y AEO para responder dudas técnicas exactas.", res: "10 keywords Top 1 en 3 meses.", link: "https://www.behance.net/gallery/231096043/a-b2b-creative-solution", tags: ["SEO", "AEO"] },
        { client: "SaaS Logístico", title: "Santa's Live Tracking", prob: "Vender la idea de un ERP cloud es abstracto y aburrido.", sol: "Dashboard técnico real mostrando ubicación de stock en tiempo real.", res: "Activación viral de alto impacto B2B.", link: "https://www.behance.net/gallery/240982385/Santas-Tracking-Christmas-2025-2Win", tags: ["Dashboard", "B2B"] },
        { client: "Líder Automotriz", title: "DOOH Reactivo al Clima", prob: "Publicidad estática y desconectada del contexto.", sol: "Conexión a API Weather: si llovía, la creatividad cambiaba en tiempo real.", res: "Pioneros en DOOH dinámico.", link: "https://www.behance.net/gallery/44019443/SSangyong-Actyon-Sports-ADS-realtime", tags: ["IoT", "Real-time"] },
        { client: "Institución de Salud", title: "Maps with Memory", prob: "Pacientes con Alzheimer perdidos: 48h críticas de búsqueda.", sol: "App con zonas memorables preventivas para envío inmediato de ubicación.", res: "Ahorro de 2 días en investigación policial.", link: "https://www.behance.net/gallery/79370809/Bupa-Maps-with-Memory", tags: ["App", "Health"] },
        { client: "Neobanco Fintech", title: "Ruleta BTL Data-Driven", prob: "Eventos físicos generan gasto sin captura de data real.", sol: "Ruleta física conectada a API de Google Sheets en tiempo real.", res: "Captura de leads instantánea al CRM.", link: "https://www.behance.net/gallery/217013571/BTL_-Ruleta-Tenpo", tags: ["BTL", "Data"] },
        { client: "Líder Automotriz", title: "Pincel Robótico Gigante", prob: "Demostrar maniobrabilidad extrema sin comerciales típicos.", sol: "Vehículo convertido en pincel operado por App y aire comprimido.", res: "Obra de arte visible desde el cielo.", link: "https://www.behance.net/gallery/45095931/Ssangyong-La-primera-pintura-hecha-con-un-auto", tags: ["Creative Tech"] },
        { client: "Gigante Electrodomésticos", title: "Lanzamiento Estratégico", prob: "Marca global desconocida en mercado local hipercompetitivo.", sol: "Estrategia 360º enfocada en escala y penetración digital.", res: "Effie de Oro en Lanzamiento de Marca.", link: "https://www.behance.net/gallery/20824907/MIDEA-Growth-Chile-Lanzamiento-Win-Effie", tags: ["Effie", "Growth"] },
        { client: "Parque Entretenimiento", title: "GiftCard de Tiempo", prob: "Competir contra pantallas en el Día del Niño.", sol: "Plataforma para regalar códigos canjeables por tiempo real con padres.", res: "Engagement digital derivado en visitas reales.", link: "https://www.behance.net/gallery/43592137/KidZania-La-primera-GiftCard-de-tiempo", tags: ["Platform"] },
        { client: "Logística Nacional", title: "Matchmaking Solidario", prob: "Proceso manual de apadrinamiento limitaba alcance.", sol: "Plataforma de 'matchmaking' para cartas navideñas.", res: "10.000+ cartas apadrinadas digitalmente.", link: "https://www.behance.net/gallery/139685235/CorreosChile-Navidad", tags: ["Social", "UI/UX"] },
        { client: "Líder Tecnología", title: "Storytelling Global", prob: "Traducir concepto filosófico abstracto en contenido masivo.", sol: "Campaña animada sobre hacedores vs creyentes.", res: "Materialización de eslogan global.", link: "https://www.behance.net/gallery/16671013/Make-dot-Believe-Sony", tags: ["Storytelling"] },
        { client: "Bebida Energética", title: "La Energía Ya Viene", prob: "Competir contra líderes de mercado con presupuesto limitado.", sol: "Guerrilla marketing emulando estética de campaña política.", res: "2da marca más vendida en tiempo récord.", link: "https://www.behance.net/gallery/33374017/Chile-la-energia-ya-viene-Shot-Go", tags: ["Guerrilla"] },
        { client: "Retail Regional", title: "Universo Narrativo", prob: "Lanzar colección de marca propia desde cero.", sol: "Creación de IP y universo donde los personajes hablan en rima.", res: "Fenómeno cultural de retail más grande del país.", link: "https://www.behance.net/gallery/16670095/Duendes-Cencosud", tags: ["Creative"] },
        { client: "Agencia Creativa", title: "El Niño Illuminati", prob: "Generar ruido en evento deportivo sin ser sponsor.", sol: "Newsjacking: integrar tendencia viral en 24h a la comunicación.", res: "100M+ en Earned Media.", link: "https://www.behance.net/gallery/40426917/Illuminati-child-2016-Centennial-America-Cup", tags: ["Viral"] }
    ],
    developments: [
        { title: "Saben", icon: "help-circle", desc: "Juego para fiestas y amigos familia online multijugador GRATIS.", link: "desarrollos.html" },
        { title: "Tikk", icon: "shopping-bag", desc: "Convierte un excel en una tienda online con venta por whatsapp.", link: "https://tikk.cl" },
        { title: "LeyResponsable", icon: "shield", desc: "Web que se dedica a ayudar a padres y madres separados.", link: "https://leyresponsable.cl" },
        { title: "Criptobot", icon: "zap", desc: "Señales y trading algorítmico de criptomonedas.", link: "https://criptobot.cl" },
        { title: "Teve", icon: "video", desc: "Plataforma de teve online desde ubicaciones open source.", link: "https://teve.cl" },
        { title: "Neural Eye", icon: "eye", desc: "IA Predictiva: Descubre dónde mirarán tus clientes antes de lanzar tu web.", link: "dantagle-ai-eye.html" }
    ],
    diagnosis: [
        { issue: "Ventas estancadas / Checkout complejo", recommendation: "Tu funnel tiene fricción. Implementemos **Tikk** para simplificar la compra vía WhatsApp directamente desde tu inventario." },
        { issue: "Invisibilidad en buscadores de IA", recommendation: "El SEO tradicional no basta. Necesitas arquitectura **AEO** para que ChatGPT y Perplexity recomienden tu solución." },
        { issue: "Alta tasa de rebote / Web confusa", recommendation: "Usemos **Neural Eye** para identificar qué elementos distraen a tu usuario y optimizar la conversión en 48h." },
        { issue: "Operación manual lenta y costosa", recommendation: "Digitalicemos el núcleo de tu negocio con un **SaaS a medida**, eliminando errores humanos y escalando el proceso." }
    ]
};

function getFeaturedCases(count = 4) {
    const shuffled = [...MASTER_DATA.cases].sort(() => 0.5 - Math.random());
    return shuffled.slice(0, count);
}
