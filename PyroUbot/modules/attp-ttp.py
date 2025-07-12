import requests
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "ᴀᴛᴛᴘ-ᴛᴛᴘ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀᴛᴛᴘ & ᴛᴛᴘ ᴄᴇꜱꜱ 』</b>

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> 
    ◉ <code>{0}ᴀᴛᴛᴘ</code> <i>ᴛᴇᴋꜱ</i> - ᴍᴇᴍʙᴜᴀᴛ ꜱᴛɪᴋᴇʀ ᴛᴇᴋꜱ ʙᴇʀᴡᴀʀɴᴀ.
    ◉ <code>{0}ᴛᴛᴘ</code> <i>ᴛᴇᴋꜱ</i> - ᴍᴇᴍʙᴜᴀᴛ ꜱᴛɪᴋᴇʀ ᴛᴇᴋꜱ ʙɪᴀꜱᴀ.</blockquote>
"""

API_KEY = "moire"

@PY.UBOT("attp")
async def attp(client, message):
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    jalan = await message.reply(f"{prs} ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ ᴄᴇꜱꜱ...")
    
    try:
        # Ambil teks dari perintah
        args = message.text.split(' ', 1)
        if len(args) < 2:
            await jalan.edit(f"{ggl} ʜᴀʀᴀᴘ ᴍᴀꜱᴜᴋᴋᴀɴ ᴛᴇᴋꜱ ᴄᴜᴋɪ! ᴄᴏɴᴛᴏʜ: <code>!ᴀᴛᴛᴘ ʜᴀʟᴏ</code>")
            return
        
        text = args[1]
        # URL API untuk ATTP
        url = f"https://api.botcahx.eu.org/api/maker/attp?text={text}&apikey=025a6ef0"
        
        # Kirim permintaan ke API
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Simpan file sementara untuk dikirim
            with open("attp.webp", "wb") as file:
                file.write(response.content)
            
            # Kirim sebagai animasi (stiker animasi)
            await client.send_sticker(
                chat_id=message.chat.id,
                sticker="attp.webp",
                reply_to_message_id=message.id
            )
            await jalan.delete()
        else:
            await jalan.edit(f"{ggl} ɢᴀɢᴀʟ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ꜱᴛɪᴋᴇʀ ᴀᴛᴛᴘ. ꜱᴛᴀᴛᴜꜱ: {response.status_code}")
    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} ᴘᴇʀᴍɪɴᴛᴀᴀɴ ɢᴀɢᴀʟ ᴄᴜᴋɪ: {e}")
    except Exception as e:
        await jalan.edit(f"{ggl} ᴛᴇʀᴊᴀᴅɪ ᴋᴇꜱᴀʟᴀʜᴀɴ ᴄᴜᴋɪ: {e}")

@PY.UBOT("ttp")
async def ttp(client, message):
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    jalan = await message.reply(f"{prs} ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ ᴄᴇꜱꜱ...")
    
    try:
        # Ambil teks dari perintah
        args = message.text.split(' ', 1)
        if len(args) < 2:
            await jalan.edit(f"{ggl} ʜᴀʀᴀᴘ ᴍᴀꜱᴜᴋᴋᴀɴ ᴛᴇᴋꜱ! ᴄᴏɴᴛᴏʜ: <code>!ᴛᴛᴘ ʜᴀʟᴏ</code>")
            return
        
        text = args[1]
        # URL API untuk TTP
        url = f"https://api.botcahx.eu.org/api/maker/ttp?text={text}&apikey=025a6ef0"
        
        # Kirim permintaan ke API
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Simpan file sementara untuk dikirim
            with open("ttp.webp", "wb") as file:
                file.write(response.content)
            
            # Kirim sebagai stiker
            await client.send_sticker(
                chat_id=message.chat.id,
                sticker="ttp.webp",
                reply_to_message_id=message.id
            )
            await jalan.delete()
        else:
            await jalan.edit(f"{ggl} ɢᴀɢᴀʟ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ꜱᴛɪᴋᴇʀ ᴛᴛᴘ. ꜱᴛᴀᴛᴜꜱ: {response.status_code}")
    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} ᴘᴇʀᴍɪɴᴛᴀᴀɴ ɢᴀɢᴀʟ: {e}")
    except Exception as e:
        await jalan.edit(f"{ggl} ᴛᴇʀᴊᴀᴅɪ ᴋᴇꜱᴀʟᴀʜᴀɴ: {e}")
