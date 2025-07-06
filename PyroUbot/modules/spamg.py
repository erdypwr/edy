import asyncio

from pyrogram.enums import ChatType
from pyrogram.errors import FloodWait

from .. import *
from PyroUbot import *

__MODULE__ = "ꜱᴘᴀᴍ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱᴘᴀᴍ ᴄᴇꜱꜱ 』</b>

<b>ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}spam</code>
   <code>ᴍᴇʟᴀᴋᴜᴋᴀɴ ꜱᴘᴀᴍ ᴘᴇꜱᴀɴ</code>

<b>ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}setdelay</code>
   <code>ᴍᴇɴɢᴀᴛᴜʀ ᴅᴇʟᴀʏ sᴇᴛɪᴀᴘ ᴘᴇsᴀɴ ʏᴀɴɢ ᴅɪ ᴋɪʀɪᴍ</code>

<b>ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}stopspam</code>
   <code>ᴍᴇᴍʙᴇʀʜᴇɴᴛɪᴋᴀɴ ꜱᴘᴀᴍ ᴘᴇꜱᴀɴ ʏᴀɴɢ sᴇᴅᴀɴɢ ʙᴇʀᴊᴀʟᴀɴ</code></blockquote>
"""

spam_progress = []

async def SpamMsg(client, message, send):
    delay = await get_vars(client.me.id, "SPAM") or 0
    await asyncio.sleep(int(delay))
    if message.reply_to_message:
        await send.copy(message.chat.id)
    else:
        await client.send_message(message.chat.id, send)

@PY.UBOT("spam")
@PY.TOP_CMD
async def _(client, message):
    global spam_progress
    spam_progress.append(client.me.id)
    sks = await EMO.BERHASIL(client)
    _msg = "<b>ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...</b>"

    r = await message.reply(_msg)
    count, msg = extract_type_and_msg(message)

    try:
        count = int(count)
    except Exception:
        return await r.edit(f"<b><code>{message.text.split()[0]}</code> [jumlah] [text/reply_msg]</b>")

    if not msg:
        return await r.edit(
            f"<b><code>{message.text.split()[0]}</code> [jumlah] [text/reply_msg]</b>"
        )
    
    for _ in range(count):
        if client.me.id not in spam_progress:
            await r.edit(f"<blockquote><b>Proses Spam Berhasil Di Batalkan Cess !</b> {sks}</blockquote>")
            return
        await SpamMsg(client, message, msg)

    spam_progress.remove(client.me.id)    
    await r.edit("<b>Spam Telah Selesai Cess</b>")

@PY.UBOT("setdelay")
@PY.TOP_CMD
async def _(client, message):
    _msg = "<b>ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...</b>"

    r = await message.reply(_msg)
    count, msg = extract_type_and_msg(message)

    try:
        count = int(count)
    except Exception:
        return await r.edit(f"<b><code>{message.text.split()[0]}</code> [count]</b>")

    if not count:
        return await r.edit(f"<b><code>{message.text.split()[0]}</code> [count]</b>")

    await set_vars(client.me.id, "SPAM", count)
    return await r.edit("<b>Spam Delay Berhasil Di Setting Cess</b>")

@PY.UBOT("stopspam")
@PY.TOP_CMD
async def _(client, message):
    global spam_progress
    if client.me.id in spam_progress:
        spam_progress.remove(client.me.id)
        await message.reply("<b>Spam Telah Berhenti Cess</b>")
    else:
        await message.reply("<b>Tidak Ada Spam Yang Ditemukan Cess</b>")
