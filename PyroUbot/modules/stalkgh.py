import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "sᴛᴀʟᴋɢʜ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴛᴀʟᴋ ɢʜ ᴄᴇꜱꜱ 』</b>

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}sᴛᴀʟᴋɢʜ</code> 
    ᴜɴᴛᴜᴋ sᴛᴀʟᴋ ɢɪᴛʜᴜʙ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴜsᴇʀɴᴀᴍᴇ</b></blockquote>
"""

@PY.UBOT("stalkgh")
async def stalkgh(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"{prs} ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    
    if len(message.command) != 2:
        return await jalan.edit(f"{ggl} ꜱɪʟᴀᴋᴀɴ ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ `ꜱᴛᴀʟᴋɢʜ` ᴅɪɪᴋᴜᴛɪ ᴜꜱᴇʀɴᴀᴍᴇ ɢɪᴛʜᴜʙ.")
    
    username = message.command[1]
    chat_id = message.chat.id
    url = f"https://api.betabotz.eu.org/api/stalk/github?username={username}&apikey=Btz-bxwol"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'result' in data and 'user' in data['result'] and len(data['result']['user']) > 0:
                result = data['result']['user']
                photoUrl = f"https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png"
                caption = f"""
<blockquote><b>ɴᴀᴍᴇ:</b> <code>{result['name']}</code>
<b>ᴜꜱᴇʀɴᴀᴍᴇ:</b> <code>{result['username']}</code>
<b>ꜰᴏʟʟᴏᴡᴇʀꜱ:</b> <code>{result['followers']}</code>
<b>ꜰᴏʟʟᴏᴡɪɴɢ:</b> <code>{result['following']}</code>
<b>ʙɪᴏ:</b> <code>{result['bio']}</code>
<b>ɪᴅ:</b> <code>{result['idUser']}</code></blockquote>
"""
                photo_path = wget.download(photoUrl)
                await client.send_photo(chat_id, caption=caption, photo=photo_path)
                if os.path.exists(photo_path):
                    os.remove(photo_path)
                
                await jalan.delete()
            else:
                await jalan.edit(f"{ggl} ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀᴛᴀ ᴄʜᴀɴɴᴇʟ ᴅɪᴛᴇᴍᴜᴋᴀɴ.")
        else:
            await jalan.edit(f"{ggl} ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ. ꜱᴛᴀᴛᴜꜱ ᴄᴏᴅᴇ: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} ᴘᴇʀᴍɪɴᴛᴀᴀɴ ɢᴀɢᴀʟ ᴄᴏʙᴀ ʟᴀɢɪ ᴄᴜᴋɪ!: {e}")
    
    except Exception as e:
        await jalan.edit(f"{ggl} ᴛᴇʀᴊᴀᴅɪ ᴋᴇꜱᴀʟᴀʜᴀɴ ᴄᴜᴋɪ!: {e}")
