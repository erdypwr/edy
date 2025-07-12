# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinChannel
# ========================×========================
# Jangan Hapus Credit Ngentod
# ========================×========================
import asyncio
import cv2
import io
import os
import requests
from PyroUbot import *
from config import Var

__MODULE__ = "ɢᴀᴍʙᴀʀ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴀᴍʙᴀʀ ᴄᴇꜱꜱ 』</b>

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}rbg</code> [ʙᴀʟᴀꜱ ɢᴀᴍʙᴀʀ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴɢʜᴀᴘᴜꜱ ʟᴀᴛᴀʀ ʙᴇʟᴀᴋᴀɴɢ ɢᴀᴍʙᴀʀ (ʀᴇǫ: ᴀᴘɪ ᴋᴇʏ ʀᴇᴍᴏᴠᴇ.ʙɢ)

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}blur</code> [ʙᴀʟᴀꜱ ɢᴀᴍʙᴀʀ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇᴍʙᴇʀɪᴋᴀɴ ᴇꜰᴇᴋ ʙʟᴜʀ ᴋᴇ ɢᴀᴍʙᴀʀ

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}negatif</code> [ʙᴀʟᴀꜱ ɢᴀᴍʙᴀʀ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇᴍʙᴇʀɪᴋᴀɴ ᴇꜰᴇᴋ ɴᴇɢᴀᴛɪꜰ ᴋᴇ ɢᴀᴍʙᴀʀ

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}miror</code> [ʙᴀʟᴀꜱ ɢᴀᴍʙᴀʀ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇᴍʙᴇʀɪᴋᴀɴ ᴇꜰᴇᴋ ᴄᴇʀᴍɪɴ ᴋᴇ ɢᴀᴍʙᴀʀ
</blockquote>
"""

def get_temp_dir():
    return getattr(Var, "TEMP_DOWNLOAD_DIRECTORY", "./")

def get_rembg_key():
    return getattr(Var, "REM_BG_API_KEY", None)

@PY.UBOT(["rbg", "removebg", "remove_bg"])
async def _(c, m):
    api_key = get_rembg_key()
    if not api_key:
        return await m.reply("<b>ᴇʀʀᴏʀ: ᴀᴘɪ ᴋᴇʏ ʀᴇᴍᴏᴠᴇ.ʙɢ ʙᴇʟᴜᴍ ᴅɪꜱᴇᴛ!</b>")
    if not m.reply_to_message or not m.reply_to_message.media:
        return await m.reply("<b>ʙᴀʟᴀꜱ ɢᴀᴍʙᴀʀ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪʜᴀᴘᴜꜱ ʙᴀᴄᴋɢʀᴏᴜɴᴅɴʏᴀ ᴄᴜᴋɪ!</b>")
    proses = await m.reply("<b>ᴘʀᴏꜱᴇꜱ ʜᴀᴘᴜꜱ ʙᴀᴄᴋɢʀᴏᴜɴᴅ ᴄᴇꜱꜱ...</b>")
    temp_dir = get_temp_dir()
    file_path = await c.download_media(m.reply_to_message, temp_dir)
    with open(file_path, "rb") as img_file:
        response = requests.post(
            "https://api.remove.bg/v1.0/removebg",
            headers={"X-API-Key": api_key},
            files={"image_file": img_file},
            stream=True,
        )
    os.remove(file_path)
    if response.status_code == 200:
        with io.BytesIO(response.content) as out_img:
            out_img.name = "no_bg.png"
            await m.reply_document(out_img, caption="<b>ʙᴀᴄᴋɢʀᴏᴜɴᴅ ᴛᴇʟᴀʜ ᴅɪʜᴀᴘᴜꜱ ᴄᴇꜱꜱ!</b>")
    else:
        await proses.edit(f"<b>ᴇʀʀᴏʀ: {response.content.decode('utf-8')}</b>")
        return
    await proses.delete()

@PY.UBOT(["blur"])
async def _(c, m):
    if not m.reply_to_message or not m.reply_to_message.media:
        return await m.reply("<b>ʙᴀʟᴀꜱ ɢᴀᴍʙᴀʀ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪʙʟᴜʀ ᴄᴜᴋɪ!</b>")
    proses = await m.reply("<b>ᴘʀᴏꜱᴇꜱ ʙʟᴜʀ ɢᴀᴍʙᴀʀ ᴄᴇꜱꜱ...</b>")
    temp_dir = get_temp_dir()
    file_path = await c.download_media(m.reply_to_message, temp_dir)
    img = cv2.imread(file_path)
    blur_img = cv2.GaussianBlur(img, (35, 35), 0)
    cv2.imwrite("blurred.png", blur_img)
    await m.reply_photo("blurred.png")
    await proses.delete()
    os.remove("blurred.png")
    os.remove(file_path)

@PY.UBOT(["negatif"])
async def _(c, m):
    if not m.reply_to_message or not m.reply_to_message.media:
        return await m.reply("<b>ʙᴀʟᴀꜱ ɢᴀᴍʙᴀʀ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪɴᴇɢᴀᴛɪꜰᴋᴀɴ ᴄᴜᴋɪ!</b>")
    proses = await m.reply("<b>ᴘʀᴏꜱᴇꜱ ɴᴇɢᴀᴛɪꜰ ɢᴀᴍʙᴀʀ ᴄᴇꜱꜱ...</b>")
    temp_dir = get_temp_dir()
    file_path = await c.download_media(m.reply_to_message, temp_dir)
    img = cv2.imread(file_path)
    neg_img = cv2.bitwise_not(img)
    cv2.imwrite("negative.png", neg_img)
    await m.reply_photo("negative.png")
    await proses.delete()
    os.remove("negative.png")
    os.remove(file_path)

@PY.UBOT(["miror"])
async def _(c, m):
    if not m.reply_to_message or not m.reply_to_message.media:
        return await m.reply("<b>ʙᴀʟᴀꜱ ɢᴀᴍʙᴀʀ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪᴄᴇʀᴍɪɴᴋᴀɴ ᴄᴜᴋɪ!</b>")
    proses = await m.reply("<b>ᴘʀᴏꜱᴇꜱ ᴄᴇʀᴍɪɴ ɢᴀᴍʙᴀʀ ᴄᴇꜱꜱ...</b>")
    temp_dir = get_temp_dir()
    file_path = await c.download_media(m.reply_to_message, temp_dir)
    img = cv2.imread(file_path)
    mirror_img = cv2.flip(img, 1)
    concat_img = cv2.hconcat([img, mirror_img])
    cv2.imwrite("mirrored.png", concat_img)
    await m.reply_photo("mirrored.png")
    await proses.delete()
    os.remove("mirrored.png")
    os.remove(file_path)
