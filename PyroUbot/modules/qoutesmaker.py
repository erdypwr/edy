__MODULE__ = "ǫᴜᴏᴛᴇꜱᴍᴀᴋᴇʀ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴠɪᴅᴇᴏ ǫᴜᴏᴛᴇꜱ ɢᴇɴᴇʀᴀᴛᴏʀ ᴄᴇꜱꜱ 』</b>

<b>ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ǫᴜᴏᴛᴇꜱ</code> [ᴜʀʟ_ᴠɪᴅᴇᴏ] [ᴋᴀᴛᴀ_ᴋᴀᴛᴀ]
<b>ꜰᴜɴɢꜱɪ:</b> ᴍᴇᴍʙᴜᴀᴛ ᴠɪᴅᴇᴏ ǫᴜᴏᴛᴇꜱ ᴅᴇɴɢᴀɴ ᴛᴇᴋꜱ ᴋᴜꜱᴛᴏᴍ.

<b>ᴄᴏɴᴛᴏʜ:</b> 
• <code>{0}ǫᴜᴏᴛᴇꜱ https://example.com/video.mp4 ʜɪᴅᴜᴘ ɪɴɪ ɪɴᴅᴀʜ, ɴɪᴋᴍᴀᴛɪ ꜱᴇᴛɪᴀᴘ ᴍᴏᴍᴇɴɴʏᴀ</code>
• <code>{0}ǫᴜᴏᴛᴇꜱ ɪᴍᴘɪᴀɴ ᴛɪᴅᴀᴋ ᴀᴋᴀɴ ᴛᴇʀᴡᴜᴊᴜᴅ ᴛᴀɴᴘᴀ ᴛɪɴᴅᴀᴋᴀɴ</code> (ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴠɪᴅᴇᴏ ᴅᴇꜰᴀᴜʟᴛ)
</blockquote>
"""

import asyncio
import html
import json
import random
import re
import requests
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from PyroUbot import *

# URL video default jika tidak ada URL yang diberikan
DEFAULT_VIDEO_URL = "https://files.catbox.moe/x2ftud.mp4"

# API key untuk BetaBotz API
APIKEY = "jagoannyabot"

# Emoji animasi untuk loading
LOADING_EMOJI = [
    "🎬", "🎭", "✨", "💫", "⭐", "🌟", "💎", "🔮", "🎞️", "📽️",
    "🎥", "📹", "🎨", "🖼️", "🌈", "✒️", "🖋️", "📝", "💭", "💡"
]

# Animasi teks loading
LOADING_TEXT = [
    "ᴍᴇᴍᴜʟᴀɪ ᴘʀᴏꜱᴇꜱ ᴘᴇᴍʙᴜᴀᴛᴀɴ ǫᴜᴏᴛᴇꜱ ᴄᴇꜱꜱ...",
    "ᴍᴇɴɢᴜɴᴅᴜʜ ᴠɪᴅᴇᴏ ꜱᴜᴍʙᴇʀ ᴄᴇꜱꜱ...",
    "ᴍᴇɴɢᴇᴋꜱᴛʀᴀᴋ ꜰʀᴀᴍᴇ ᴠɪᴅᴇᴏ ᴄᴇꜱꜱ...",
    "ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴛᴇᴋꜱ ᴋᴇ ᴠɪᴅᴇᴏ ᴄᴇꜱꜱ...",
    "ᴍᴇɴɢᴀᴛᴜʀ ᴇꜰᴇᴋ ᴠɪꜱᴜᴀʟ ᴄᴇꜱꜱ...",
    "ᴍᴇɴᴇʀᴀᴘᴋᴀɴ ꜰɪʟᴛᴇʀ ᴀᴇꜱᴛʜᴇᴛɪᴄ ᴄᴇꜱꜱ...",
    "ᴍᴇʀᴇɴᴅᴇʀ ᴠɪᴅᴇᴏ ꜰɪɴᴀʟ ᴄᴇꜱꜱ...",
    "ᴍᴇɴʏɪᴀᴘᴋᴀɴ ᴠɪᴅᴇᴏ ǫᴜᴏᴛᴇꜱ ᴇʟᴜ ᴄᴇꜱꜱ...",
    "ꜱᴇᴅɪᴋɪᴛ ʟᴀɢɪ ꜱᴇʟᴇꜱᴀɪ ᴄᴇꜱꜱ...",
    "ᴍᴇɴɢᴏᴘᴛɪᴍᴀʟᴋᴀɴ ᴋᴜᴀʟɪᴛᴀꜱ ᴠɪᴅᴇᴏ ᴄᴇꜱꜱ..."
]

# Fungsi untuk memeriksa apakah string adalah URL valid
def is_valid_url(url):
    """Memeriksa Apakah String Adalah URL Valid Cess"""
    url_pattern = re.compile(
        r'^(https?|ftp)://'  # http:// atau https://
        r'([A-Za-z0-9.-]+)'  # domain
        r'(\.[A-Za-z]{2,})'  # .com, .org, dll
        r'(:[0-9]+)?'  # port opsional
        r'(/.*)?$'  # path opsional
    )
    return bool(url_pattern.match(url))

# Fungsi untuk membuat video quotes via API
async def generate_quotes_video(video_url, quote_text, process_msg):
    """Membuat Video Quotes Dengan Teks Kustom Menggunakan API Cess"""

    # Proses pembuatan dengan animasi loading
    used_emojis = set()
    used_texts = set()
    
    for _ in range(5):
        # Pilih emoji yang belum digunakan
        available_emojis = [e for e in LOADING_EMOJI if e not in used_emojis]
        if not available_emojis:
            used_emojis.clear()
            available_emojis = LOADING_EMOJI
        
        emoji = random.choice(available_emojis)
        used_emojis.add(emoji)
        
        # Pilih teks yang belum digunakan
        available_texts = [t for t in LOADING_TEXT if t not in used_texts]
        if not available_texts:
            used_texts.clear()
            available_texts = LOADING_TEXT
        
        text = random.choice(available_texts)
        used_texts.add(text)
        
        # Update pesan dengan animasi loading
        await process_msg.edit(
            f"<blockquote><b>{emoji} {text}</b></blockquote>",
            parse_mode=ParseMode.HTML
        )
        await asyncio.sleep(1.5)
    
    # Membuat URL API dengan parameter yang sesuai
    encoded_text = requests.utils.quote(quote_text)
    encoded_url = requests.utils.quote(video_url)
    api_url = f"https://api.betabotz.eu.org/api/maker/quotesvideo?url={encoded_url}&text={encoded_text}&apikey={APIKEY}"
    
    try:
        # Melakukan panggilan ke API
        response = requests.get(api_url, timeout=60)
        
        if response.status_code != 200:
            return {
                "status": False,
                "error": f"ᴇʀʀᴏʀ API: {response.status_code}"
            }
        
        # Parse respons JSON
        try:
            data = response.json()
            
            # Contoh format respons API:
            # {
            #     "creator": "BetaBotz",
            #     "result": "https://i.supa.codes/8KKDc7"
            # }
            
            if "result" not in data:
                return {
                    "status": False,
                    "error": "ғᴏʀᴍᴀᴛ ʀᴇsᴘᴏɴs API ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ ᴄᴇss"
                }
            
            # Dapatkan URL video hasil
            result_url = data["result"]
            
            return {
                "status": True,
                "video_url": video_url,
                "result_url": result_url,
                "quote": quote_text
            }
            
        except ValueError:
            return {
                "status": False,
                "error": "ʀᴇsᴘᴏɴs ʙᴜᴋᴀɴ ғᴏʀᴍᴀᴛ JSON ʏᴀɴɢ ᴠᴀʟɪᴅ ᴄᴇss"
            }
    except requests.exceptions.Timeout:
        return {
            "status": False,
            "error": "ᴛɪᴍᴇᴏᴜᴛ sᴀᴀᴛ ᴍᴇɴɢʜᴜʙᴜɴɢɪ API ᴄᴇss"
        }
    except requests.exceptions.RequestException as e:
        return {
            "status": False,
            "error": f"ᴇʀʀᴏʀ ᴋᴏɴᴇᴋsɪ ᴄᴇss: {str(e)}"
        }
    except Exception as e:
        return {
            "status": False,
            "error": f"ᴇʀʀᴏʀ ᴛɪᴅᴀᴋ ᴛᴇʀᴅᴜɢᴀ ᴄᴇss: {str(e)}"
        }

# Format respons quotes dengan gaya menarik
def format_quotes_response(result):
    """Format Respons Hasil Pembuatan Quotes Agar Tampil Menarik Cess"""

    # Dapatkan emoji acak
    emoji_set = ["✨", "💫", "🌟", "💎", "🎬", "🎭", "📽️", "🎞️", "🖋️", "✒️"]
    emoji = random.choice(emoji_set)
    
    # Format informasi quotes
    formatted_response = f"""
