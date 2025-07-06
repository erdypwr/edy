from pyrogram import Client, filters
from PyroUbot import PY
from PyroUbot import *

__MODULE__ = "ᴄʀᴇᴀᴛᴇ ʙᴏᴛ"
__HELP__ = """
<blockquote><b>Bantuan Untuk Auto Create Bot Cess</b>

Perintah: <code>{0}createbot</code> [nama_bot username_bot]
Penjelasan: Membuat Bot Telegram Baru Secara Otomatis Melalui @BotFather Cess</blockquote></b>
"""

@PY.UBOT("createbot")
@PY.TOP_CMD
async def create_bot_command(client, message):
    # Ambil argumen dari pesan
    args = message.text.split(maxsplit=2)

    if len(args) < 3:
        await message.reply_text(
            "<blockquote><b>⚠️ Gunakan format Cess: createbot [nama_bot] [username_bot]</b></blockquote>\n"
            "Contoh Cess: <code>.createbot MyNewBot MyNew_Bot</code>"
        )
        return

    bot_name = args[1]
    bot_username = args[2]

    if not bot_username.endswith("Bot"):
        await message.reply_text("❌ **Username Bot Harus Diakhiri Dengan 'Bot' Cess.**")
        return

    try:
        botfather = "@BotFather"
        
        # Kirim perintah ke BotFather
        await client.send_message(botfather, "/newbot")
        await asyncio.sleep(2)
        await client.send_message(botfather, bot_name)
        await asyncio.sleep(2)
        await client.send_message(botfather, bot_username)

        await message.reply_text(
            f"<blockquote><b>✅ **Permintaan Pembuatan Bot Telah Dikirim Ke @BotFather Cess!**\n"
            f"🆕 **Nama Bot:** `{bot_name}`\n"
            f"🔗 **Username:** @{bot_username}\n\n"
            "Silakan Cek @BotFather Untuk Melanjutkan Proses Konfigurasi Cess.</blockquote></b>"
        )
    
    except Exception as e:
        await message.reply_text(f"⚠️ Terjadi kesalahan Cess: {str(e)}")