import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "ɢᴇᴍᴘᴀ"
__HELP__ = """
<blockquote><b>『 ɢᴇᴍᴘᴀ ᴄᴇꜱꜱ 』</b>

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ɢᴇᴍᴘᴀ</code>
   <i>ᴘᴇɴᴊᴇʟᴀꜱᴀɴ:</b> ᴄᴇᴋ ɪɴꜰᴏ ꜱᴇᴋɪᴛᴀʀ ɢᴇᴍᴘᴀ ʙᴍᴋɢ</i></blockquote>

"""

@PY.UBOT("gempa")
async def stalkig(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)

    jalan = await message.reply(f"{prs} ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    chat_id = message.chat.id
    url = f"https://api.botcahx.eu.org/api/search/gempa?apikey=025a6ef0"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            hasil = data['result']['result']
            lintang = hasil['Lintang']
            bujur = hasil['Bujur']
            magnitude = hasil['Magnitudo']
            kedalaman = hasil['Kedalaman']
            potensi = hasil['Potensi']
            wilayah = hasil['Wilayah']
            tanggal = hasil['tanggal']
            jam = hasil['jam']
            photoUrl = f"https://warning.bmkg.go.id/img/logo-bmkg.png"
            caption = f"""
<blockquote><b>╭─ •  「 <b>ɪɴꜰᴏ ɢᴇᴍᴘᴀ ᴛᴇʀᴋɪɴɪ</b> 」
│  ◦ <b>ᴍᴀɢɴɪᴛᴜᴅᴇ: <code>{magnitude}</code></b>
│  ◦ <b>ᴋᴇᴅᴀʟᴀᴍᴀɴ: <code>{kedalaman}</code></b>
│  ◦ <b>ᴋᴏᴏʀᴅɪɴᴀᴛ: <code>{bujur}, {lintang}</code></b>
│  ◦ <b>ᴡᴀᴋᴛᴜ: <code>{tanggal}, {jam}</code></b>
│  ◦ <b>ʟᴏᴋᴀꜱɪ: <code>{wilayah}</code></b>
│  ◦ <b>ᴘᴏᴛᴇɴꜱɪ: <code>{potensi}</code></b>
╰──── • 
</blockquote></b>
"""
            photo_path = wget.download(photoUrl)
            await client.send_photo(chat_id, caption=caption, photo=photo_path)
            if os.path.exists(photo_path):
                os.remove(photo_path)
            
            await jalan.delete()
        else:
            await jalan.edit(f"{ggl} ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴋᴜɴᴄɪ 'ʜᴀꜱɪʟ' ᴅᴀʟᴀᴍ ʀᴇsᴘᴏɴs ᴄᴜᴋɪ ᴄᴇss.")
    
    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} ᴘᴇʀᴍɪɴᴛᴀᴀɴ ɢᴀɢᴀʟ ᴄᴇss: {e}")

    except Exception as e:
        await jalan.edit(f"{ggl} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ᴄᴇss: {e}")