<blockquote>
<b>{emoji} ᴠɪᴅᴇᴏ ǫᴜᴏᴛᴇꜱ ɢᴇɴᴇʀᴀᴛᴏʀ ᴄᴇꜱꜱ {emoji}</b>
────────────────────
<b>ǫᴜᴏᴛᴇ:</b> <i>"{result["quote"]}"</i>
────────────────────
<b>✅ ᴠɪᴅᴇᴏ ǫᴜᴏᴛᴇꜱ ᴇʟᴜ ᴛᴇʟᴀʜ ꜱɪᴀᴘ!</b>
<b>🔄 ᴍᴇɴɢɪʀɪᴍ ᴠɪᴅᴇᴏ...</b>
</blockquote>
"""
    return formatted_response

# Handler untuk ᴘᴇʀɪɴᴛᴀʜ quotes
@PY.UBOT("quotes")
async def quotes_cmd(client, message: Message):
    """Command Handler Untuk Membuat Video Quotes Cess"""

    # Simpan ID pesan asli untuk dihapus nanti
    original_msg_id = message.id
    
    # Parsing pesan untuk mendapatkan URL dan teks
    parts = message.text.split(None, 1)
    
    # Jika hanya ada ᴘᴇʀɪɴᴛᴀʜ tanpa argumen
    if len(parts) < 2:
        # Kirim pesan error dan hapus setelah 5 detik
        error_msg = await message.reply(
            "<blockquote><b>❌ ᴍᴏʜᴏɴ ᴍᴀꜱᴜᴋᴋᴀɴ ᴛᴇᴋꜱ ǫᴜᴏᴛᴇꜱ ᴄᴜᴋɪ!</b>\n\n"
            f"<b>ᴄᴏɴᴛᴏʜ:</b> <code>{message.command[0]} ʜɪᴅᴜᴘ ɪɴɪ ɪɴᴅᴀʜ, ɴɪᴋᴍᴀᴛɪ sᴇᴛɪᴀᴘ ᴍᴏᴍᴇɴɴʏᴀ ᴄᴇss</code></blockquote>",
            parse_mode=ParseMode.HTML
        )
        await asyncio.sleep(5)
        try:
            await message.delete()
            await error_msg.delete()
        except:
            pass
        return
    
    # Dapatkan argumen penuh
    args = parts[1].strip()
    
    # Periksa apakah argumen pertama adalah URL valid
    args_parts = args.split(' ', 1)
    
    if len(args_parts) > 1 and is_valid_url(args_parts[0]):
        # Jika argumen pertama adalah URL
        video_url = args_parts[0]
        quote_text = args_parts[1]
    else:
        # Jika bukan URL, gunakan URL default
        video_url = DEFAULT_VIDEO_URL
        quote_text = args
    
    # Kirim pesan proses
    process_msg = await message.reply(
        f"<blockquote><b>🎬 ᴍᴇᴍᴜʟᴀɪ ᴘʀᴏꜱᴇꜱ ᴘᴇᴍʙᴜᴀᴛᴀɴ ᴠɪᴅᴇᴏ ǫᴜᴏᴛᴇꜱ ᴄᴇꜱꜱ...</b></blockquote>",
        parse_mode=ParseMode.HTML
    )
    
    # Membuat video quotes
    result = await generate_quotes_video(video_url, quote_text, process_msg)
    
    if not result or not result.get("status"):
        error_msg = result.get("error", "ᴇʀʀᴏʀ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ ᴄᴇss") if result else "ɢᴀɢᴀʟ ᴍᴇᴍʙᴜᴀᴛ ǫᴜᴏᴛᴇs ᴄᴜᴋɪ"
        await process_msg.edit(
            f"<blockquote><b>❌ ɢᴀɢᴀʟ ᴍᴇᴍʙᴜᴀᴛ ᴠɪᴅᴇᴏ ǫᴜᴏᴛᴇꜱ ᴄᴇꜱꜱ!</b>\n<b>ᴇʀʀᴏʀ:</b> {error_msg}</blockquote>",
            parse_mode=ParseMode.HTML
        )
        # Hapus pesan error setelah 5 detik
        await asyncio.sleep(5)
        try:
            await message.delete()
            await process_msg.delete()
        except:
            pass
        return
    
    # Format respons
    formatted_response = format_quotes_response(result)
    
    # Update pesan respons
    await process_msg.edit(
        formatted_response,
        parse_mode=ParseMode.HTML
    )
    
    # Kirim video hasil
    try:
        # Coba download dan kirim video
        video_result_url = result.get("result_url")
        
        # Kirim video sebagai pesan
        emoji = random.choice(["✨", "🎬", "🎭", "📽️", "🎞️"])
        caption = f"<blockquote><b>{emoji} ᴠɪᴅᴇᴏ ǫᴜᴏᴛᴇꜱ</b>\n<i>\"{quote_text}\"</i></blockquote>"
        
        # Kirim video dengan URL
        video_msg = await message.reply_video(
            video_result_url,
            caption=caption,
            parse_mode=ParseMode.HTML
        )
        
        # Hapus pesan asli dan pesan proses setelah video terkirim
        try:
            await message.delete()
            await process_msg.delete()
        except:
            pass
        
    except Exception as e:
        # Jika gagal mengirim video, kirim link saja
        final_msg = await message.reply(
            f"<blockquote><b>✅ ᴠɪᴅᴇᴏ ǫᴜᴏᴛᴇꜱ ᴇʟᴜ:</b>\n\n{result.get('result_url')}\n\n<b>ǫᴜᴏᴛᴇ:</b> <i>\"{quote_text}\"</i></blockquote>",
            parse_mode=ParseMode.HTML
        )
        
        # Hapus pesan lain dan hanya tinggalkan link
        try:
            await message.delete()
            await process_msg.delete()
        except:
            pass