import os
import asyncio
import time
from glitch_this import ImageGlitcher
from PIL import Image
from PyroUbot import *

__MODULE__ = "ɢʟɪᴛᴄʜ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ɢʟɪᴛᴄʜ 』</b>

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}glitch</code> [ʟᴇᴠᴇʟ 1-8] [ʙᴀʟᴀꜱ ɢᴀᴍʙᴀʀ/ꜱᴛɪᴄᴋᴇʀ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴɢɢʟɪᴛᴄʜ ɢᴀᴍʙᴀʀ/ꜱᴛɪᴄᴋᴇʀ ᴅᴇɴɢᴀɴ ᴇꜰᴇᴋ ɢʟɪᴛᴄʜ ᴅᴀʀɪ ʟᴇᴠᴇʟ 1-8 (ᴅᴇꜰᴀᴜʟᴛ 2)
</blockquote>
"""

TEMP_DOWNLOAD_DIRECTORY = "./downloads/"
GLITCHED = TEMP_DOWNLOAD_DIRECTORY + "glitch.gif"

@PY.UBOT(["glitch"])
async def _(c, m):
    if not m.reply_to_message or not m.reply_to_message.media:
        return await m.reply("<b>ʙᴀʟᴀꜱ ᴋᴇ ɢᴀᴍʙᴀʀ/ꜱᴛɪᴄᴋᴇʀ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪɢʟɪᴛᴄʜ!</b>")
    await m.reply("<b>ᴍᴇɴɢᴜɴᴅᴜʜ ᴍᴇᴅɪᴀ...</b>")
    file = await m.reply_to_message.download(file_name=TEMP_DOWNLOAD_DIRECTORY)
    try:
        args = m.text.split()
        value = int(args[1]) if len(args) > 1 and args[1].isdigit() and 1 <= int(args[1]) <= 8 else 2
    except Exception:
        value = 2
    await m.reply("<b>ᴍᴇɴɢɢʟɪᴛᴄʜ ɢᴀᴍʙᴀʀ...</b>")
    glitcher = ImageGlitcher()
    img = Image.open(file)
    glitch_img = glitcher.glitch_image(img, value, color_offset=True, gif=True)
    DURATION = 200
    LOOP = 0
    glitch_img[0].save(
        GLITCHED,
        format="GIF",
        append_images=glitch_img[1:],
        save_all=True,
        duration=DURATION,
        loop=LOOP,
    )
    await m.reply("<b>ᴍᴇɴɢᴜɴɢɢᴀʜ ɢᴀᴍʙᴀʀ ɢʟɪᴛᴄʜ...</b>")
    c_time = time.time()
    await c.send_document(m.chat.id, GLITCHED, reply_to_message_id=m.reply_to_message.message_id if m.reply_to_message else None)
    os.remove(file)
    os.remove(GLITCHED)
