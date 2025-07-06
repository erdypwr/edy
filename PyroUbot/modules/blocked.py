from PyroUbot import *
from pyrogram.raw.functions.contacts import GetBlocked

__MODULE__ = "ʙʟᴏᴄᴋᴇᴅ"
__HELP__ = """
<blockquote><b>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙʟᴏᴄᴋᴇᴅ

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}unblockall</code>
    ᴍᴇɴɢ ᴜɴʙʟᴏᴄᴋ ꜱᴇᴍᴜᴀ ᴜꜱᴇʀ ᴅɪ ᴅᴀꜰᴛᴀʀ ᴄᴏɴᴛᴀᴄᴛ

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}getblock</code>
    ᴍᴇʟɪʜᴀᴛ ᴊᴜᴍʟᴀʜ ʏᴀɴɢ ᴅɪ ʙʟᴏᴄᴋɪʀ ᴅɪ ᴄᴏɴᴛᴀᴄᴛ</b></blockquote>
"""

@PY.UBOT("unblockall")
async def _(user, message):
    sks = await EMO.BERHASIL(user)
    prs = await EMO.PROSES(user)
    _prs = await message.reply(f"{prs}ꜱᴇᴅᴀɴɢ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴜɴʙʟᴏᴄᴋᴀʟʟ...")
    mecha = await user.invoke(GetBlocked(offset=0, limit=100))
    user_ids = [entry.peer_id.user_id for entry in mecha.blocked]
    for x in user_ids:
        try:
            await user.unblock_user(x)
        except:
            pass
    await _prs.edit(f"{sks}ʙᴇʀʜᴀꜱɪʟ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴜɴʙʟᴏᴄᴋᴀʟʟ ᴜꜱᴇʀꜱ")

@PY.UBOT("getblock")
async def _(user, message):
    prs = await EMO.PROSES(user)
    _prs = await message.reply(f"{prs}ꜱᴇᴅᴀɴɢ ᴍᴇɴɢᴇᴄᴇᴋ ᴄᴇꜱꜱ...")
    mecha = await user.invoke(GetBlocked(offset=0, limit=100))
    user_ids = [entry.peer_id.user_id for entry in mecha.blocked]
    teko = len(user_ids)
    if user_ids:
        try:
            await _prs.edit(f"ᴋᴀᴍᴜ ᴍᴇᴍʙʟᴏᴄᴋɪʀ : {teko} ᴜꜱᴇʀꜱ")
        except Exception as i:
            await _prs.edit(f"{i}")
    else:
        await _prs.edit(f"ᴛɪᴅᴀᴋ ᴀᴅᴀ ʏᴀɴɢ ᴅɪ ʙʟᴏᴄᴋɪʀ ᴄᴇꜱꜱ")
