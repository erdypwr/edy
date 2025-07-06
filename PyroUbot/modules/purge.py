import asyncio

from PyroUbot import *

__MODULE__ = "ᴘᴜʀɢᴇ"
__HELP__ = """
<blockquote>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘᴜʀɢᴇ ᴄᴇꜱꜱ 』

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ᴘᴜʀɢᴇ</code>
    ʙᴇʀꜱɪʜᴋᴀɴ (ʜᴀᴘᴜꜱ ꜱᴇᴍᴜᴀ ᴘᴇꜱᴀɴ) ᴅᴀʀɪ ᴘᴇꜱᴀɴ ʏᴀɴɢ ᴅɪ ʙᴀʟᴇꜱ

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ᴅᴇʟ</code>
    ᴍᴇɴɢʜᴀᴘᴜꜱ ᴘᴇꜱᴀɴ ʏᴀɴɢ ᴅɪ ʙᴀʟᴀꜱ

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ᴘᴜʀɢᴇᴍᴇ</code>
    ᴍᴇɴɢʜᴀᴘᴜꜱ ᴘᴇꜱᴀɴ ᴇʟᴜ ꜱᴇɴᴅɪʀɪ </blockquote>
"""


@PY.UBOT("del")
@PY.TOP_CMD
async def _(client, message):
    rep = message.reply_to_message
    await message.delete()
    await rep.delete()


@PY.UBOT("purgeme")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if len(message.command) != 2:
        return await message.delete()
    n = (
        message.reply_to_message
        if message.reply_to_message
        else message.text.split(None, 1)[1].strip()
    )
    if not n.isnumeric():
        return await message.reply(f"{ggl}Argumen Tidak Valid")
    n = int(n)
    if n < 1:
        return await message.reply(f"{ggl}Butuh Nomer 1-999")
    chat_id = message.chat.id
    message_ids = [
        m.id
        async for m in client.search_messages(
            chat_id,
            from_user=int(message.from_user.id),
            limit=n,
        )
    ]
    if not message_ids:
        return await message.reply_text(f"{ggl}Tidak Ada Pesan Yang Ditemukan Cess")
    to_delete = [message_ids[i : i + 999] for i in range(0, len(message_ids), 999)]
    for hundred_messages_or_less in to_delete:
        await client.delete_messages(
            chat_id=chat_id,
            message_ids=hundred_messages_or_less,
            revoke=True,
        )
        mmk = await message.reply(f"{brhsl} {n} Pesan Telah Dihapus Cess")
        await asyncio.sleep(1)
        await mmk.delete()


@PY.UBOT("purge")
@PY.TOP_CMD
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    await message.delete()
    if not message.reply_to_message:
        return await message.reply_text(f"{ggl}Membalas Pesan Untuk Dibersihkan Cess")
    chat_id = message.chat.id
    message_ids = []
    for message_id in range(
        message.reply_to_message.id,
        message.id,
    ):
        message_ids.append(message_id)
        if len(message_ids) == 100:
            await client.delete_messages(
                chat_id=chat_id,
                message_ids=message_ids,
                revoke=True,
            )
            message_ids = []
    if len(message_ids) > 0:
        await client.delete_messages(
            chat_id=chat_id,
            message_ids=message_ids,
            revoke=True,
        )
