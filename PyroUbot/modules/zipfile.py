import asyncio
import os
import time
import zipfile
from datetime import date
from PyroUbot import *

__MODULE__ = "ᴢɪᴘꜰɪʟᴇ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴢɪᴘꜰɪʟᴇ 』</b>

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}compress</code> [ʙᴀʟᴀꜱ ꜰɪʟᴇ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴɢᴄᴏᴍᴘʀᴇꜱꜱ ꜰɪʟᴇ ᴍᴇɴᴊᴀᴅɪ ᴢɪᴘ

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}addzip</code> [ʙᴀʟᴀꜱ ꜰɪʟᴇ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴᴀᴍʙᴀʜ ꜰɪʟᴇ ᴋᴇ ᴅᴀꜰᴛᴀʀ ᴢɪᴘ

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}upzip</code> [ɴᴀᴍᴀ ᴢɪᴘ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴɢᴜᴘʟᴏᴀᴅ ᴅᴀꜰᴛᴀʀ ᴢɪᴘ

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}rmzip</code>
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴɢʜᴀᴘᴜꜱ ᴅᴀꜰᴛᴀʀ ᴢɪᴘ
</blockquote>
"""

TEMP_DOWNLOAD_DIRECTORY = "./downloads/"
ZIP_DOWNLOAD_DIRECTORY = "./zips/"
today = date.today()

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), arcname=file)
            os.remove(os.path.join(root, file))

@PY.UBOT(["compress"])
async def _(c, m):
    if not m.reply_to_message or not m.reply_to_message.media:
        return await m.reply("<b>ʙᴀʟᴀꜱ ᴋᴇ ꜰɪʟᴇ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪᴄᴏᴍᴘʀᴇꜱꜱ!</b>")
    proses = await m.reply("<b>ᴍᴇɴɢᴜɴᴅᴜʜ ꜰɪʟᴇ...</b>")
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    c_time = time.time()
    file = await m.reply_to_message.download(file_name=TEMP_DOWNLOAD_DIRECTORY)
    await proses.edit(f"<b>ꜰɪʟᴇ ᴛᴇʀᴜɴᴅᴜʜ: <code>{file}</code>\nᴍᴇɴɢᴄᴏᴍᴘʀᴇꜱꜱ ꜰɪʟᴇ...</b>")
    zip_path = file + ".zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file, arcname=os.path.basename(file))
    await c.send_document(m.chat.id, zip_path, reply_to_message_id=m.id)
    await proses.edit("<b>ꜱᴇʟᴇꜱᴀɪ!</b>")
    os.remove(file)
    os.remove(zip_path)

@PY.UBOT(["addzip"])
async def _(c, m):
    if not m.reply_to_message or not m.reply_to_message.media:
        return await m.reply("<b>ʙᴀʟᴀꜱ ᴋᴇ ꜰɪʟᴇ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴅᴀꜰᴛᴀʀ ᴢɪᴘ!</b>")
    proses = await m.reply("<b>ᴍᴇɴɢᴜɴᴅᴜʜ ꜰɪʟᴇ...</b>")
    if not os.path.isdir(ZIP_DOWNLOAD_DIRECTORY):
        os.makedirs(ZIP_DOWNLOAD_DIRECTORY)
    file = await m.reply_to_message.download(file_name=ZIP_DOWNLOAD_DIRECTORY)
    await proses.edit(f"<b>{os.path.basename(file)} ʙᴇʀʜᴀꜱɪʟ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴅᴀꜰᴛᴀʀ ᴢɪᴘ</b>")

@PY.UBOT(["upzip"])
async def _(c, m):
    if not os.path.isdir(ZIP_DOWNLOAD_DIRECTORY):
        return await m.reply("<b>ᴅᴀꜰᴛᴀʀ ꜰɪʟᴇ ᴢɪᴘ ᴛɪᴅᴀᴋ ᴀᴅᴀ!</b>")
    proses = await m.reply("<b>ᴍᴇɴɢᴢɪᴘ ꜰɪʟᴇ...</b>")
    args = m.text.split(None, 1)
    curdate = today.strftime("%m%d%y")
    title = args[1] if len(args) > 1 else "zipfile" + f"{curdate}"
    zipf = zipfile.ZipFile(title + ".zip", "w", zipfile.ZIP_DEFLATED)
    zipdir(ZIP_DOWNLOAD_DIRECTORY, zipf)
    zipf.close()
    await c.send_document(m.chat.id, title + ".zip", reply_to_message_id=m.id)
    await proses.edit("<b>ᴢɪᴘ ᴛᴇʀᴋɪʀɪᴍ ᴅᴀɴ ᴅᴀꜰᴛᴀʀ ᴢɪᴘ ᴅɪʜᴀᴘᴜꜱ!</b>")
    os.remove(title + ".zip")
    try:
        os.rmdir(ZIP_DOWNLOAD_DIRECTORY)
    except Exception:
        pass

@PY.UBOT(["rmzip"])
async def _(c, m):
    if not os.path.isdir(ZIP_DOWNLOAD_DIRECTORY):
        return await m.reply("<b>ᴅɪʀᴇᴋᴛᴏʀɪ ᴢɪᴘ ᴛɪᴅᴀᴋ ᴀᴅᴀ!</b>")
    for root, dirs, files in os.walk(ZIP_DOWNLOAD_DIRECTORY):
        for file in files:
            os.remove(os.path.join(root, file))
    os.rmdir(ZIP_DOWNLOAD_DIRECTORY)
    await m.reply("<b>ᴅᴀꜰᴛᴀʀ ᴢɪᴘ ᴅɪʜᴀᴘᴜꜱ!</b>")
