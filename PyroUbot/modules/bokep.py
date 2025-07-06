import random
from pyrogram.enums import MessagesFilter
from PyroUbot import *


__MODULE__ = "ʙᴏᴋᴇx ʙɪᴀsᴇ"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙᴏᴋᴇᴘ ʙɪᴀꜱᴇ 』</b>

<blockquote><b>ᴘᴇʀɪɴᴛᴀʜ :
<code>{0}bokep</code>
ꜰɪᴛᴜʀ ʙᴏᴋᴇᴘ ʏᴀ</b></blockquote>
"""

@PY.UBOT("bokep")
async def _(client, message):
    y = await message.reply_text(f"<blockquote><b>**ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ʙᴏᴋᴇᴘ ᴅᴜʟᴜ ᴄᴇꜱꜱ...**</b></blockquote>", quote=True)
    try:
        await client.join_chat("https://t.me/+kJJqN5kUQbs1NTVl")
    except:
        pass
    try:
        bokepnya = []
        async for bokep in client.search_messages(
            -1001867672427, filter=MessagesFilter.VIDEO
        ):
            bokepnya.append(bokep)
        video = random.choice(bokepnya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)
    if client.me.id == OWNER_ID:
        return
    await client.leave_chat(-1001867672427)
