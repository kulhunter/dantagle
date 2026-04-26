const MASTER_DATA = {
    cases: [
        { client: "Oracle NetSuite Partner", title: "Hackeando el B2B Orgánico", prob: "Bases saturadas de SPAM y nula visibilidad en Google.", sol: "Arquitectura SEO y AEO para responder dudas técnicas exactas.", res: "10 keywords Top 1 en 3 meses.", link: "https://www.behance.net/gallery/231096043/a-b2b-creative-solution", tags: ["SEO", "AEO"] },
        { client: "2Win", title: "Santa's Live Tracking", prob: "Vender la idea de un ERP cloud es abstracto y aburrido.", sol: "Dashboard técnico real mostrando ubicación de stock de Santa.", res: "Activación viral de alto impacto B2B.", link: "https://www.behance.net/gallery/240982385/Santas-Tracking-Christmas-2025-2Win", tags: ["Dashboard", "B2B"] },
        { client: "Ssangyong", title: "DOOH Reactivo al Clima", prob: "Publicidad automotriz estática y desconectada del contexto.", sol: "Conexión a API Weather: si llovía, el auto se cubría de barro.", res: "Pioneros en DOOH dinámico en Chile.", link: "https://www.behance.net/gallery/44019443/SSangyong-Actyon-Sports-ADS-realtime", tags: ["IoT", "Real-time"] },
        { client: "Bupa", title: "Maps with Memory", prob: "Pacientes con Alzheimer perdidos: 48h críticas de búsqueda.", sol: "App con zonas memorables preventivas para envío inmediato.", res: "Ahorro de 2 días en investigación policial.", link: "https://www.behance.net/gallery/79370809/Bupa-Maps-with-Memory", tags: ["App", "Health"] },
        { client: "Tenpo", title: "Ruleta BTL Data-Driven", prob: "Eventos BTL generan gasto sin captura de data real.", sol: "Ruleta física conectada a API de Google Sheets en tiempo real.", res: "Captura de leads instantánea al CRM.", link: "https://www.behance.net/gallery/217013571/BTL_-Ruleta-Tenpo", tags: ["BTL", "Data"] },
        { client: "Ssangyong", title: "Pincel Robótico Gigante", prob: "Demostrar maniobrabilidad extrema sin comerciales típicos.", sol: "Auto convertido en pincel operado por App y aire comprimido.", res: "Obra de arte visible desde el cielo.", link: "https://www.behance.net/gallery/45095931/Ssangyong-La-primera-pintura-hecha-con-un-auto", tags: ["Creative Tech"] },
        { client: "MIDEA", title: "Lanzamiento MIDEA Chile", prob: "Marca asiática desconocida en mercado hipercompetitivo.", sol: "Estrategia 360º enfocada en escala global y penetración.", res: "Effie de Oro en Lanzamiento de Marca.", link: "https://www.behance.net/gallery/20824907/MIDEA-Growth-Chile-Lanzamiento-Win-Effie", tags: ["Effie", "Growth"] },
        { client: "KidZania", title: "GiftCard de Tiempo", prob: "Competir contra consolas en el Día del Niño.", sol: "Plataforma para regalar códigos canjeables por tiempo con padres.", res: "Engagement digital derivado en visitas reales.", link: "https://www.behance.net/gallery/43592137/KidZania-La-primera-GiftCard-de-tiempo", tags: ["Platform"] },
        { client: "CorreosChile", title: "Logística Solidaria", prob: "Proceso manual de apadrinamiento limitaba alcance.", sol: "Plataforma de matchmaking 'Tinder' de cartas navideñas.", res: "10.000+ cartas apadrinadas digitalmente.", link: "https://www.behance.net/gallery/139685235/CorreosChile-Navidad", tags: ["Social", "UI/UX"] },
        { client: "Sony", title: "Make.Believe Storytelling", prob: "Traducir concepto filosófico abstracto en contenido.", sol: "Campaña animada sobre hacedores vs creyentes.", res: "Materialización de eslogan global.", link: "https://www.behance.net/gallery/16671013/Make-dot-Believe-Sony", tags: ["Storytelling"] },
        { client: "Shot&Go", title: "La Energía Ya Viene", prob: "Competir contra RedBull con presupuesto limitado.", sol: "Guerrilla marketing emulando estética política presidencial.", res: "2da energética más vendida en Chile.", link: "https://www.behance.net/gallery/33374017/Chile-la-energia-ya-viene-Shot-Go", tags: ["Guerrilla"] },
        { client: "Cencosud", title: "Duendes Mágicos", prob: "Lanzar colección de peluches desde cero.", sol: "Universo narrativo donde personajes solo hablan en rima.", res: "Fenómeno cultural de retail más grande de Chile.", link: "https://www.behance.net/gallery/16670095/Duendes-Cencosud", tags: ["Creative"] },
        { client: "Why Agency", title: "El Niño Illuminati", prob: "Generar ruido en Copa América sin ser sponsor.", sol: "Newsjacking: integrar niño viral en 24h a la comunicación.", res: "100M+ CLP en Earned Media.", link: "https://www.behance.net/gallery/40426917/Illuminati-child-2016-Centennial-America-Cup", tags: ["Viral"] },
        { client: "Sony", title: "La Luna es Chilena", prob: "Apalancar hito histórico nacional extravagante.", sol: "Plataforma para certificados digitales de propiedad lunar.", res: "Hito digital viral nacional.", link: "https://www.behance.net/gallery/17818129/The-moon-is-Chilean-Sony", tags: ["Viral"] },
        { client: "Enjoy", title: "Prende Tu Verano", prob: "Aumentar público joven en casinos en verano.", sol: "Campaña buscando candidato para viajar pagado asistiendo a fiestas.", res: "Aumento masivo de afluencia joven.", link: "https://www.behance.net/gallery/33561767/Enjoy-Prende-Tu-verano-2016", tags: ["Experience"] },
        { client: "Ssangyong", title: "Auto Familiar de Madera", prob: "Las marcas de autos no le hablan a los niños.", sol: "Pickup de madera tamaño real como plaza de juegos.", res: "Insight familiar medido físicamente.", link: "https://www.behance.net/gallery/43610699/SSangyong-Car-4-children", tags: ["BTL"] },
        { client: "Ilko", title: "Recetas en Cueca", prob: "Destacar en saturación de contenido en Fiestas Patrias.", sol: "Recetas musicalizadas con métrica de Cueca.", res: "Reinvención de contenido gastronómico.", link: "https://www.behance.net/gallery/33145231/Chilean-recipes-in-Cueca-version", tags: ["Content"] },
        { client: "Int. Bipolar Foundation", title: "Alquimia Visual Bipolar", prob: "Explicar dualidad del trastorno en medio estático.", sol: "Gráfica reversible 180º que cambia el mensaje de amor a odio.", res: "Impacto emocional analógico.", link: "https://www.behance.net/gallery/45604075/International-Bipolar-Foundation-The-bipolar-Ad", tags: ["Print"] },
        { client: "Sexshop Chile", title: "La Ilusión de los 2 Métodos", prob: "Promocionar condones evadiendo censura.", sol: "Espacio negativo que sugiere masturbación sin mostrarla.", res: "Oro en WINA Festival (Print).", link: "https://www.behance.net/gallery/48577569/SEXSHOPCHILE-TWO-METHODS", tags: ["Award"] }
    ],
    developments: [
        { title: "Tikk", icon: "shopping-bag", desc: "Vende por WhatsApp: Tu tienda completa operando en un chat.", link: "https://tikk.cl" },
        { title: "Neural Eye", icon: "eye", desc: "IA que predice dónde mirarán tus clientes antes de lanzar tu web.", link: "dantagle-ai-eye.html" },
        { title: "Saben", icon: "help-circle", desc: "Trivia IA para marcas: Gamificación que genera leads reales.", link: "desarrollos.html" },
        { title: "LeyResponsable", icon: "shield", desc: "Legal Tech: Trámites legales automatizados sin burocracia.", link: "https://leyresponsable.cl" },
        { title: "Criptobot", icon: "zap", desc: "Trading Algorítmico: Señales técnicas automáticas de alta frecuencia.", link: "https://criptobot.cl" },
        { title: "Teve", icon: "video", desc: "Plataforma Streaming: Tu propio canal de video profesional.", link: "desarrollos.html" }
    ],
    diagnosis: [
        { issue: "Mis ventas están estancadas", recommendation: "Necesitas automatizar la conversión. Con **Tikk** puedes cerrar ventas directamente en WhatsApp." },
        { issue: "No aparezco en las respuestas de IA", recommendation: "Tu sitio necesita arquitectura **AEO**. Mira el caso de **Oracle NetSuite** para ver cómo lo logramos." },
        { issue: "Pierdo usuarios en mi web", recommendation: "Usemos **Neural Eye** para ver qué están ignorando tus clientes en tiempo real." },
        { issue: "Procesos manuales lentos", recommendation: "Podemos crear un **SaaS a medida** como lo hicimos con **CorreosChile** y su plataforma navideña." }
    ]
};

function getFeaturedCases(count = 4) {
    const shuffled = [...MASTER_DATA.cases].sort(() => 0.5 - Math.random());
    return shuffled.slice(0, count);
}
