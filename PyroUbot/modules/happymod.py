from pyrogram import Client, filters
import requests
from PyroUbot import *

__MODULE__ = "ʜᴀᴘᴘʏᴍᴏᴅ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʜᴀᴘᴘʏᴍᴏᴅ ᴄᴇꜱꜱ ⦫</b>

<blockquote><b>⎆ perintah :
ᚗ <code>{0}hmod</code> nama apk
⊷ search apk mod android</b></blockquote>
"""

@PY.UBOT("hmod")
async def _(client, message):
    args = message.text.split(" ", 1)

    if len(args) < 2:
        await message.reply_text("❌ Harap Gunakan Format:\n`.hmod Nama Game <nama_aplikasi>` Cess", quote=True)
        return

    query = args[1]
    api_url = f"https://api.botcahx.eu.org/api/search/happymod?query={query}&apikey=045705b1"

    try:
        response = requests.get(api_url)
        data = response.json()

        if not data.get("status") or "result" not in data:
            await message.reply_text("⚠️ Tidak Ditemukan Hasil Untuk Pencarian Ini Cess.", quote=True)
            return

        results = data["result"][:5]
        response_text = "🔍 **Hasil Pencarian HappyMod Cess:**\n\n"

        for item in results:
            title = item["title"]
            icon = item["icon"]
            rating = item["rating"]
            link = item["link"]

            response_text += (
                f"""
**__📌 {title}
⭐ Rating: {rating}
🔗 [Unduh di HappyMod]({link})__**"""
            )

        await message.reply_text(response_text, disable_web_page_preview=True, quote=True)
    except Exception as e:
        await message.reply_text(f"❌ Terjadi Kesalahan Cess:\n`{str(e)}`", quote=True)
