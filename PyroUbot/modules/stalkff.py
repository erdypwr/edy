import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "ꜱᴛᴀʟᴋꜰꜰ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱᴛᴀʟᴋꜰꜰ ᴄᴇꜱꜱ 』</b>

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}stalkff</code> 
   <i>ᴘᴇɴᴊᴇʟᴀꜱᴀɴ:</b> ꜱᴇᴀʀᴄʜ ᴀᴋᴜɴ ꜰꜰ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ɪᴅ</i></blockquote>
"""

@PY.UBOT("stalkff")
async def stalkff(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)

    jalan = await message.reply(f"{prs} ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")

    if len(message.command) != 2:
        return await jalan.edit(f"{ggl} ꜱɪʟᴀᴋᴀɴ ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ `ꜱᴛᴀʟᴋꜰꜰ` ɪᴅ ᴀᴋᴜɴ.")
    
    id = message.command[1]
    chat_id = message.chat.id
    url = f"https://ff.lxonfire.workers.dev/?id={id}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            Nicname = data['nickname']
            region = data['region']
            openid = data['open_id']
            photoUrl = data['img_url']
            caption = f"""
<b><emoji id=5841235769728962577>⭐</emoji>ɴɪᴄɴᴀᴍᴇ: <code>{Nicname}</code></b>
<b><emoji id=5843952899184398024>⭐</emoji>ʀᴇɢɪᴏɴ: <code>{region}</code></b>
<b><emoji id=5841243255856960314>⭐</emoji>ᴏᴘᴇɴɪᴅ: <code>{openid}</code></b>
"""
            photo_path = wget.download(photoUrl)
            await client.send_photo(chat_id, caption=caption, photo=photo_path)
            if os.path.exists(photo_path):
                os.remove(photo_path)
            
            await jalan.delete()
        else:
            await jalan.edit(f"{ggl} ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴋᴜɴᴄɪ 'ʜᴀꜱɪʟ' ᴅᴀʟᴀᴍ ʀᴇꜱᴘᴏɴꜱ ᴄᴜᴋɪ.")
    
    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} ᴘᴇʀᴍɪɴᴛᴀᴀɴ ɢᴀɢᴀʟ ᴄᴏʙᴀ ʟᴀɢɪ ᴄᴜᴋɪ!: {e}")
    
    except Exception as e:
        await jalan.edit(f"{ggl} ᴛᴇʀᴊᴀᴅɪ ᴋᴇꜱᴀʟᴀʜᴀɴ ᴄᴜᴋɪ!: {e}")
