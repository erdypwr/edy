import asyncio
from time import sleep
from PyroUbot import *

__MODULE__ = "ᴛᴏxɪᴄ"
__HELP__ = """
 <blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴏxɪᴄ ᴄᴇꜱꜱ 』</b>

• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}jamet</code>
• <b>ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ɢᴀᴛᴀᴜ ɢᴀʙᴜᴛ ᴅᴏᴀɴɢ.</b>

• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}vir</code>
• <b>ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ɢᴀᴛᴀᴜ ɢᴀʙᴜᴛ ᴅᴏᴀɴɢ.</b>

• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}ppx</code>
• <b>ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ɢᴀᴛᴀᴜ ɢᴀʙᴜᴛ ᴅᴏᴀɴɢ.</b>

• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}kiss</code>
• <b>ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ɢᴀᴛᴀᴜ ɢᴀʙᴜᴛ ᴅᴏᴀɴɢ.</b>

• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}pc</code>
• <b>ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ɢᴀᴛᴀᴜ ɢᴀʙᴜᴛ ᴅᴏᴀɴɢ.</b>

• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}hah</code>
• <b>ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ɢᴀᴛᴀᴜ ɢᴀʙᴜᴛ ᴅᴏᴀɴɢ.</b>

• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}gembel</code>
• <b>ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ɢᴀᴛᴀᴜ ɢᴀʙᴜᴛ ᴅᴏᴀɴɢ.

• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}marah</code>
• <b>ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ɢᴀᴛᴀᴜ ɢᴀʙᴜᴛ ᴅᴏᴀɴɢ.</b>

• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}cuki</code>
• <b>ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ɢᴀᴛᴀᴜ ɢᴀʙᴜᴛ ᴅᴏᴀɴɢ.</b></blockquote>

"""

@PY.UBOT("jamet")
async def bulan(client, message):
    animation_interval = 0.2
    animation_ttl = range(96)
    await message.edit("ᴡᴏɪɪ..")
    animation_chars = [
        "ʟᴜ ʏᴀɴɢ ʀᴜꜱᴜʜ ꜱᴀɴᴀʜ ꜱɪɴɪʜ?",
        "ɴɪ ɢᴡ ʙɪʟᴀɴɢɪɴ ʏᴀ",
        "ɢᴀᴜꜱᴀʜ ꜱᴏ ᴀꜱɪᴋ",
        "ᴇᴍᴀɴɢ ʟᴜ ᴛᴇʀᴋᴇɴᴀʟ?",
        "ᴄᴜᴍᴀ ᴋᴀᴄᴜɴɢ ᴅɪ ʀᴇᴀʟ ꜱᴏᴋ ᴍᴀᴜ ʀᴜꜱᴜʜ",
        "ᴏʀᴀɴɢ ʏᴀɴɢ ᴋᴀʏᴀ ʟᴜ ɴɪ ʜᴀʀᴜꜱ ɢᴡ ᴋᴀᴛᴀɪɴ",
        "ᴊᴀɴɢᴀɴ ꜱᴏᴋ ᴛɪɴɢɢɪ ᴅɪ ᴛᴇʟᴇɢʀᴀᴍ ʙɢꜱᴛᴛ",
        "ʙᴏᴄᴀʜ ᴋᴀᴍᴘᴜɴɢ",
        "ᴛʜᴏʟᴏʟ ᴋᴀʟᴀᴜ ʟᴜ ᴍᴀᴜ ʀᴜꜱᴜʜ ᴊᴀɴɢᴀɴ ᴅɪꜱɪɴɪ ᴛʜᴏʟᴏʟ",
        "ᴍᴇɴᴅɪɴɢ ʟᴜ ʙᴀɴᴛᴜ ᴍᴀᴋ ʟᴜ ꜱᴏɴᴏ, ᴅᴀʀɪ ᴘᴀᴅᴀ ɢᴀ ᴀᴅᴀ ᴋᴇʀᴊᴀᴀɴ",]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 32])


