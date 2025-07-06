import asyncio
from time import sleep
from PyroUbot import *

__MODULE__ = "salam"
__HELP__ = """
 <blockquote><b>Bantuan Untuk salam Cess</b>

• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}p</code>
• <b>Penjelasan : Assalamu'alaikum.</b>

• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}pe</code>
• <b>Penjelasan : Assalamualaikum Warahmatullahi Wabarakatuh.</b>

• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}l</code>
• <b>Penjelasan : Wa'alaikumsalam.</b>

• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}wl</code>
• <b>Penjelasan : Wa'alaikumsalam Warahmatullahi Wabarakatuh.</b>

• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}as</code>
• <b>Penjelasan : Coba Aja Cess.</b></blockquote>

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
