from asyncio.exceptions import TimeoutError
from pyrogram.errors import FloodWait
from PyroUbot import *

__MODULE__ = "PDF"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ PDF ᴄᴇꜱꜱ 』</b>

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}pdf</code> [ʙᴀʟᴀꜱ ᴋᴇ ᴛᴇᴋꜱ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴɢᴜʙᴀʜ ᴛᴇᴋꜱ ᴍᴇɴᴊᴀᴅɪ ꜰɪʟᴇ PDF ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ @office2pdf_bot.
</blockquote>
"""

@PY.UBOT("pdf")
async def _(c, m):
    if not m.reply_to_message:
        return await m.reply("<b>ꜱɪʟᴀᴋᴀɴ ʙᴀʟᴀꜱ ᴋᴇ ᴘᴇꜱᴀɴ ᴛᴇᴋꜱ ᴀᴘᴀ ᴘᴜɴ ᴄᴜᴋɪ!</b>")
    reply_message = m.reply_to_message
    chat = "@office2pdf_bot"
    pesan_proses = await m.reply("<b>ᴍᴇɴɢᴜʙᴀʜ ᴍᴇɴᴊᴀᴅɪ PDF ᴄᴇꜱꜱ...</b>")
    try:
        async with c.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("/start")
                response = await conv.get_response()
                msg = await conv.send_message(reply_message)
                convert = await conv.send_message("/ready2conv")
                cnfrm = await conv.get_response()
                editfilename = await conv.send_message("Yes")
                enterfilename = await conv.get_response()
                filename = await conv.send_message("PYRO UBOT")
                started = await conv.get_response()
                pdf = await conv.get_response()
                await c.send_read_action(conv.chat_id, "typing")
            except Exception:
                await pesan_proses.edit("<b>ᴜɴʙʟᴏᴄᴋ @office2pdf_bot ᴅᴀɴ ᴄᴏʙᴀ ʟᴀɢɪ ᴄᴜᴋɪ.</b>")
                return
        await m.reply_document(pdf.document)
        await c.delete_messages(
            conv.chat_id,
            [
                msg_start.id,
                response.id,
                msg.id,
                started.id,
                filename.id,
                editfilename.id,
                enterfilename.id,
                cnfrm.id,
                pdf.id,
                convert.id,
            ],
        )
        await pesan_proses.delete()
    except TimeoutError:
        return await pesan_proses.edit(
            "<b>ERROR: @office2pdf_bot ᴛɪᴅᴀᴋ ᴍᴇʀᴇꜱᴘᴏɴ ᴄᴜᴋɪ, ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ ᴄᴇꜱꜱ.</b>"
        )
