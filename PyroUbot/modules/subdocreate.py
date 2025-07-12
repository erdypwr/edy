import requests
import json
from pyrogram import *
from pyrogram import Client, filters
from PyroUbot import PY

__MODULE__ = "ᴄʀᴇᴀᴛᴇ ᴅᴏᴍᴀɪɴ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱᴜʙᴅᴏᴍᴀɪɴ ᴄʀᴇᴀᴛᴏʀ ᴄᴇꜱꜱ 』</b>

ᴘᴇʀɪɴᴛᴀʜ:
<code>{0}ꜱᴜʙᴅᴏᴄʀᴇᴀᴛᴇ [ᴅᴏᴍᴀɪɴ] [ꜱᴜʙᴅᴏᴍᴀɪɴ] [ɪᴘ]</code> → ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ꜱᴜʙᴅᴏᴍᴀɪɴ ᴋᴇ ᴅᴏᴍᴀɪɴ ʏᴀɴɢ ᴛᴇʀꜱᴇᴅɪᴀ ᴅɪ ᴄʟᴏᴜᴅꜰʟᴀʀᴇ.
<code>{0}ʟɪꜱᴛᴅᴏᴍᴀɪɴ </code> → ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ʟɪꜱᴛ ᴅᴏᴍᴀɪɴ.

🔍 ᴄᴏɴᴛᴏʜ:
<code>{0}ꜱᴜʙᴅᴏᴄʀᴇᴀᴛᴇ example.com test 192.168.1.1</code>

💡 ɢᴜɴᴀᴋᴀɴ <code>{0}ᴅᴏᴍᴀɪɴʟɪꜱᴛ</code> ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴀꜰᴛᴀʀ ᴅᴏᴍᴀɪɴ ʏᴀɴɢ ᴛᴇʀꜱᴇᴅɪᴀ.</blockquote></b>
"""

# Konfigurasi Cloudflare (Tambahkan daftar domain dengan Zone ID)
CLOUDFLARE_API_TOKEN = "auQMrkPsYbpFO29HwHMEVzNvkY_nLNlR3vPW6Y7Y"
DOMAIN_LIST = {
    "digitalatelier.tech": "1932711fb1d4d86b1f53b00d1b275f8a",
    "mydigital-store.me": "11c1abb8f727bf4d7342f1cade2b3cd7"
}

# Fungsi untuk menambahkan subdomain ke Cloudflare
def create_subdomain(zone_id, subdomain, target_ip):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    headers = {
        "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "type": "A",  # Bisa diubah ke "CNAME" jika ingin menggunakan CNAME
        "name": subdomain,
        "content": target_ip,
        "ttl": 1,
        "proxied": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

@PY.UBOT("subdocreate")
@PY.TOP_CMD
async def subdomain_create(client, message):
    args = message.text.split(maxsplit=3)
    if len(args) < 4:
        await message.reply_text("❌ ꜱɪʟᴀᴋᴀɴ ᴍᴀꜱᴜᴋᴋᴀɴ ꜰᴏʀᴍᴀᴛ ʏᴀɴɢ ʙᴇɴᴀʀ ᴄᴜᴋɪ: `.ꜱᴜʙᴅᴏᴄʀᴇᴀᴛᴇ [ᴅᴏᴍᴀɪɴ] [ꜱᴜʙᴅᴏᴍᴀɪɴ] [ɪᴘ]`")
        return

    domain = args[1].strip()
    subdomain = args[2].strip()
    target_ip = args[3].strip()

    if domain not in DOMAIN_LIST:
        await message.reply_text(f"❌ ᴅᴏᴍᴀɪɴ `{domain}` ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴅᴀʟᴀᴍ ᴅᴀꜰᴛᴀʀ ᴄᴜᴋɪ. ɢᴜɴᴀᴋᴀɴ `.ᴅᴏᴍᴀɪɴʟɪꜱᴛ` ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴀꜰᴛᴀʀ ᴅᴏᴍᴀɪɴ ʏᴀɴɢ ᴛᴇʀꜱᴇᴅɪᴀ.")
        return

    zone_id = DOMAIN_LIST[domain]
    full_subdomain = f"{subdomain}.{domain}"

    await message.reply_text(f"🔍 **ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ꜱᴜʙᴅᴏᴍᴀɪɴ ᴄᴇꜱꜱ:** `{full_subdomain}` ➝ `{target_ip}`")

    result = create_subdomain(zone_id, full_subdomain, target_ip)

    if result.get("success"):
        await message.reply_text(f"✅ **ꜱᴜʙᴅᴏᴍᴀɪɴ ʙᴇʀʜᴀꜱɪʟ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴄᴇꜱꜱ!**\n🌐 `{full_subdomain} → {target_ip}`")
    else:
        error_msg = result.get("errors", [{"message": "Unknown Error"}])[0]["message"]
        await message.reply_text(f"❌ **ɢᴀɢᴀʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ꜱᴜʙᴅᴏᴍᴀɪɴ**\n⚠️ ᴇʀʀᴏʀ: `{error_msg}`")

@PY.UBOT("domainlist")
@PY.TOP_CMD
async def list_domains(client, message):
    domain_list_text = "📜 **ᴅᴀꜰᴛᴀʀ ᴅᴏᴍᴀɪɴ ʏᴀɴɢ ᴛᴇʀꜱᴇᴅɪᴀ ᴄᴇꜱꜱ:**\n"
    for domain in DOMAIN_LIST.keys():
        domain_list_text += f"✅ `{domain}`\n"
    
    await message.reply_text(domain_list_text)
