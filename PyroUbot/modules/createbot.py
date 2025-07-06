from pyrogram import Client, filters
from PyroUbot import PY
from PyroUbot import *

__MODULE__ = "ᴄʀᴇᴀᴛᴇ ʙᴏᴛ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘᴇᴍʙᴜᴀᴛᴀɴ ʙᴏᴛ ᴀᴜᴛᴏᴍᴀᴛɪs 』</b>

ᴘᴇʀɪɴᴛᴀʜ: <code>{0}ᴄʀᴇᴀᴛᴇʙᴏᴛ</code> [ɴᴀᴍᴀ_ʙᴏᴛ ᴜsᴇʀɴᴀᴍᴇ_ʙᴏᴛ]
ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴍᴇᴍʙᴜᴀᴛ ʙᴏᴛ ᴛᴇʟᴇɢʀᴀᴍ ʙᴀʀᴜ ᴏᴛᴏᴍᴀᴛɪs ᴍᴇʟᴀʟᴜɪ @ʙᴏᴛꜰᴀᴛʜᴇʀ ᴄᴇss</blockquote>

"""

@PY.UBOT("createbot")
@PY.TOP_CMD
async def create_bot_command(client, message):
    # Ambil argumen dari pesan
    args = message.text.split(maxsplit=2)

    if len(args) < 3:
        await message.reply_text(
            "<blockquote><b>⚠️ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ ᴄᴇss: createbot [nama_bot] [username_bot]</b></blockquote>\n"
            "ᴄᴏɴᴛᴏʜ ᴄᴇss: <code>.createbot NamaBot Nama_Bot</code>"
        )
        return

    bot_name = args[1]
    bot_username = args[2]

    if not bot_username.endswith("Bot"):
        await message.reply_text("❌ **ᴜsᴇʀɴᴀᴍᴇ ʙᴏᴛ ʜᴀʀᴜs ᴅɪᴀᴋʜɪʀɪ ᴅᴇɴɢᴀɴ 'ʙᴏᴛ' ᴄᴇss.**")
        return

    try:
        botfather = "@BotFather"
        
        # Kirim ᴘᴇʀɪɴᴛᴀʜ ke BotFather
        await client.send_message(botfather, "/newbot")
        await asyncio.sleep(2)
        await client.send_message(botfather, bot_name)
        await asyncio.sleep(2)
        await client.send_message(botfather, bot_username)

        await message.reply_text(
            f"<blockquote><b>✅ **ᴘᴇʀᴍɪɴᴛᴀᴀɴ ᴘᴇᴍʙᴜᴀᴛᴀɴ ʙᴏᴛ ᴛᴇʟᴀʜ ᴅɪᴋɪʀɪᴍ ᴋᴇ @BotFather ᴄᴇss!**\n"
            f"🆕 **ɴᴀᴍᴀ ʙᴏᴛ:** `{bot_name}`\n"
            f"🔗 **ᴜsᴇʀɴᴀᴍᴇ:** @{bot_username}\n\n"
            "sɪʟᴀᴋᴀɴ ᴄᴇᴋ @BotFather ᴜɴᴛᴜᴋ ᴍᴇʟᴀɴᴊᴜᴛᴋᴀɴ ᴘʀᴏsᴇs ᴋᴏɴꜰɪɢᴜʀᴀsɪ ᴄᴇss.</blockquote></b>"
        )
    
    except Exception as e:
        await message.reply_text(f"⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ᴄᴇss: {str(e)}")