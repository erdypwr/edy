from PyroUbot import *
from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardMarkup, InlineQueryResultArticle,                            InputTextMessageContent, InlineKeyboardButton)
from datetime import datetime
import pytz

hadir_list = []

def get_hadir_list():
    return "\n".join([f"<blockquote><b>👤 {user['mention']} - {user['jam']}</blockquote></b>" for user in hadir_list])

__MODULE__ = "ᴀʟ ǫᴜʀ'ᴀɴ"
__HELP__ = """
<blockquote><b>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀʟ ǫᴜʀ'ᴀɴ

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ᴀʟǫᴜʀᴀɴ 1 2</code>
    ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ᴀʏᴀᴛ ᴀʟ ǫᴜʀ'ᴀɴ

ᴄᴏɴᴛᴏʜ: <code>{0}ᴀʟǫᴜʀᴀɴ 1 2</code>
ᴍᴀᴋᴀ ʜᴀꜱɪʟɴʏᴀ ꜱᴜʀᴀʜ ᴀʟ-ꜰᴀᴛɪʜᴀʜ ᴀʏᴀᴛ 2</blockquote></b>
"""

@PY.UBOT("absen")
@PY.TOP_CMD
async def absen_command(c, m):
    ggl = await EMO.GAGAL(c)
    sks = await EMO.BERHASIL(c)
    prs = await EMO.PROSES(c)
    user_id = m.from_user.id
    mention = m.from_user.mention
    timestamp = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%d-%m-%Y")
    jam = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%H:%M:%S")
    hadir_list.append({"user_id": user_id, "mention": mention, "jam": jam})
    hadir_text = get_hadir_list()
    try:
        x = await c.get_inline_bot_results(bot.me.username, "absen_in")
        if x.results:
            await m.reply_inline_bot_result(x.query_id, x.results[0].id)
        else:
            await m.reply(f"<blockquote><b>{ggl}ᴛɪᴅᴀᴋ ᴀᴅᴀ ʜᴀꜱɪʟ ɪɴʟɪɴᴇ ʙᴏᴛ</b></blockquote>")
    except asyncio.TimeoutError:
        await m.reply(f"<blockquote><b>{ggl}ᴡᴀᴋᴛᴜ ʜᴀʙɪꜱ ᴅᴀʟᴀᴍ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ʜᴀꜱɪʟ ɪɴʟɪɴᴇ ʙᴏᴛ</b></blockquote>")
    except Exception as e:
        await m.reply(f"<blockquote><b>{ggl}ᴛᴇʀᴊᴀᴅɪ ᴋᴇꜱᴀʟᴀʜᴀɴ: {str(e).translate(str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀꜱᴛᴜᴠᴡxʏᴢᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀꜱᴛᴜᴠᴡxʏᴢ'))}</b></blockquote>")

@PY.UBOT("delabsen")
@PY.TOP_CMD
async def clear_absen_command(c, m):
    hadir_list.clear()
    ggl = await EMO.GAGAL(c)
    sks = await EMO.BERHASIL(c)
    prs = await EMO.PROSES(c)
    await m.reply(f"<blockquote><b>{sks}ꜱᴇᴍᴜᴀ ᴀʙꜱᴇɴ ʙᴇʀʜᴀꜱɪʟ ᴅɪʜᴀᴘᴜꜱ</b></blockquote>")


@PY.INLINE("^absen_in")
async def absen_query(c, iq):
    user_id = iq.from_user.id
    mention = iq.from_user.mention
    timestamp = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%d-%m-%Y")
    jam = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%H:%M:%S")
    hadir_list.append({"user_id": user_id, "mention": mention, "jam": jam})
    hadir_text = get_hadir_list()

    text = f"<blockquote><b>**ᴀʙꜱᴇɴ ᴛᴀɴɢɢᴀʟ:**\n{timestamp}\n\n**ʟɪꜱᴛ ᴀʙꜱᴇɴ:**\n{hadir_text}\n\n</b></blockquote>"
    buttons = [[InlineKeyboardButton("hadir", callback_data="absen_hadir")]]
    keyboard = InlineKeyboardMarkup(buttons)
    await c.answer_inline_query(
        iq.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="💬",
                    input_message_content=InputTextMessageContent(text),
                    reply_markup=keyboard
                )
            )
        ],
    )

@PY.CALLBACK("absen_hadir")
async def hadir_callback(c, cq):
    user_id = cq.from_user.id
    mention = cq.from_user.mention
    timestamp = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%d-%m-%Y")
    jam = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%H:%M:%S")
    if any(user['user_id'] == user_id for user in hadir_list):
        await cq.answer("ᴇʟᴜ ꜱᴜᴅᴀʜ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴀʙꜱᴇɴ ꜱᴇʙᴇʟᴜᴍɴʏᴀ", show_alert=True)
    else:
        hadir_list.append({"user_id": user_id, "mention": mention, "jam": jam})
        hadir_text = get_hadir_list()
        text = f"ᴀʙꜱᴇɴ ᴛᴀɴɢɢᴀʟ:\n{timestamp}\n\nʟɪꜱᴛ ᴀʙꜱᴇɴ:\n{hadir_text}\n\n"
        buttons = [[InlineKeyboardButton("hadir", callback_data="absen_hadir")]]
        keyboard = InlineKeyboardMarkup(buttons)
        await cq.edit_message_text(text, reply_markup=keyboard)
