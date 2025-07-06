import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *
from PyroUbot.core.helpers.emoji import EMO

__MODULE__ = "ʟʏʀɪᴄꜱ"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟʏʀɪᴄꜱ ᴄᴇꜱꜱ 』</b>

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ʟʏʀɪᴄꜱ</code> 
   <i>ᴘᴇɴᴊᴇʟᴀꜱᴀɴ:</b> ᴘᴇɴᴄᴀʀɪᴀɴ ʟɪʀɪᴋ ᴍᴜꜱɪᴋ ᴄᴇꜱꜱ</i>
"""

@PY.UBOT("lyrics")
async def lyrics(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"{prs} ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    
    if len(message.command) != 2:
        return await jalan.edit(f"{ggl} ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ `ʟʏʀɪᴄꜱ` ᴊᴜᴅᴜʟ ᴍᴜꜱɪᴋ ᴄᴇꜱꜱ.")

    lyrics = message.command[1]
    chat_id = message.chat.id
    url = f"https://widipe.com/lirik?text={lyrics}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            hasil = data['result']
            lyrics = hasil['lyrics']
            photoUrl = f"https://cdn.vectorstock.com/i/1000v/71/92/music-lyrics-logo-mark-for-concert-vector-35117192.jpg"
            caption = f"""
<b><emoji id=5841235769728962577>⭐</emoji>{lyrics}</b>
"""
            photo_path = wget.download(photoUrl)
            await client.send_photo(chat_id, caption=caption, photo=photo_path)
            if os.path.exists(photo_path):
                os.remove(photo_path)
            
            await jalan.delete()
        else:
            await jalan.edit(f"{ggl} ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴋᴜɴᴄɪ 'hasil' ᴅᴀʟᴀᴍ ʀᴇꜱᴘᴏɴꜱ ᴄᴜᴋɪ ᴄᴇꜱꜱ.")

    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} ᴘᴇʀᴍɪɴᴛᴀᴀɴ ɢᴀɢᴀʟ ᴄᴇꜱꜱ: {e}")

    except Exception as e:
        await jalan.edit(f"{ggl} ᴛᴇʀᴊᴀᴅɪ ᴋᴇꜱᴀʟᴀʜᴀɴ ᴄᴇꜱꜱ: {e}")
