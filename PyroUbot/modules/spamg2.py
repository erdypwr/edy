import asyncio

from pyrogram.errors import FloodWait

from PyroUbot import *
import monggo

spam_taksdb = {}

kontol = False

__MODULE__ = "ꜱᴘᴀᴍ 2"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱᴘᴀᴍ 2 ᴄᴇꜱꜱ 』<b>

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ꜱᴅꜱᴘᴍ</code> [ᴡᴀᴋᴛᴜ] [ʙᴀʟᴀꜱ ᴋᴇ ᴘᴇꜱᴀɴ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇᴍᴜʟᴀɪ ꜱᴘᴀᴍ ᴋᴇ ᴅᴀᴛᴀʙᴀꜱᴇ.

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ꜱᴛᴅꜱᴘᴍ</code>
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴɢʜᴇɴᴛɪᴋᴀɴ ᴘʀᴏꜱᴇꜱ ꜱᴘᴀᴍ ᴅɪᴅᴀᴛᴀʙᴀꜱᴇ.

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ʟɪꜱᴛꜱᴘᴍ</code> 
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇʟɪʜᴀᴛ ᴅᴀғᴛᴀʀ ɢʀᴜᴘ ᴅɪᴅᴀʟᴀᴍ ᴅᴀᴛᴀʙᴀꜱᴇ.

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ᴀᴅᴅꜱᴘᴍ</code> 
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ɢʀᴜᴘ ᴋᴇ ᴅᴀʟᴀᴍ ᴅᴀᴛᴀʙᴀꜱᴇ ꜱᴘᴀᴍ.

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ᴅᴇʟꜱᴘᴍ</code> 
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴɢʜᴀᴘᴜꜱ ɢʀᴜᴘ ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀꜱᴇ ꜱᴘᴀᴍ.</b></blockquote><b>
"""


@PY.UBOT("sdspm")
async def _(c, m):
    global kontol

    if not m.reply_to_message:
        return await m.reply("<b>ꜱɪʟᴀᴋᴀɴ ʙᴀʟᴀꜱ ᴋᴇ ᴘᴇꜱᴀɴ !!</b>")
    if len(m.command) != 2:
        return await m.reply("<b>ꜱɪʟᴀʜᴋᴀɴ ʙᴀʟᴀꜱ ᴋᴇ ᴘᴇꜱᴀɴ ᴅᴀɴ ʙᴇʀɪᴋᴀɴ ᴡᴀᴋᴛᴜ ᴅᴇʟᴀʏ.</b>")
    try:
        interval = int(m.command[1])
    except ValueError:
        return await m.reply("<b>ᴡᴀᴋᴛᴜ ᴅᴇʟᴀʏ ʜᴀʀᴜꜱ ʙᴇʀᴜᴘᴀ ᴀɴɢᴋᴀ.</b>")

    scheduled_message = m.reply_to_message
    chat_ids = monggo.ambil_spdb(c.me.id)
    kontol = True
    for chat_id in chat_ids:
        if not kontol:
            break
        if interval < 10:
            await m.reply(
                f"<b>ᴍɪɴɪᴍᴀʟ ᴡᴀᴋᴛᴜ ᴅᴇʟᴀʏ 10 ᴊᴀɴɢᴀɴ  <code>{interval}</code></b>"
            )
        else:

            async def send_scheduled_message(chat_id):
                try:
                    while True:
                        await asyncio.sleep(interval)
                        await scheduled_message.copy(chat_id)
                except FloodWait:
                    if chat_id in spam_taksdb:
                        task = spam_taksdb[chat_id]
                        task.cancel()
                        del spam_taksdb[chat_id]

            task = asyncio.create_task(send_scheduled_message(chat_id))
            spam_taksdb[chat_id] = task
    kontol = False
    await m.reply(f"<b>ᴘʀᴏꜱᴇꜱ ꜱᴘᴀᴍ ᴋᴇ ᴅᴀᴛᴀʙᴀꜱᴇ !</b>")


@PY.UBOT("stdspm")
async def _(c, m):
    global kontol
    if not kontol:
        return await m.reply_text(
            "<b>ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇɴɢɪʀɪᴍᴀɴ ꜱᴘᴀᴍ ʏᴀɴɢ ꜱᴇᴅᴀɴɢ ʙᴇʀʟᴀɴɢꜱᴜɴɢ.</b>"
        )
    chat_ids = monggo.ambil_spdb(c.me.id)
    for chat_id in chat_ids:
        if chat_id in spam_taksdb:
            task = spam_taksdb[chat_id]
            task.cancel()
            del spam_taksdb[chat_id]
    kontol = False
    await m.reply("<b>ꜱᴘᴀᴍ ᴅᴀᴛᴀʙᴀꜱᴇ ᴅɪʜᴇɴᴛɪᴋᴀɴ.</b>")


@PY.UBOT("listspm")
async def _(c, m):
    teks = "<b>ᴅᴀꜰᴛᴀʀ ᴅᴀᴛᴀʙᴀꜱᴇ ꜱᴘᴀᴍ:</b>\n\n"
    user_id = c.me.id
    lists = monggo.ambil_spdb(user_id)
    if len(lists) == 0:
        await m.reply("<b>ᴅᴀᴛᴀʙᴀꜱᴇ ᴋᴏꜱᴏɴɢ.</b>")
    else:
        for count, chat_id in enumerate(lists, 1):
            teks += f"{count}. <code>{chat_id}</code>\n"
        await m.reply(teks)


@PY.UBOT("addspm|delspm")
async def _(c, m):
    user_id = c.me.id
    chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
    mmk = await m.reply("<b>ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...</b>")
    if m.command[0] == "addspm":
        monggo.tambah_spdb(user_id, chat_id)
        return await mmk.edit(
            f"<code>{chat_id}</code> <b>ʙᴇʀʜᴀꜱɪʟ ᴅɪ ᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴅᴀᴛᴀʙᴀꜱᴇ.</b>"
        )
    elif m.command[0] == "delspm":
        monggo.kureng_spdb(user_id, chat_id)
        return await mmk.edit(
            f"<code>{chat_id}</code> <b>ʙᴇʀʜᴀꜱɪʟ ᴅɪ ʜᴀᴘᴜꜱ ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀꜱᴇ.</b>"
        )
    else:
        return await mmk.edit(f"<b>ꜱɪʟᴀᴋᴀɴ ᴋᴇᴛɪᴋ <code>{m.text}.</code></b>")
