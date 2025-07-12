# This is a troll indeed ffs _facepalm_
# Ported from xtra-telegram by @heyworld
import asyncio
from PyroUbot import *
from pyrogram.types import Message
import platform

__MODULE__ = "ꜰᴀᴋᴇɢʙᴀɴ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜰᴀᴋᴇɢʙᴀɴ ᴄᴇꜱꜱ 』</b>

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}fgban</code> [ʙᴀʟᴀꜱ ᴋᴇ ᴘᴇꜱᴀɴ] [ᴀʟᴀꜱᴀɴ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴀᴋꜱɪ ꜰᴀᴋᴇ ɢʟᴏʙᴀʟ ʙᴀɴɴᴇᴅ (ʜᴀɴʏᴀ ᴘᴜʀᴀ-ᴘᴜʀᴀ, ʙᴜᴋᴀɴ ʙᴇɴᴀʀᴀɴ)
...</blockquote>
"""

DEFAULTUSER = str(getattr(Var, "ALIVE_NAME", None) or platform.node())

@PY.UBOT(["fgban"])
async def _(c, m: Message):
    reason = m.text.split(None, 1)[1] if len(m.command) > 1 else None
    await m.reply("<b>ꜱᴜᴍᴍᴏɴɪɴɢ ᴏᴜᴛ ᴛʜᴇ ᴍɪɢʜᴛʏ ɢʙᴀɴ ʜᴀᴍᴍᴇʀ ☠️</b>")
    await asyncio.sleep(2)
    if m.reply_to_message:
        reply_message = m.reply_to_message
        user = reply_message.from_user
        if user.id == 1036951071:
            await reply_message.reply(
                "<b>ᴡᴀɪᴛ ᴀ sᴇᴄᴏɴᴅ, ᴛʜɪs ɪs ᴍʏ ᴍᴀsᴛᴇʀ!<br>ʜᴏᴡ ᴅᴀʀᴇ ʏᴏᴜ ᴛʜʀᴇᴀᴛᴇɴ ᴛᴏ ɢʙᴀɴ ᴍʏ ᴍᴀsᴛᴇʀ!<br>ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ɪs ɪɴᴠɪɴᴄɪʙʟᴇ.</b>"
            )
            return
        jnl = (
            f"<b>ᴡᴀʀɴɪɴɢ!!</b> <a href='tg://user?id={user.id}'>{user.first_name}</a> "
            f"<b> ɢʙᴀɴɴᴇᴅ ʙʏ</b> {DEFAULTUSER}<br>"
            f"<b>ɴᴀᴍᴀ:</b> {user.first_name}<br>"
            f"<b>ID:</b> <code>{user.id}</code><br>"
        )
        if user.username:
            jnl += f"<b>ᴜsᴇʀɴᴀᴍᴇ:</b> @{user.username}<br>"
        else:
            jnl += "<b>ᴜsᴇʀɴᴀᴍᴇ:</b> `ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴜsᴇʀɴᴀᴍᴇ`<br>"
        if reason:
            jnl += f"<b>ᴀʟᴀsᴀɴ:</b> {reason}"
        else:
            jnl += "<b>ᴀʟᴀsᴀɴ:</b> `ᴊᴀᴍᴇᴛ`"
        await reply_message.reply(jnl)
    else:
        mention = f"<b>ᴡᴀʀɴɪɴɢ!! ᴜsᴇʀ ɢʙᴀɴɴᴇᴅ ʙʏ {DEFAULTUSER}<br>ᴀʟᴀsᴀɴ:</b> `ᴊᴀᴍᴇᴛ`"
        await m.reply(mention)
    await m.delete()
