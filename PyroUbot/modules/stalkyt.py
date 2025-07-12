import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "sᴛᴀʟᴋʏᴛ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱᴛᴀʟᴋ ʏᴛ ᴄᴇꜱꜱ 』

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}stalkyt</code> 
    ᴜɴᴛᴜᴋ ꜱᴛᴀʟᴋ ʏᴛ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴜꜱᴇʀɴᴀᴍᴇ</b></blockquote>
"""

@PY.UBOT("stalkyt")
async def stalkyt(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"{prs} ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    
    if len(message.command) != 2:
        return await jalan.edit(f"{ggl} ꜱɪʟᴀᴋᴀɴ ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ `ꜱᴛᴀʟᴋʏᴛ` ᴅɪɪᴋᴜᴛɪ ᴜꜱᴇʀɴᴀᴍᴇ ʏᴏᴜᴛᴜʙᴇ.")
    
    username = message.command[1]
    chat_id = message.chat.id
    url = f"https://api.betabotz.eu.org/api/stalk/yt?username={username}&apikey=Btz-bxwol"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'result' in data and 'data' in data['result'] and len(data['result']['data']) > 0:
                first_channel = data['result']['data'][0]
                photoUrl = first_channel['avatar']
                description = first_channel.get('description', 'no desk')
                caption = f"""
<blockquote><b>ᴄʜᴀɴɴᴇʟ ɴᴀᴍᴇ:</b> <code>{first_channel['channelName']}</code>
<b>ꜱᴜʙꜱᴄʀɪʙᴇʀꜱ:</b> <code>{first_channel['subscriberH']}</code>
<b>ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ:</b> <code>{description}</code>
<b>ᴜʀʟ:</b> <code>{first_channel['url']}</code></blockquote>
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
