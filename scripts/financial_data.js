/**
 * financial_data.js
 * Centralized fetcher for Chilean financial indicators (UF, UTM, IPC)
 */
async function getFinancialIndicators() {
    try {
        // Using mindicador.cl API (CORS friendly usually)
        const response = await fetch('https://mindicador.cl/api');
        const data = await response.json();
        return {
            uf: data.uf.valor,
            utm: data.utm.valor,
            ipc: data.ipc.valor,
            dolar: data.dolar.valor,
            retencion: 0.1525 // Current 2026 value
        };
    } catch (error) {
        console.error("Error fetching financial data:", error);
        // Fallback to static current values
        return {
            uf: 38500,
            utm: 67000,
            ipc: 4.5,
            retencion: 0.1525
        };
    }
}
