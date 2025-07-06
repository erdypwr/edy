import os
import subprocess
from pyrogram import Client, filters
from PyroUbot import PY
import shutil
from pyrogram.types import Message

__MODULE__ = "ᴇɴᴄʀʏᴘᴛ ʜᴀʀᴅ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴇɴᴄʀʏᴘᴛ ᴊꜱ ᴄᴇꜱꜱ 』</b>

ᴘᴇʀɪɴᴛᴀʜ:
<code>{0}ᴇɴᴄ</code> → ʙᴀʟᴀꜱ ꜰɪʟᴇ .ᴊꜱ ᴜɴᴛᴜᴋ ᴅɪᴇɴᴋʀɪᴘꜱɪ.

ꜱᴜᴍʙᴇʀ: ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴜɢʟɪꜰʏᴊꜱ ᴜɴᴛᴜᴋ ᴇɴᴋʀɪᴘꜱɪ ᴊᴀᴠᴀꜱᴄʀɪᴘᴛ.</blockquote></b>

"""

# Periksa apakah UglifyJS sudah terinstal
if not shutil.which("uglifyjs"):
    raise Exception("⚠️ UglifyJS belum terinstal. Install dengan `npm install -g uglify-js`")

@PY.UBOT("enc")
@PY.TOP_CMD
async def encrypt_js(client: Client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.document:
        return await message.reply("😠 sɪʟᴀᴋᴀɴ ʙᴀʟᴀꜱ ꜰɪʟᴇ .ᴊꜱ ᴜɴᴛᴜᴋ ᴅɪᴇɴᴋʀɪᴘꜱɪ.")

    file_info = message.reply_to_message.document
    file_name = file_info.file_name

    if not file_name.endswith('.js'):
        return await message.reply("❌ ꜰɪʟᴇ ʜᴀʀᴜꜱ ʙᴇʀᴇᴋꜱᴛᴇɴꜱɪ .ᴊꜱ!")

    # Mengunduh file dari Telegram
    msg = await message.reply("⚡ ᴍᴇɴɢᴜɴᴅᴜʜ ꜰɪʟᴇ...")
    file_path = await client.download_media(message.reply_to_message.document)

    await msg.edit("⚡ ᴍᴇᴍᴘʀᴏꜱᴇꜱ ᴇɴᴄʀʏᴘᴛ ʜᴀʀᴅ ᴄᴏᴅᴇ ᴄᴇꜱꜱ...")

    # Buat nama file hasil enkripsi
    encrypted_file_path = f"./encrypted_{file_name}"

    # Jalankan UglifyJS untuk obfuscation
    try:
        subprocess.run(["uglifyjs", file_path, "-o", encrypted_file_path, "-c", "-m"], check=True)

        await message.reply_document(
            encrypted_file_path,
            caption="✅ **ꜰɪʟᴇ ʙᴇʀʜᴀꜱɪʟ ᴅɪᴇɴᴋʀɪᴘꜱɪ!**\n🔒 @errcessbot"
        )

    except subprocess.CalledProcessError:
        await msg.edit("❌ ɢᴀɢᴀʟ ᴍᴇɴɢᴇɴᴋʀɪᴘꜱɪ ꜰɪʟᴇ!")

    # Hapus file sementara
    os.remove(file_path)
    os.remove(encrypted_file_path)
