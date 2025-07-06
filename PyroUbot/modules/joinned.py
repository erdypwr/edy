from pyrogram import *
from pyrogram import errors
from pyrogram import enums
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors.exceptions.not_acceptable_406 import ChannelPrivate
from PyroUbot import *

__MODULE__ = "ᴊᴏɪɴʟᴇᴀᴠᴇ"
__HELP__ = """
<blockquote>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴊᴏɪɴʟᴇᴀᴠᴇ ᴄᴇss</blockquote>

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}kickme</code>
    ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴏᴜᴘ ᴛᴇʟᴇɢʀᴀᴍ

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}join</code>
    ᴊᴏɪɴ ᴋᴇ ɢʀᴏᴜᴘ ᴍᴇʟᴀʟᴜɪ ᴛᴀᴜᴛᴀɴ ᴀᴛᴀᴜ ᴜsᴇʀɴᴀᴍᴇ ɢʀᴏᴜᴘ

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}leaveallgc</code>
    ᴋᴇʟᴜᴀʀ sᴇᴍᴜᴀ ᴅᴀʀɪ ɢʀᴏᴜᴘ ᴛᴇʟᴇɢʀᴀᴍ ᴋᴇᴄᴜᴀʟɪ ᴀᴅᴍɪɴ/ᴏᴡɴᴇʀ

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}leaveallmute</code>
    ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴜᴘ ʏᴀɴɢ ᴍᴇᴍʙᴀᴛᴀsɪ ᴇʟᴜ

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}leaveallch</code>
    ᴋᴇʟᴜᴀʀ sᴇᴍᴜᴀ ᴅᴀʀɪ ᴄʜᴀɴɴᴇʟ ᴋᴇᴄᴜᴀʟɪ ᴀᴅᴍɪɴ/ᴏᴡɴᴇʀ</blockquote>
"""


@PY.UBOT("kickme")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await message.reply(f"{prs}ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    if message.chat.id in BLACKLIST_CHAT:
        return await xxnx.edit(f"{ggl}ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴅɪʟᴀʀᴀɴɢ ᴅɪɢᴜɴᴀᴋᴀɴ ᴅɪ ɢʀᴏᴜᴘ ɪɴɪ ᴄᴇss!")
    try:
        await xxnx.edit_text(f"{client.me.first_name} ᴛᴇʟᴀʜ ᴍᴇɴɪɴɢɢᴀʟᴋᴀɴ ɢʀᴜᴘ ɪɴɪ, ʙʏᴇ ᴄᴜᴋɪ!!{sks}")
        await client.leave_chat(Man)
    except Exception as ex:
        await xxnx.edit_text(f"{ggl}ᴇʀʀᴏʀ: \n\n{str(ex)}")



@PY.UBOT("join")
@PY.TOP_CMD
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await message.reply(f"{prs}ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    try:
        await xxnx.edit(f"{sks}ʙᴇʀʜᴀsɪʟ ʙᴇʀɢᴀʙᴜɴɢ ᴋᴇ ᴄʜᴀᴛ ɪᴅ ᴄᴇss: {Man}")
        await client.join_chat(Man)
    except Exception as ex:
        await xxnx.edit(f"{ggl}ᴇʀʀᴏʀ: \n\n{str(ex)}")


@PY.UBOT("leaveallgc")
@PY.TOP_CMD
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    Man = await message.reply(f"{prs}ɢʟᴏʙᴀʟ ʟᴇᴀᴠᴇ ᴅᴀʀɪ ᴏʙʀᴏʟᴀɴ ɢʀᴏᴜᴘ ᴄᴇss...")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                member = await client.get_chat_member(chat, "me")
                if member.status not in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
                    done += 1
                    await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Man.edit(
        f"{sks}ʙᴇʀʜᴀsɪʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {done} ɢʀᴏᴜᴘ\n{ggl}ɢᴀɢᴀʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {er} ɢʀᴏᴜᴘ ᴄᴇss"
    )


@PY.UBOT("leaveallch")
@PY.TOP_CMD
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    Man = await message.reply(f"{prs}ɢʟᴏʙᴀʟ ʟᴇᴀᴠᴇ ᴅᴀʀɪ ᴄʜᴀɴɴᴇʟ ᴄᴇss...")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == ChatType.CHANNEL:
            chat = dialog.chat.id
            try:
                member = await client.get_chat_member(chat, "me")
                if member.status not in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
                    done += 1
                    await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Man.edit(
        f"{sks}ʙᴇʀʜᴀsɪʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {done} ᴄʜᴀɴɴᴇʟ\n{ggl}ɢᴀɢᴀʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {er} ᴄʜᴀɴɴᴇʟ ᴄᴇss"
    )

@PY.UBOT("leaveallmute")
@PY.TOP_CMD
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    done = 0
    Haku = await message.reply_text(f"{prs}ᴘʀᴏꜱᴇꜱꜱ ᴄᴇss...")
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (ChatType.SUPERGROUP, ChatType.GROUP):
            chat_id = dialog.chat.id
            try:
                member = await client.get_chat_member(chat_id, "me")
                if member.status == ChatMemberStatus.RESTRICTED:
                    await client.leave_chat(chat_id)
                    done += 1
            except Exception:
                pass
    await Haku.edit(f"""
{sks}ʙᴇʀʜᴀsɪʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ : {done} ɢʀᴜᴘ ʏᴀɴɢ ᴛᴇʟᴀʜ ᴍᴇᴍʙᴀᴛᴀsɪ ᴇʟᴜ ᴄᴇss!
""")
