from PyroUbot import *
import random
import requests
from pyrogram.enums import *
from pyrogram.enums import ChatAction
from pyrogram import *
from pyrogram.types import *
from io import BytesIO

__MODULE__ = "ᴡᴀʟʟᴘᴀᴘᴇʀ 2"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴡᴀʟʟᴘᴀᴘᴇʀ ᴄᴇꜱꜱ 』</b>

<blockquote><b>ᴘᴇʀɪɴᴛᴀʜ :
<code>{0}wallpp2</code> [ǫᴜᴇʀʏ]
ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ᴡᴀʟʟᴘᴀᴘᴇʀ/ɢᴀᴍʙᴀʀ

✮ ǫᴜᴇʀʏ ✮
   卍 ᴄᴏꜱᴘʟᴀʏ
   卍 ᴘᴜʙɢ
   卍 ᴄᴏɢᴀɴ2   
   卍 ᴄᴇᴄᴀɴ2   
   卍 ᴍᴏᴛᴏʀ
   卍 ᴍᴏʙɪʟ     
   卍 ᴍᴏᴜɴᴛᴀɪɴ 
   卍 ᴄʏʙᴇʀꜱᴘᴀᴄᴇ 
   卍 ᴅᴀʀᴋᴊᴏᴋᴇꜱ  
   卍 ᴍᴇᴍᴇ 
"""

URLS = {
    "cosplay": "https://api.botcahx.eu.org/api/wallpaper/cosplay?apikey=045705b1",
    "meme": "https://api.botcahx.eu.org/api/random/meme?apikey=045705b1",
    "darkjokes": "https://api.botcahx.eu.org/api/random/darkjokes?apikey=045705b1",
    "cyberspace": "https://api.botcahx.eu.org/api/wallpaper/cyberspace?apikey=045705b1",
    "mountain": "https://api.botcahx.eu.org/api/wallpaper/mountain?apikey=045705b1",
    "mobil": "https://api.botcahx.eu.org/api/wallpaper/mobil?apikey=045705b1",
    "motor": "https://api.botcahx.eu.org/api/wallpaper/motor?apikey=045705b1",
    "cecan2": "https://api.botcahx.eu.org/api/wallpaper/cecan2?apikey=045705b1",
    "cogan2": "https://api.botcahx.eu.org/api/wallpaper/cogan2?apikey=045705b1",
    "pubg": "https://api.botcahx.eu.org/api/wallpaper/pubg?apikey=045705b1",
    }


@PY.UBOT("wallpp2")
@PY.TOP_CMD
async def _(client, message):
    # Extract query from message
    query = message.text.split()[1] if len(message.text.split()) > 1 else None
    
    if query not in URLS:
        valid_queries = ", ".join(URLS.keys())
        await message.reply(f"<emoji id=5215204871422093648>❌</emoji> ǫᴜᴇʀʏ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ ᴄᴜᴋɪ. ɢᴜɴᴀᴋᴀɴ ꜱᴀʟᴀʜ ꜱᴀᴛᴜ ᴅᴀʀɪ: {valid_queries}.")
        return

    processing_msg = await message.reply("<emoji id=4943239162758169437>🤩</emoji> ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    
    try:
        await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        response = requests.get(URLS[query])
        response.raise_for_status()
        
        photo = BytesIO(response.content)
        photo.name = 'image.jpg'
        
        await client.send_photo(message.chat.id, photo)
        await processing_msg.delete()
    except requests.exceptions.RequestException as e:
        await processing_msg.edit_text(f"<emoji id=5215204871422093648>❌</emoji> ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ɢᴀᴍʙᴀʀ ᴀɴɪᴍᴇ ᴄᴜᴋɪ: {e}")
