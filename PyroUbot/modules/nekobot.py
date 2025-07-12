import os
import re
import requests
from PIL import Image
from validators.url import url
from PyroUbot import *

__MODULE__ = "ɴᴇᴋᴏʙᴏᴛ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɴᴇᴋᴏʙᴏᴛ ᴄᴇꜱꜱ 』</b>

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}trump</code> [ᴛᴇᴋꜱ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇᴍʙᴜᴀᴛ ɢᴀᴍʙᴀʀ ᴛʀᴜᴍᴘ ᴛᴡᴇᴇᴛ ᴅᴇɴɢᴀɴ ᴛᴇᴋꜱ ʏᴀɴɢ ᴅɪʙᴇʀɪᴋᴀɴ

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}qg</code> [ᴛᴇᴋꜱ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇᴍʙᴜᴀᴛ ɢᴀᴍʙᴀʀ ᴛᴡᴇᴇᴛ @QoryGore

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}cmm</code> [ᴛᴇᴋꜱ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇᴍʙᴜᴀᴛ ɢᴀᴍʙᴀʀ ʙᴀɴɴᴇʀ ᴄʜᴀɴɢᴇ ᴍʏ ᴍɪɴᴅ

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}kanna</code> [ᴛᴇᴋꜱ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇᴍʙᴜᴀᴛ ɢᴀᴍʙᴀʀ ᴋᴀɴɴᴀɢᴇɴ

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}tweet</code> [ᴜꜱᴇʀɴᴀᴍᴇ].[ᴛᴇᴋꜱ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇᴍʙᴜᴀᴛ ɢᴀᴍʙᴀʀ ᴛᴡᴇᴇᴛ ᴅᴇɴɢᴀɴ ᴜꜱᴇʀɴᴀᴍᴇ ᴅᴀɴ ᴛᴇᴋꜱ ʏᴀɴɢ ᴅɪʙᴇʀɪᴋᴀɴ
</blockquote>
"""

EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+"
)

def deEmojify(inputString: str) -> str:
    return re.sub(EMOJI_PATTERN, "", inputString)

def get_nekobot_img(url_api):
    r = requests.get(url_api).json()
    geng = r.get("message")
    if not url(geng):
        return None
    with open("gpx.png", "wb") as f:
        f.write(requests.get(geng).content)
    img = Image.open("gpx.png").convert("RGB")
    img.save("gpx.webp", "webp")
    return "gpx.webp"

def purge():
    try:
        os.remove("gpx.png")
        os.remove("gpx.webp")
    except OSError:
        pass

@PY.UBOT(["trump"])
async def _(c, m):
    text = m.text.split(None, 1)[1] if len(m.command) > 1 else None
    if not text:
        return await m.reply("<b>ᴋɪʀɪᴍᴋᴀɴ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ᴛʀᴜᴍᴘ ᴛᴡᴇᴇᴛ ᴄᴜᴋɪ!</b>")
    await m.reply("<b>ᴍᴇᴍʙᴜᴀᴛ ᴛʀᴜᴍᴘ ᴛᴡᴇᴇᴛ ᴄᴇꜱꜱ...</b>")
    text = deEmojify(text)
    img = get_nekobot_img(f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}")
    if not img:
        return await m.reply("<b>ɢᴀɢᴀʟ ᴍᴇɴɢɢᴇɴᴇʀᴀᴛᴇ ɢᴀᴍʙᴀʀ ᴄᴜᴋɪ!</b>")
    await m.reply_document(img)
    purge()

@PY.UBOT(["qg"])
async def _(c, m):
    text = m.text.split(None, 1)[1] if len(m.command) > 1 else None
    if not text:
        return await m.reply("<b>ᴋɪʀɪᴍᴋᴀɴ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ @QoryGore ᴛᴡᴇᴇᴛ ᴄᴜᴋɪ!</b>")
    await m.reply("<b>ᴍᴇᴍʙᴜᴀᴛ ᴛᴡᴇᴇᴛ @QoryGore ᴄᴇꜱꜱ...</b>")
    text = deEmojify(text)
    img = get_nekobot_img(f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=QoryGore")
    if not img:
        return await m.reply("<b>ɢᴀɢᴀʟ ᴍᴇɴɢɢᴇɴᴇʀᴀᴛᴇ ɢᴀᴍʙᴀʀ ᴄᴜᴋɪ!</b>")
    await m.reply_document(img)
    purge()

@PY.UBOT(["cmm"])
async def _(c, m):
    text = m.text.split(None, 1)[1] if len(m.command) > 1 else None
    if not text:
        return await m.reply("<b>ᴋɪʀɪᴍᴋᴀɴ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ʙᴀɴɴᴇʀ ᴄᴜᴋɪ!</b>")
    await m.reply("<b>ᴍᴇᴍʙᴜᴀᴛ ʙᴀɴɴᴇʀ ᴄᴇꜱꜱ...</b>")
    text = deEmojify(text)
    img = get_nekobot_img(f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}")
    if not img:
        return await m.reply("<b>ɢᴀɢᴀʟ ᴍᴇɴɢɢᴇɴᴇʀᴀᴛᴇ ɢᴀᴍʙᴀʀ!</b>")
    await m.reply_document(img)
    purge()

@PY.UBOT(["kanna"])
async def _(c, m):
    text = m.text.split(None, 1)[1] if len(m.command) > 1 else None
    if not text:
        return await m.reply("<b>ᴋɪʀɪᴍᴋᴀɴ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ᴋᴀɴɴᴀɢᴇɴ!</b>")
    await m.reply("<b>ᴋᴀɴɴᴀ ᴍᴇɴᴜʟɪꜱ ᴛᴇᴋꜱ ᴇʟᴜ ᴄᴇꜱꜱ...</b>")
    text = deEmojify(text)
    img = get_nekobot_img(f"https://nekobot.xyz/api/imagegen?type=kannagen&text={text}")
    if not img:
        return await m.reply("<b>ɢᴀɢᴀʟ ᴍᴇɴɢɢᴇɴᴇʀᴀᴛᴇ ɢᴀᴍʙᴀʀ ᴄᴜᴋɪ!</b>")
    await m.reply_document(img)
    purge()

@PY.UBOT(["tweet"])
async def _(c, m):
    text = m.text.split(None, 1)[1] if len(m.command) > 1 else None
    if not text or "." not in text:
        return await m.reply("<b>ᴋɪʀɪᴍᴋᴀɴ ᴜꜱᴇʀɴᴀᴍᴇ.ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ᴛᴡᴇᴇᴛ ᴄᴜᴋɪ!</b>")
    username, tweet_text = text.split(".", 1)
    await m.reply(f"<b>ᴍᴇᴍʙᴜᴀᴛ ᴛᴡᴇᴇᴛ @{username}...</b>")
    tweet_text = deEmojify(tweet_text)
    img = get_nekobot_img(f"https://nekobot.xyz/api/imagegen?type=tweet&text={tweet_text}&username={username}")
    if not img:
        return await m.reply("<b>ɢᴀɢᴀʟ ᴍᴇɴɢɢᴇɴᴇʀᴀᴛᴇ ɢᴀᴍʙᴀʀ ᴄᴜᴋɪ!</b>")
    await m.reply_document(img)
    purge()
