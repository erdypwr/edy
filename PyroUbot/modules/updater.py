import os
import platform
import subprocess
import sys
import traceback
from datetime import datetime
from io import BytesIO, StringIO
from PyroUbot.config import OWNER_ID
import psutil
from PyroUbot import *


async def send_large_output(message, out):
    # Kirim output panjang sebagai file jika melebihi batas karakter Telegram
    with BytesIO(str(out).encode()) as file:
        file.name = "output.txt"
        await message.reply_document(document=file, caption="ᴏᴜᴛᴘᴜᴛ ᴛᴇʀʟᴀʟᴜ ᴘᴀɴᴊᴀɴɢ, ᴅɪᴋɪʀɪᴍ sᴇʙᴀɢᴀɪ ғɪʟᴇ.")

async def ngentod(client, message):
    out = subprocess.check_output(["git", "pull"]).decode("UTF-8")
    if "Already up to date." in str(out):
        return await message.reply(out, quote=True)
    elif int(len(str(out))) > 4096:
        await send_large_output(message, out)
    else:
        await message.reply(f"```{out}```", quote=True)
    os.execl(sys.executable, sys.executable, "-m", "PyroUbot")

@PY.BOT("update")
@PY.OWNER
async def _(c, m):
    await ngentod(c, m)


@PY.UBOT("update")
@PY.OWNER
async def _(c, m):
    await ngentod(c, m)