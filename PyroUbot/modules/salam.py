import asyncio
from time import sleep
from PyroUbot import *

__MODULE__ = "salam"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴀʟᴀᴍ ᴄᴇss 』</b>

• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}ᴘ</code>
• <b>ᴘᴇɴᴊᴇʟᴀsᴀɴ : ᴀssᴀʟᴀᴍᴜ'ᴀʟᴀɪᴋᴜᴍ.</b>

• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}ᴘᴇ</code>
• <b>ᴘᴇɴᴊᴇʟᴀsᴀɴ : ᴀssᴀʟᴀᴍᴜ'ᴀʟᴀɪᴋᴜᴍ ᴡᴀʀᴀʜᴍᴀᴛᴜʟʟᴀʜɪ ᴡᴀʙᴀʀᴀᴋᴀᴛᴜʜ.</b>

• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}ʟ</code>
• <b>ᴘᴇɴᴊᴇʟᴀsᴀɴ : ᴡᴀ'ᴀʟᴀɪᴋᴜᴍsᴀʟᴀᴍ.</b>

• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}ᴡʟ</code>
• <b>ᴘᴇɴᴊᴇʟᴀsᴀɴ : ᴡᴀ'ᴀʟᴀɪᴋᴜᴍsᴀʟᴀᴍ ᴡᴀʀᴀʜᴍᴀᴛᴜʟʟᴀʜɪ ᴡᴀʙᴀʀᴀᴋᴀᴛᴜʜ.</b>

• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}ᴀs</code>
• <b>ᴘᴇɴᴊᴇʟᴀsᴀɴ : ᴄᴏʙᴀ ᴀᴊᴀ ᴄᴇss.</b></blockquote>
"""


@PY.UBOT("p")
async def inijugajangandiapusataudigantikrnizzyganteng(client, message):
    await message.edit(
        "Assalamu'alaikum",
    )


@PY.UBOT("pe")
async def biarpanjangajayangpentingizzyganteng(client, message):
    await message.edit(
        "Assalamualaikum Warahmatullahi Wabarakatuh",
    )


@PY.UBOT("l")
async def biarmampuslusemuakontol(client, message):
    await message.edit(
        "Waalaikumsalam",
    )


@PY.UBOT("wl")
async def ularnagapanajnagnyabukankepalangtapiizzygantengamat(client, message):
    await message.edit(
        "Wa'alaikumsalam Warahmatullahi Wabarakatuh",
    )


@PY.UBOT("as")
async def pelerpelerpeler(client, message):
    await message.edit(
        "Salam dulu woy!",
    )
