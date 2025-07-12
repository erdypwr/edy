import os
import requests
from PyroUbot import *
from bs4 import BeautifulSoup
from wikipedia import summary, exceptions as wiki_exceptions

__MODULE__ = "ꜱᴄʀᴀᴘᴇʀꜱ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱᴄʀᴀᴘᴇʀꜱ ᴄᴇꜱꜱ 』</b>

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}img</code> [ᴋᴀᴛᴀ ᴋᴜɴᴄɪ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴᴄᴀʀɪ ɢᴀᴍʙᴀʀ ᴅɪ ɢᴏᴏɢʟᴇ ᴅᴀɴ ᴍᴇɴɢɪʀɪᴍ ʜᴀꜱɪʟɴʏᴀ

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}wiki</code> [ᴋᴀᴛᴀ ᴋᴜɴᴄɪ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴᴄᴀʀɪ ɪɴꜰᴏʀᴍᴀꜱɪ ᴅɪ ᴡɪᴋɪᴘᴇᴅɪᴀ
</blockquote>
"""

@PY.UBOT(["img"])
async def _(c, m):
    query = m.text.split(None, 1)[1] if len(m.command) > 1 else None
    if not query:
        return await m.reply("<b>ᴍᴀꜱᴜᴋᴋᴀɴ ᴋᴀᴛᴀ ᴋᴜɴᴄɪ ᴘᴇɴᴄᴀʀɪᴀɴ ɢᴀᴍʙᴀʀ ᴄᴜᴋɪ!</b>")
    await m.reply("<b>ᴍᴇɴᴄᴀʀɪ ɢᴀᴍʙᴀʀ ᴄᴇꜱꜱ...</b>")
    url = f"https://www.google.com/search?tbm=isch&q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    images = [img["src"] for img in soup.find_all("img") if img.get("src") and "gstatic" in img.get("src")]
    if not images:
        return await m.reply("<b>ɢᴀᴍʙᴀʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴄᴜᴋɪ!</b>")
    await c.send_photo(m.chat.id, images[0], caption=f"<b>ʜᴀꜱɪʟ ᴘᴇɴᴄᴀʀɪᴀɴ ɢᴀᴍʙᴀʀ ᴅᴀʀɪ:</b> <code>{query}</code>")

@PY.UBOT(["wiki"])
async def _(c, m):
    query = m.text.split(None, 1)[1] if len(m.command) > 1 else None
    if not query:
        return await m.reply("<b>ᴍᴀꜱᴜᴋᴋᴀɴ ᴋᴀᴛᴀ ᴋᴜɴᴄɪ ᴘᴇɴᴄᴀʀɪᴀɴ ᴡɪᴋɪᴘᴇᴅɪᴀ ᴄᴜᴋɪ!</b>")
    await m.reply("<b>ᴍᴇɴᴄᴀʀɪ ᴅɪ ᴡɪᴋɪᴘᴇᴅɪᴀ ᴄᴇꜱꜱ...</b>")
    try:
        result = summary(query)
        if len(result) >= 4096:
            with open("output.txt", "w+") as file:
                file.write(result)
            await c.send_document(m.chat.id, "output.txt", caption=f"<b>ʜᴀꜱɪʟ ᴡɪᴋɪᴘᴇᴅɪᴀ ᴛᴇʀʟᴀʟᴜ ᴘᴀɴᴊᴀɴɢ, ᴅɪᴋɪʀɪᴍ sᴇʙᴀɢᴀɪ ғɪʟᴇ ᴄᴇꜱꜱ</b>")
            os.remove("output.txt")
            return
        await m.reply(f"<b>ʜᴀꜱɪʟ ᴡɪᴋɪᴘᴇᴅɪᴀ ᴄᴇꜱꜱ:</b>\n{result}")
    except wiki_exceptions.DisambiguationError as error:
        await m.reply(f"<b>ᴅɪᴛᴇᴍᴜᴋᴀɴ ʜᴀʟᴀᴍᴀɴ ᴛɪᴅᴀᴋ ᴀᴍʙɪɢᴜ ᴄᴜᴋɪ:</b>\n{error}")
    except wiki_exceptions.PageError as pageerror:
        await m.reply(f"<b>ʜᴀʟᴀᴍᴀɴ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴄᴜᴋɪ:</b>\n{pageerror}")
