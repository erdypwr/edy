import asyncio
from asyncio import sleep
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message

from PyroUbot import *

@PY.UBOT("etmin")
@PY.TOP_CMD
async def promotte(client: Client, message: Message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    user_id = await extract_user(message)
    anu = await eor(message, f"{prs}ᴘʀᴏsᴇs ᴄᴇss...")
    if not user_id:
        return await anu.edit(f"{ggl}ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.")
    (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    try:
        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=False,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=False,
            ),
        )
        await asyncio.sleep(1)
        umention = (await client.get_users(user_id)).mention
        return await anu.edit(f"{sks}ʙᴇʀʜᴀsɪʟ ᴍᴇᴍᴘʀᴏᴍᴏsɪᴋᴀɴ : {umention} ᴍᴇɴᴊᴀᴅɪ ᴀᴅᴍɪɴ")
    except ChatAdminRequired:
        await anu.edit(f"{ggl}**ᴇʟᴜ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ ᴅɪ ɢʀᴏᴜᴘ ɪɴɪ !**")

@PY.UBOT("ceo")
@PY.TOP_CMD
async def promotte(client: Client, message: Message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    user_id = await extract_user(message)
    anu = await eor(message, f"{prs}ᴘʀᴏsᴇs ᴄᴇss...")
    if not user_id:
        return await anu.edit(f"{ggl}ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.")
    (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    try:
        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=True,
            ),
        )
        await asyncio.sleep(1)
        umention = (await client.get_users(user_id)).mention
        return await anu.edit(f"{sks}ʙᴇʀʜᴀsɪʟ ᴍᴇᴍᴘʀᴏᴍᴏsɪᴋᴀɴ : {umention} ᴍᴇɴᴊᴀᴅɪ ᴄᴇᴏ")
    except ChatAdminRequired:
        await anu.edit(f"{ggl}**ᴇʟᴜ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ ᴅɪ ɢʀᴏᴜᴘ ɪɴɪ !**")

 
@PY.UBOT("demote")
@PY.TOP_CMD
async def demote(client: Client, message: Message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    user_id = await extract_user(message)
    sempak = await eor(message, f"{prs}ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    if not user_id:
        return await sempak.edit(f"{ggl}ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ")
    if user_id == client.me.id:
        return await sempak.edit(f"{ggl}ᴛɪᴅᴀᴋ ʙɪsᴀ ᴅᴇᴍᴏᴛᴇ ᴅɪʀɪ sᴇɴᴅɪʀɪ.")
    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
        ),
    )
    await asyncio.sleep(1)
    umention = (await client.get_users(user_id)).mention
    await sempak.edit(f"{sks}ᴅᴇᴍᴏᴛᴇᴅ : {umention}")
    await sempak.edit(sempak)
    await sempak.delete()

@PY.UBOT("getlink")
@PY.TOP_CMD
async def get_link(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    try:
        link = await client.export_chat_invite_link(message.chat.id)
        await message.reply_text(f"{sks}ɪɴɪ ʜᴀsɪʟɴʏᴀ ᴄᴇꜱꜱ : {link}", disable_web_page_preview=True)
    except Exception as r:
        await message.reply_text(f"{ggl}ᴛᴇʀᴊᴀᴅɪ ᴇʀʀᴏʀ : \n {r}")
