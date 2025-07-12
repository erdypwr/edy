import asyncio

from pyrogram.enums import *
from pyrogram.errors import FloodWait
from pyrogram.types import *

from PyroUbot import *

__MODULE__ = "sᴜᴅᴏ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴜᴅᴏ ᴄᴇꜱꜱ 』</b>

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ᴀᴅᴅꜱᴜᴅᴏ [@ᴜꜱᴇʀɴᴀᴍᴇ/ʀᴇᴘʟᴀʏ ᴘᴇꜱᴀɴ]</code>  
<i>ᴘᴇɴᴊᴇʟᴀꜱᴀɴ:</i> ᴜɴᴛᴜᴋ ᴀᴋꜱᴇꜱ ᴜꜱᴇʀ ʟᴀɪɴ ᴀɢᴀʀ ʙɪꜱᴀ ᴍᴇɴᴊᴀʟᴀɴᴋᴀɴ ꜰɪᴛᴜʀ ᴇʀʀᴄᴇꜱꜱʙᴏᴛ 

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ᴅᴇʟꜱᴜᴅᴏ [@ᴜꜱᴇʀɴᴀᴍᴇ/ʀᴇᴘʟᴀʏ ᴘᴇꜱᴀɴ]</code>  
<i>ᴘᴇɴᴊᴇʟᴀꜱᴀɴ:</i> ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜꜱ ᴀᴋꜱᴇꜱ ᴜꜱᴇʀ  

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ʟɪꜱᴛꜱᴜᴅᴏ</code>  
<i>ᴘᴇɴᴊᴇʟᴀꜱᴀɴ:</i> ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴀꜰᴛᴀʀ ᴜꜱᴇʀ ʏᴀɴɢ ꜱᴜᴅᴀʜ ᴅɪʙᴇʀɪ ᴀᴋꜱᴇꜱ ꜱᴜᴅᴏ</i>  
"""

@PY.UBOT("addsudo")
async def _(client, message):
    msg = await message.reply("⏰ ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit("❌ ꜱɪʟᴀʜᴋᴀɴ ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ᴍᴀꜱᴜᴋᴋᴀɴ ᴜꜱᴇʀɴᴀᴍᴇ/ᴜꜱᴇʀ ɪᴅ ᴄᴜᴋɪ.")

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(f"❌ ᴇʀʀᴏʀ ᴄᴜᴋɪ: {error}")

    sudo_users = await get_list_from_vars(client.me.id, "SUDOERS")
    if user.id in sudo_users:
        return await msg.edit(f"❌ {user.first_name} ꜱᴜᴅᴀʜ ᴍᴇɴᴊᴀᴅɪ ᴘᴇɴɢɢᴜɴᴀ ꜱᴜᴅᴏ ᴄᴇꜱꜱ.")

    try:
        await add_to_vars(client.me.id, "SUDOERS", user.id)
        return await msg.edit(f"🏓 {user.first_name} ʙᴇʀʜᴀꜱɪʟ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ꜱᴇʙᴀɢᴀɪ ꜱᴜᴅᴏ ɢᴀɴɢ ᴄᴇꜱꜱ.")
    except Exception as error:
        return await msg.edit(f"❌ ᴇʀʀᴏʀ ᴄᴜᴋɪ: {error}")

@PY.UBOT("delsudo|unsudo")
async def _(client, message):
    msg = await message.reply("🏓 ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit("❌ ꜱɪʟᴀʜᴋᴀɴ ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ᴍᴀꜱᴜᴋᴋᴀɴ ᴜꜱᴇʀɴᴀᴍᴇ/ᴜꜱᴇʀ ɪᴅ ᴄᴜᴋɪ.")

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(f"❌ ᴇʀʀᴏʀ ᴄᴜᴋɪ: {error}")

    sudo_users = await get_list_from_vars(client.me.id, "SUDOERS")
    if user.id not in sudo_users:
        return await msg.edit(f"❌ {user.first_name} ʙᴜᴋᴀɴ ʙᴀɢɪᴀɴ ᴅᴀʀɪ ᴘᴇɴɢɢᴜɴᴀ ꜱᴜᴅᴏ ᴄᴜᴋɪ.")

    try:
        await remove_from_vars(client.me.id, "SUDOERS", user.id)
        return await msg.edit(f"🏓 {user.first_name} ʙᴇʀʜᴀꜱɪʟ ᴅɪʜᴀᴘᴜꜱ ᴅᴀʀɪ ᴅᴀꜰᴛᴀʀ ᴘᴇɴɢɢᴜɴᴀ ꜱᴜᴅᴏ ᴄᴜᴋɪ.")
    except Exception as error:
        return await msg.edit(f"❌ ᴇʀʀᴏʀ ᴄᴜᴋɪ: {error}")

@PY.UBOT("sudolist|listsudo")
async def _(client, message):
    msg = await message.reply("🏓 ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    sudo_users = await get_list_from_vars(client.me.id, "SUDOERS")

    if not sudo_users:
        return await msg.edit("❌ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇɴɢɢᴜɴᴀ ꜱᴜᴅᴏ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴄᴜᴋɪ.")

    sudo_list = []
    for user_id in sudo_users:
        try:
            user = await client.get_users(int(user_id))
            sudo_list.append(f"• [{user.first_name}](tg://user?id={user.id}) | <code>{user.id}</code>")
        except:
            continue

    response = f"🏓 ᴅᴀꜰᴛᴀʀ ᴘᴇɴɢɢᴜɴᴀ ꜱᴜᴅᴏ ᴄᴇꜱꜱ:\n" + "\n".join(sudo_list)
    return await msg.edit(response)