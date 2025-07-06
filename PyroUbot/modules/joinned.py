from pyrogram import *
from pyrogram import errors
from pyrogram import enums
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors.exceptions.not_acceptable_406 import ChannelPrivate
from PyroUbot import *

__MODULE__ = "ᴊᴏɪɴʟᴇᴀᴠᴇ"
__HELP__ = """
<blockquote>Bantuan Untuk Joinleave Cess</blockquote>

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}kickme</code>
    Keluar Dari Group Telegram

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}join</code>
    Join Ke Group Melalui Tautan Atau Username Group

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}leaveallgc</code>
    Keluar Semua Dari Group Telegram Kecuali Admin/Owner

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}leaveallmute</code>
    Keluar Dari Grup Yang Membatasi Anda

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}leaveallch</code>
    Keluar Semua Dari Channel Kecuali Admin/Owner</blockquote>
"""


@PY.UBOT("kickme")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await message.reply(f"{prs}Prosess Cess...")
    if message.chat.id in BLACKLIST_CHAT:
        return await xxnx.edit(f"{ggl}ᴘᴇʀɪɴᴛᴀʜ Ini Dilarang Digunakan Di Group Ini Cess!")
    try:
        await xxnx.edit_text(f"{client.me.first_name} Telah Meninggalkan Grup Ini, Bye Cuki!!{sks}")
        await client.leave_chat(Man)
    except Exception as ex:
        await xxnx.edit_text(f"{ggl}ERROR: \n\n{str(ex)}")



@PY.UBOT("join")
@PY.TOP_CMD
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await message.reply(f"{prs}Prosess Cess...")
    try:
        await xxnx.edit(f"{sks}Berhasil Bergabung Ke Chat ID Cess: {Man}")
        await client.join_chat(Man)
    except Exception as ex:
        await xxnx.edit(f"{ggl}ERROR: \n\n{str(ex)}")


@PY.UBOT("leaveallgc")
@PY.TOP_CMD
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    Man = await message.reply(f"{prs}Global Leave Dari Obrolan Group Cess...")
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
        f"{sks}Berhasil Keluar Dari {done} Group\n{ggl}Gagal Keluar Dari {er} Group Cess"
    )


@PY.UBOT("leaveallch")
@PY.TOP_CMD
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    Man = await message.reply(f"{prs}Global Leave Dari Channel Cess...")
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
        f"{sks}Berhasil Keluar Dari {done} Channel\n{ggl}Gagal Keluar Dari {er} Channel Cess"
    )

@PY.UBOT("leaveallmute")
@PY.TOP_CMD
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    done = 0
    Haku = await message.reply_text(f"{prs}Prosess Cess...")
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
{sks}Berhasil Keluar Dari : {done} Grup Yang Telah Membatasi Elu Cess!
""")
