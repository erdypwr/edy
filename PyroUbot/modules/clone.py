import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from PyroUbot import *

__MODULE__ = "𝙲𝙻𝙾𝙽𝙴"
__HELP__ = """
『 📚 ꜰᴏʟᴅᴇʀ ᴜɴᴛᴜᴋ ᴄʟᴏɴᴇ ᴄᴇꜱꜱ 』

🚦 ᴘᴇʀɪɴᴛᴀʜ : {0}ᴄʟᴏɴᴇ @ᴜꜱᴇʀɴᴀᴍᴇ
🦠 ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇɴᴄʟᴏɴᴇ ꜱᴇꜱᴇᴏʀᴀɴɢ ᴜꜱᴇʀ ᴄᴇꜱꜱ.
🚦 ᴘᴇʀɪɴᴛᴀʜ : {0}ᴄʟᴏɴᴇ ᴋᴇᴍʙᴀʟɪ
🦠 ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴍʙᴀʟɪᴋᴀɴ ᴋᴀᴍᴜ ᴋᴇ ɪᴅᴇɴᴛɪᴛᴀꜱ ꜱᴇʙᴇʟᴜᴍɴʏᴀ ᴄᴇꜱꜱ.</b></blockquote>

"""

STORAGE = {}

@PY.UBOT("clone")
async def impostor(client: Client, message: Message):
    user_id = message.from_user.id  
    inputArgs = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else ""
    WannX2 = ["@WannX2", "@wannx2"]

    if inputArgs in WannX2:
        await message.edit("❌ [Kontol] - Tidak dapat menyamar sebagai Developer😡")
        await client.send_message("@wannofsupport", "Maaf Telah MengClone Wann 🥺")
        return

    xx = await message.edit("⏰ ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")

    if "kembali" in inputArgs:
        if user_id not in STORAGE:
            return await xx.edit("📑 ᴇʟᴜ Harus Meng-Clone Seseorang Dulu Sebelum Mengembalikan Identitas Cess!")

        await message.edit("⏰ ᴍᴇɴɢᴇᴍʙᴀʟɪᴋᴀɴ ɪᴅᴇɴᴛɪᴛᴀs ᴀsʟɪ...")
        await update_profile(client, STORAGE[user_id], restore=True)
        del STORAGE[user_id]
        return await xx.edit("📑 ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢᴇᴍʙᴀʟɪᴋᴀɴ ᴀᴋᴜɴ ᴀɴᴅᴀ!")

    if inputArgs:
        try:
            user = await client.get_users(inputArgs)
        except:
            return await xx.edit("❌ ɴᴀᴍᴀ ᴘᴇɴɢɢᴜɴᴀ/ɪᴅ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ ᴄᴇss")
        userObj = await client.get_chat(user.id)
    elif message.reply_to_message:
        reply_user = message.reply_to_message.from_user
        if not reply_user:
            return await xx.edit("❌ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴʏᴀᴍᴀʀ sᴇʙᴀɢᴀɪ ᴀᴅᴍɪɴ ᴀɴᴏɴɪᴍ ᴄᴇss 🥺")
        userObj = await client.get_chat(reply_user.id)
    else:
        return await xx.edit("❌ ɢᴜɴᴀᴋᴀɴ .ᴄʟᴏɴᴇ @ᴜsᴇʀɴᴀᴍᴇ ᴀᴛᴀᴜ ʀᴇᴘʟʏ ᴘᴇsᴀɴ ᴘᴇɴɢɢᴜɴᴀ.")

    if user_id not in STORAGE:
        my_profile = await client.get_chat("me")
        my_photos = [p async for p in client.get_chat_photos("me")]
        STORAGE[user_id] = {"profile": my_profile, "photos": my_photos}

    await xx.edit("ᴍᴇɴᴄᴜʀɪ ɪᴅᴇɴᴛɪᴛᴀs sɪ ᴄᴜᴋɪ...")
    await update_profile(client, userObj)
    await xx.edit("ᴀᴏᴡᴋᴀᴏᴡᴋᴡ ɢᴡ ᴊᴀᴅɪ ʟᴜ ɴɪ, ᴄᴜᴋɪ🥴")


async def update_profile(client: Client, userObj, restore=False):
    if restore:
        profile_data = userObj["profile"]
        photos = userObj["photos"]

        await client.update_profile(
            first_name=profile_data.first_name or "ᴀᴋᴜɴ ᴅɪʜᴀᴘᴜs",
            last_name=profile_data.last_name or "",
            bio=profile_data.bio or ""
        )

        if photos:
            try:
                pfp = await client.download_media(photos[0].file_id)
                await client.set_profile_photo(photo=pfp)
            except:
                pass
        return

    first_name = userObj.first_name or "ᴀᴋᴜɴ ᴅɪʜᴀᴘᴜs"
    last_name = userObj.last_name or ""
    
    user_info = await client.get_users(userObj.id)
    is_premium = user_info.is_premium if hasattr(user_info, "is_premium") else False

    bio = userObj.bio if is_premium else (userObj.bio[:70] if userObj.bio else "")

    try:
        photos = [p async for p in client.get_chat_photos(userObj.id)]
        if photos:
            pfp = await client.download_media(photos[0].file_id)
            await client.set_profile_photo(photo=pfp)
    except:
        pass

    await client.update_profile(first_name=first_name, last_name=last_name, bio=bio)