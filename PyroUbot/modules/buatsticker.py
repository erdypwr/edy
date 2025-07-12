# Random RGB Sticklet by @PhycoNinja13b
# modified by @UniBorg
# ported to userbot by @heyworld & thanks to @Xcruzhd2 for Fonts
import io
import os
import random
import textwrap
from PIL import Image, ImageDraw, ImageFont
from pyrogram.types import Message
from PyroUbot import *

__MODULE__ = "ʙᴜᴀᴛꜱᴛɪᴄᴋᴇʀ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙᴜᴀᴛꜱᴛɪᴄᴋᴇʀ ᴄᴇꜱꜱ 』</b>

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}cs</code> [ᴛᴇᴋꜱ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇᴍʙᴜᴀᴛ ꜱᴛɪᴄᴋᴇʀ ᴅᴀʀɪ ᴛᴇᴋꜱ ᴅᴇɴɢᴀɴ ʀᴀɴᴅᴏᴍ ᴡᴀʀɴᴀ ʀɢʙ
</blockquote>
"""

async def get_font_file(client, channel_id):
    font_file_message_s = await client.get_messages(
        channel_id,
        filter="document",
        limit=None,
    )
    font_file_message = random.choice(font_file_message_s)
    return await client.download_media(font_file_message)

@PY.UBOT(["cs"])
async def _(c, m: Message):
    text = m.text.split(None, 1)[1] if len(m.command) > 1 else None
    if not text:
        return await m.reply("<b>ᴍᴀꜱᴜᴋᴋᴀɴ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ꜱᴛɪᴄᴋᴇʀ ᴄᴜᴋɪ!</b>")
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    sticktext = textwrap.wrap(text, width=10)
    sticktext = "\n".join(sticktext)
    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 230
    FONT_FILE = await get_font_file(c, "@xcruzfont")
    font = ImageFont.truetype(FONT_FILE, size=fontsize)
    while draw.multiline_textsize(sticktext, font=font) > (512, 512):
        fontsize -= 3
        font = ImageFont.truetype(FONT_FILE, size=fontsize)
    width, height = draw.multiline_textsize(sticktext, font=font)
    draw.multiline_text(
        ((512 - width) / 2, (512 - height) / 2), sticktext, font=font, fill=(R, G, B)
    )
    image_stream = io.BytesIO()
    image_stream.name = "sticker.webp"
    image.save(image_stream, "WebP")
    image_stream.seek(0)
    await m.reply_document(image_stream, caption="<b>ꜱᴛɪᴄᴋᴇʀ ᴛᴇʀʙᴜᴀᴛ ᴄᴇꜱꜱ!</b>")
    try:
        os.remove(FONT_FILE)
    except Exception:
        pass
