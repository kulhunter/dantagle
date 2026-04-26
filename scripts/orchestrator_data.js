const MASTER_DATA = {
    cases: [
        { id: 1, title: "Tikk.cl", category: "E-commerce Automation", description: "Infraestructura boutique para PyMEs chilenas.", link: "https://tikk.cl", tags: ["Next.js", "WhatsApp API"] },
        { id: 2, title: "CriptoBot", category: "AI Fintech", description: "Algoritmos de trading de alta frecuencia.", link: "https://criptobot.cl", tags: ["Python", "IA"] },
        { id: 3, title: "Neural Eye", category: "UX AI", description: "Diagnóstico de atención visual predictivo.", link: "dantagle-ai-eye.html", tags: ["Computer Vision"] },
        { id: 4, title: "Ley Responsable", category: "Legal SaaS", description: "Automatización de procesos legales masivos.", link: "https://leyresponsable.cl", tags: ["Automation"] },
        { id: 5, title: "Maps with Memory", category: "Award Project", description: "Proyecto premiado en Adlatina y Latinspots.", link: "https://www.latinspots.com/pieza/grafica/board-maps-with-memory/20289", tags: ["Creative Tech"] },
        { id: 6, title: "Duoc UC Strategy", category: "Education", description: "Transformación digital del viaje del consumidor.", link: "https://www.duoc.cl/eventos/el-viaje-del-consumidor-mitos-y-realidades-del-marketing-digital/", tags: ["Strategy"] },
        { id: 7, title: "Agency The Factory", category: "Growth", description: "Orquestación de procesos de agencia digital.", link: "http://agenciathefactory.blogspot.com/", tags: ["Management"] },
        { id: 8, title: "Obsolescencia CM", category: "Thought Leadership", description: "Manifiesto sobre la evolución del marketing.", link: "https://es.linkedin.com/pulse/la-obsolescencia-programada-del-cm-daniel-tagle-dennis", tags: ["Strategy"] },
        { id: 9, title: "Como dijo que dijo", category: "Viral Content", description: "Estrategia de branding y contenido masivo.", link: "http://comodijoquedijo.weebly.com/", tags: ["Branding"] },
        { id: 10, title: "FIAP 2016", category: "Award", description: "Maratón de Jóvenes Creativos.", link: "https://comunicaciones.udd.cl/noticias/2016/03/asi-se-vivio-la-maraton-de-jovenes-creativos-fiap-2016-en-la-udd/", tags: ["Creativity"] },
        { id: 11, title: "El Ojo Jury", category: "Authority", description: "Jurado en El Ojo de Iberoamérica.", link: "https://www.adlatina.com/campa%C3%B1as/maps-with-memory", tags: ["Jury"] },
        { id: 12, title: "Flyer to SaaS", category: "Full Spectrum", description: "Entrega total desde diseño a software.", link: "desarrollos.html", tags: ["Execution"] },
        { id: 13, title: "AEO Optimization", category: "SEO AI", description: "Dominación de motores de respuesta IA.", link: "blog.html", tags: ["AEO"] },
        { id: 14, title: "WhatsApp Sales", category: "Conversion", description: "Motor de ventas conversacional B2B.", link: "wa.html", tags: ["Growth"] },
        { id: 15, title: "Finance Suite", category: "Tactical Tools", description: "Herramientas de data en tiempo real.", link: "uf.html", tags: ["Fintech"] },
        { id: 16, title: "Creativepool #1", category: "Global Ranking", description: "Ranking mundial como Creative Technologist.", link: "https://creativepool.com/top-25/creative-technologists/", tags: ["Ranking"] },
        { id: 17, title: "UDD Masterclass", category: "Mentorship", description: "Formación de nuevas generaciones digitales.", link: "index.html", tags: ["Education"] },
        { id: 18, title: "B2B Hub", category: "Automation", description: "Centralización de procesos complejos.", link: "desarrollos.html", tags: ["B2B"] },
        { id: 19, title: "Personal Brand V3", category: "Identity", description: "Re-arquitectura de identidad digital 2026.", link: "index.html", tags: ["Design"] }
    ],
    developments: [
        { title: "Tikk", icon: "shopping-bag", desc: "E-commerce WhatsApp", link: "https://tikk.cl" },
        { title: "Saben", icon: "help-circle", desc: "Trivia IA Engine", link: "desarrollos.html" },
        { title: "LeyResponsable", icon: "shield", desc: "Legal Tech SaaS", link: "https://leyresponsable.cl" },
        { title: "Criptobot", icon: "zap", desc: "Fintech Algo-Trading", link: "https://criptobot.cl" },
        { title: "Calculadora UTM", icon: "calculator", desc: "Finanzas SII", link: "calculadora-utm.html" },
        { title: "Validador RUT", icon: "check-square", desc: "Utilidad Chilena", link: "rut.html" }
    ],
    diagnosis: [
        { issue: "Mis ventas están estancadas", recommendation: "Te recomiendo orquestar un motor de ventas en WhatsApp como **Tikk**." },
        { issue: "No aparezco en las respuestas de IA", recommendation: "Necesitas una estrategia de **AEO (Answer Engine Optimization)**." },
        { issue: "Mi UX es confusa", recommendation: "Usemos **Neural Eye** para diagnosticar tus focos de atención." },
        { issue: "Tengo procesos manuales lentos", recommendation: "Podemos automatizarlos con un **SaaS a medida**." }
    ]
};

function getFeaturedCases(count = 4) {
    const shuffled = [...MASTER_DATA.cases].sort(() => 0.5 - Math.random());
    return shuffled.slice(0, count);
}