@PY.UBOT("vir")
async def izzyganteng(client, message):
    e = await message.edit("ᴏᴏᴏᴏ")
    await e.edit("ɪɴɪ ʏᴀɴɢ ᴠɪʀᴛᴜᴀʟ")
    await e.edit("ʏᴀɴɢ ᴋᴀᴛᴀɴʏᴀ ꜱᴀʏᴀɴɢ ʙᴀɴɢᴇᴛ")
    await e.edit("ᴛᴀᴘɪ ᴛᴇᴛᴇᴘ ᴀᴊᴀ ᴅɪ ᴛɪɴɢɢᴀʟ")
    await e.edit("ɴɪ ɪɴɢᴇᴛ")
    await e.edit("ᴛᴀɴɢᴀɴɴʏᴀ ᴀᴊᴀ ɢᴀ ʙɪꜱᴀ ᴅɪ ᴘᴇɢᴀɴɢ")
    await e.edit("ᴀᴘᴀʟᴀɢɪ ᴋᴇᴍᴀʟᴜᴀɴ ɴʏᴀ")
    await e.edit("ʙʜᴀʜᴀʜᴀʜᴀ")
    await e.edit("ᴋᴀꜱɪᴀɴ ʙᴀʜᴀʜᴀʜᴀ ɢʙʟᴏᴋ ᴍᴋɴ ᴛᴜʜ ᴠɪʀᴛᴜᴀʟ")


@PY.UBOT("ppx")
async def izzygantengbgt(client, message):
    typew = await message.edit("`ᴏɪ ᴘᴘᴋᴋ ʟᴜ ᴋᴀʟᴀᴜ ᴍᴀᴜ ɴɪᴍʙʀᴜɴɢ, ɴɪᴍʙʀᴜɴɢ ᴀᴊᴀ ɢᴏʙʟᴏᴋᴋᴋ ᴊɢɴ ʀᴜꜱᴜʜʜ ᴅɪꜱɪɴɪɪ ᴛʜᴏʟᴏʟ!!`")


@PY.UBOT("kiss")
async def izzyemangganteng(client, message):
    e = await message.edit("`ᴄᴜɪʜʜʜʜ, ɴɪʜ ɢᴡ ᴄɪᴜᴍ ᴘᴀʟᴀ ᴏᴛᴀᴋ ᴋᴀᴜ, ᴋᴀᴜ ᴘᴜɴʏᴀ ᴏᴛᴀᴋ ɢᴀ ɢʙʟᴋᴋ!!`")


@PY.UBOT("pc")
async def izzypalingganteng(client, message):
    typew = await message.edit("`ᴇʜ ᴘᴀɴᴛᴇx, ʟᴜ ᴘᴄ ɢᴡ ʟᴀɢɪ, ɢᴡ ᴛᴀʙᴏᴋ ᴘᴀʟᴀ ʟᴜ ᴛɪɴɢɢᴀʟ ᴛᴜʟᴀɴɢ!`")


# ᴄʀᴇᴀᴛᴇ ʙʏ ᴍʏꜱᴇʟꜰ @ʙᴏʏꜱᴢ


@PY.UBOT("hah")
async def izzygantengsekali(client, message):
    await message.edit( "`ᴇᴍᴀɴɢ ᴋɪᴛᴀ ᴋᴇɴᴀʟ? ᴋᴀɢᴀ ɢᴏʙʟᴏᴋ ꜱᴏᴋᴀʙ ʙᴀɴɢᴇᴛ ʟᴜ ɢᴏʙʟᴏᴋ!!`")


@PY.UBOT("gembel")
async def izzyemangpalingganteng(client, message):
    animation_chars = [
            "`ᴍᴜᴋᴀ ʙᴀᴘᴀᴋ ʟᴜ ᴋᴇᴋ ᴋᴇʟᴀᴘᴀ ꜱᴀᴡɪᴛ ᴀɴᴊɪɴɢ, ɢᴀ ᴜꜱᴀʜ ɴɢᴀᴛᴀɪɴ ᴏʀᴀɴɢ, ᴍᴜᴋᴀ ʟᴜ ᴀᴊᴀ ᴋᴇᴋ ɢᴇᴍʙᴇʟ ᴛᴇxᴀꜱ ɢᴏʙʟᴏᴋ!!`",
    ]
    animation_interval = 2
    animation_ttl = range(11)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 11])

@PY.UBOT("marah")
async def perintah_marah(client, message):
    await message.edit("`ɢᴡ ʟᴀɢɪ ᴍᴀʀᴀʜ ᴄᴜᴋɪ, ᴊᴀɴɢᴀɴ ɢᴀɴɢɢᴜ ɢᴡ!`")

@PY.UBOT("cuki")
async def perintah_salam(client, message):
    await message.edit("`ᴄᴜᴋɪ ʙᴇᴛᴜʟ ᴇʟᴜ ᴋᴏɴᴛᴏʟ ᴜᴅᴀʜ ʙᴇʟᴜᴍ ᴍᴀɴᴅɪ ꜱᴇᴛᴀʜᴜɴ ᴀᴇ ꜱᴜᴅᴀʜ ʙᴇɢᴀʏᴀ!`")
