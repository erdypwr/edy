from PyroUbot import *
from pyrogram.enums import ParseMode
__MODULE__ = "ᴄᴜꜱᴛᴏᴍ"
__HELP__ = """
<blockquote><b>『ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴜꜱᴛᴏᴍ ᴄᴇꜱꜱ 』

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ʟɪʜᴀᴛᴇᴍᴏᴊɪ</code>

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ᴛᴇxᴛ</code>
   ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴛᴇxᴛ ᴘᴀᴅᴀ ᴛᴀᴍᴘɪʟᴀɴ ᴛᴇʀᴛᴇɴᴛᴜ ᴄᴇꜱꜱ

ǫᴜᴇʀʏ:
  <code>{0}ᴘᴏɴɢ</code> | ᴅᴇꜰᴀᴜʟᴛ : ± ᴘᴏɴɢ
  <code>{0}ᴏᴡɴᴇʀ</code> | ᴅᴇꜰᴀᴜʟᴛ : ± ᴏᴡɴᴇʀ
  <code>{0}ᴜʙᴏᴛ</code> | ᴅᴇꜰᴀᴜʟᴛ : ± ᴜʙᴏᴛ

ᴄᴏɴᴛᴏʜ :
     <code>{0}</code>ᴛᴇxᴛ ᴘᴏɴɢ ɴᴏɴᴇ | ᴜɴᴛᴜᴋ ᴍᴇɴʏᴇᴛɪɴɢ ᴋᴇ ᴅᴇꜰᴀᴜʟᴛ</b></blockquote>

"""
def extract_emojis_from_entities(message):
    emojis = []
    for entity in message.entities:
        emoji = message.text[entity.offset : entity.offset + entity.length]
        emojis.append(emoji)
    return emojis

@PY.UBOT("text")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    try:
        msg = await message.reply(f"{prs}ᴘʀᴏsᴇs ᴄᴇss...", quote=True)

        if len(message.command) < 3:
            return await msg.edit(f"{ggl}ᴍᴀsᴜᴋᴋᴀɴ ǫᴜᴇʀʏ ᴅᴀɴ ᴠᴀʟᴜᴇɴʏᴀ ᴄᴇss")

        query_mapping = {
            "pong": "STRING_PONG",
            "owner": "STRING_OWNER",
            "ubot": "STRING_UBOT",
            "devs": "STRING_DEVS",
        }

        command = message.command[0]
        mapping = message.command[1]
        value = " ".join(message.command[2:])

        if mapping.lower() in query_mapping:
            if value.lower() == "none":
                value = False
            query_var = query_mapping[mapping.lower()]
            await set_vars(client.me.id, query_var, value)
            await msg.edit(
                f"{brhsl}ᴛᴇᴋs ʙᴇʀʜᴀsɪʟ ᴅɪꜱᴇᴛᴇʟ ᴋᴇ: {value}"
            )
        else:
            await msg.edit(f"{ggl}ᴍᴀᴘᴘɪɴɢ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴄᴇss, ɢᴜɴᴀᴋᴀɴ: {', '.join(query_mapping.keys())}")

    except Exception as error:
        await msg.edit(str(error))

@PY.UBOT("lihatemoji")
async def extract_emoji(client, message):
    try:
        if not message.reply_to_message:
            return await message.reply_text("ʜᴀʀᴀᴘ ᴍᴇᴍʙᴀʟᴀs ᴘᴇsᴀɴ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴋsᴛʀᴀᴋ ɪᴅ ᴇᴍᴏᴊɪ ᴋʜᴜsᴜs ᴄᴇss.")
        
        custom_emoji_ids = [entity.custom_emoji_id for entity in message.reply_to_message.entities]
        emojis = extract_emojis_from_entities(message.reply_to_message)
        
        formatted_emojis = "".join([f"<emoji id={emoji_id}>{emoji}</emoji>" if emoji_id is not None else emoji for emoji_id, emoji in zip(custom_emoji_ids, emojis)])
        
        await message.reply_text(f"{formatted_emojis}", parse_mode=ParseMode.DISABLED)
    
    except Exception as e:
        await message.reply_text(str(e))
