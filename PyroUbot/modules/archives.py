from PyroUbot.core.helpers.tools import get_data_id
from PyroUbot import *
__MODULE__ = "ᴀʀᴄʜɪᴠᴇ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀʀᴄʜɪᴠᴇ ⦫<b>

<blockquote><b>⎆ ᴘᴇʀɪɴᴛᴀʜ :
ᚗ <code>{0}ᴀʀᴄʜ</code>
⊷ ᴍᴇɴɢᴀʀᴄʜɪᴠᴇᴋᴀɴ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ᴘʀɪʙᴀᴅɪ ᴍᴀᴜᴘᴜɴ ᴄʜᴀɴɴᴇʟ

ᚗ <code>{0}ᴜɴᴀʀᴄʜ</code>
⊷ ᴍᴇɴɢᴜɴᴀʀᴄʜɪᴠᴇᴋᴀɴ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ᴘʀɪʙᴀᴅɪ ᴍᴀᴜᴘᴜɴ ᴄʜᴀɴɴᴇʟ</b></blockquote>
"""
@PY.UBOT("arch")
@PY.TOP_CMD
async def archive_user(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if len(message.command) <2:
        return await message.reply(f"{ggl}ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ᴀʀᴄʜ ᴀʟʟ, ᴜꜱᴇʀꜱ, ɢʀᴏᴜᴘ")
    anjai = await message.reply(f"{prs}ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    anjir = message.command[1]
    xx = await get_data_id(client, anjir)
    for anu in xx:
        await client.archive_chats(anu)
    
    await anjai.edit(f"{brhsl}ʙᴇʀʜᴀꜱɪʟ ᴍᴇɴɢᴀʀᴄʜɪᴠᴇᴋᴀɴ ꜱᴇᴍᴜᴀ {anjir}")

@PY.UBOT("unarch")
@PY.TOP_CMD
async def unarchive_user(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if len(message.command) <2:
        return await message.reply(f"{ggl}ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ᴀʀᴄʜ ᴀʟʟ, ᴜꜱᴇʀꜱ, ɢʀᴏᴜᴘ")
    anjai = await message.reply(f"{prs}ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    anjir = message.command[1]
    xx = await get_data_id(client, anjir)
    for anu in xx:
        await client.unarchive_chats(anu)
    await anjai.edit(f"{brhsl}ʙᴇʀʜᴀꜱɪʟ ᴍᴇɴɢᴜɴᴀʀᴄʜɪᴠᴇᴋᴀɴ ꜱᴇᴍᴜᴀ {anjir}")
