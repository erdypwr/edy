# 🍀 © @tofik_dn
# ⚠️ Do not remove credits
import asyncio
from pyrogram.errors import FloodWait
from PyroUbot import *

__MODULE__ = "ʟᴏɢᴏ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟᴏɢᴏ ᴄᴇꜱꜱ 』</b>

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}logo</code> [ᴛᴇᴋꜱ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇᴍʙᴜᴀᴛ ʟᴏɢᴏ ᴅᴀʀɪ ᴛᴇᴋꜱ ʏᴀɴɢ ᴅɪʙᴇʀɪᴋᴀɴ ᴍᴇʟᴀʟᴜɪ @tdtapibot
</blockquote>
"""

@PY.UBOT("logo")
async def _(c, m):
    user = await c.get_me()
    text = m.text.split(None, 1)[1] if len(m.command) > 1 else None
    if not text:
        return await m.reply("<b>ꜱɪʟᴀᴋᴀɴ ᴍᴀꜱᴜᴋᴋᴀɴ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ʟᴏɢᴏ ᴄᴜᴋɪ!</b>")
    proses = await m.reply("<b>ᴘʀᴏꜱᴇꜱ ᴍᴇᴍʙᴜᴀᴛ ʟᴏɢᴏ ᴄᴇꜱꜱ...</b>")
    chat = "@tdtapibot"
    try:
        async with c.conversation(chat) as conv:
            msg = await conv.send_message(f"/logo {text}")
            response = await conv.get_response()
            logo = await conv.get_response()
            await c.send_read_action(conv.chat_id, "typing")
    except Exception:
        await proses.edit("<b>ᴇʀʀᴏʀ: ᴍᴏʜᴏɴ ʙᴜᴋᴀ ʙʟᴏᴋɪʀ @tdtapibot ᴅᴀɴ ᴄᴏʙᴀ ʟᴀɢɪ!</b>")
        return
    await asyncio.sleep(0.5)
    await m.reply_document(logo.document, caption=f"ʟᴏɢᴏ ʙʏ <a href='tg://user?id={user.id}'>{user.first_name}</a>")
    await c.delete_messages(conv.chat_id, [msg.id, response.id, logo.id])
    await proses.delete()
