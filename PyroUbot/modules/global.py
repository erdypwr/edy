import asyncio

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *
from pyrogram.types import ChatPermissions
from PyroUbot import *
from PyroUbot.core.helpers.emoji import EMO
from PyroUbot.core.helpers.font_help import gens_font


__MODULE__ = "ɢʟᴏʙᴀʟ"
__HELP__ = """
<blockquote>『ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢʟᴏʙᴀʟ ᴄᴇꜱꜱ 』

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ɢʙᴀɴ</code>
ʙᴀɴɴᴇᴅ ᴜꜱᴇʀ ᴅᴀʀɪ ꜱᴇᴍᴜᴀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ᴄᴇꜱꜱ

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ᴜɴɢʙᴀɴ</code>
ᴜɴʙᴀɴɴᴇᴅ ᴜꜱᴇʀ ᴅᴀʀɪ ꜱᴇᴍᴜᴀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ᴄᴇꜱꜱ

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ɢᴍᴜᴛᴇ</code>
ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴍᴜᴛᴇ ᴜꜱᴇʀ ᴅᴀʀɪ ꜱᴇᴍᴜᴀ ɢᴄ ʏᴀɴɢ ʟᴜ ᴀᴅᴍɪɴ ᴄᴇꜱꜱ

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ᴜɴɢᴍᴜᴛᴇ</code>
ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜɴɢᴍᴜᴛᴇ ᴜꜱᴇʀ ᴅᴀʀɪ ꜱᴇᴍᴜᴀ ɢᴄ ʏᴀɴɢ ʟᴜ ᴀᴅᴍɪɴ ᴄᴇꜱꜱ</blockquote>

"""

      

@PY.UBOT("gban")
@PY.TOP_CMD
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    user_id = await extract_user(message)
    _msg = f"{prs}ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ..."

    Tm = await message.reply(_msg)
    if not user_id:
        return await Tm.edit(f"{ggl}ᴜsᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴄᴇss")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    done = 0
    failed = 0
    text = gens_font("tiny", "ɢʟᴏʙᴀʟ {}\n\nʙᴇʀʜᴀsɪʟ: {} ᴄʜᴀᴛ\nɢᴀɢᴀʟ: {} ᴄʜᴀᴛ\nᴜsᴇʀ: <a href='tg://user?id={}'>{} {}</a>")
    global_id = await get_data_id(client, "global")
    for dialog in global_id:
        if user.id == OWNER_ID:
            return await Tm.edit(f"{ggl}ᴇʟᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ɢʙᴀɴ ᴅɪᴀ ᴋᴀʀᴇɴᴀ ᴅɪᴀ ᴘᴇᴍʙᴜᴀᴛ ɢᴜᴀ ᴄᴇss")
        try:
            await client.ban_chat_member(dialog, user.id)
            done += 1
            await asyncio.sleep(0.1)
        except Exception:
            failed += 1
            await asyncio.sleep(0.1)
    await message.reply(
        text.format(
            "banned", done, failed, user.id, user.first_name, (user.last_name or "")
        )
    )
    return await Tm.delete()


@PY.UBOT("ungban")
@PY.TOP_CMD
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    user_id = await extract_user(message)
    _msg = gens_font("tiny", f"{prs}ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")

    Tm = await message.reply(_msg)
    if not user_id:
        return await Tm.edit(gens_font("tiny", f"{ggl}ᴜsᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴄᴇss"))
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    done = 0
    failed = 0
    text = "ɢʟᴏʙᴀʟ {}\n\nʙᴇʀʜᴀsɪʟ: {} ᴄʜᴀᴛ\nɢᴀɢᴀʟ: {} ᴄʜᴀᴛ\nᴜsᴇʀ: <a href='tg://user?id={}'>{} {}</a>"
    global_id = await get_data_id(client, "global")
    for dialog in global_id:
        try:
            await client.unban_chat_member(dialog, user.id)
            done += 1
            await asyncio.sleep(0.1)
        except Exception:
            failed += 1
            await asyncio.sleep(0.1)
    await message.reply(
        text.format(
            "unbanned",
            done,
            failed,
            user.id,
            user.first_name,
            (user.last_name or ""),
        )
    )
    return await Tm.delete()

@PY.UBOT("gmute")
@PY.TOP_CMD
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    user_id = await extract_user(message)
    _msg = f"{prs}ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ..."

    Tm = await message.reply(_msg)
    if not user_id:
        return await Tm.edit(f"{ggl}ᴜsᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴄᴇss")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    done = 0
    failed = 0
    text = "Global {}\n\nBerhasil: {} Chat\nGagal: {} Chat\nUser: <a href='tg://user?id={}'>{} {}</a>"
    global_id = await get_data_id(client, "group")
    for dialog in global_id:
        if user.id == OWNER_ID:
            return await Tm.edit(f"{ggl}ᴇʟᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ɢᴍᴜᴛᴇ ᴅɪᴀ ᴋᴀʀᴇɴᴀ ᴅɪᴀ ᴘᴇᴍʙᴜᴀᴛ ɢᴜᴀ ᴄᴇss")
        try:
            await client.restrict_chat_member(dialog, user.id, ChatPermissions(can_send_messages=False))
            done += 1
            await asyncio.sleep(0.1)
        except Exception:
            failed += 1
            await asyncio.sleep(0.1)
    await message.reply(
        text.format(
            "mute", done, failed, user.id, user.first_name, (user.last_name or "")
        )
    )
    return await Tm.delete()

@PY.UBOT("ungmute")
@PY.TOP_CMD
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    user_id = await extract_user(message)
    _msg = f"{prs}ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ..."
    Tm = await message.reply(_msg)
    if not user_id:
        return await Tm.edit(f"{ggl}ᴜsᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴄᴇss")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    done = 0
    failed = 0
    text = "Global {}\n\nBerhasil: {} Chat\nGagal: {} Chat\nUser: <a href='tg://user?id={}'>{} {}</a>"
    global_id = await get_data_id(client, "global")
    for dialog in global_id:
        try:
            await client.restrict_chat_member(dialog, user.id, ChatPermissions(can_send_messages=True))
            done += 1
            await asyncio.sleep(0.1)
        except Exception:
            failed += 1
            await asyncio.sleep(0.1)
    await message.reply(
        text.format(
            "ungmuted",
            done,
            failed,
            user.id,
            user.first_name,
            (user.last_name or ""),
        )
    )
    return await Tm.delete()
