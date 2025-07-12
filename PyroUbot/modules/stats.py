import time
from PyroUbot import *

__MODULE__ = "ꜱᴛᴀᴛꜱ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱᴛᴀᴛꜱ ᴄᴇꜱꜱ 』</b>

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}stats</code>
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴᴀᴍᴘɪʟᴋᴀɴ ꜱᴛᴀᴛɪꜱᴛɪᴋ ᴀᴋᴜɴ ᴛᴇʟᴇɢʀᴀᴍ ᴇʟᴜ
• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ustat</code> / <code>{0}ustats</code> / <code>{0}deteksi</code> [ᴜꜱᴇʀɴᴀᴍᴇ/ɪᴅ/ʙᴀʟᴀꜱ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴɢᴇᴄᴇᴋ ʀɪᴡᴀʏᴀᴛ ɢʀᴜᴘ ᴅᴀʀɪ ᴘᴇɴɢɢᴜɴᴀ ᴛᴇʀꜱᴇʙᴜᴛ
</blockquote>
"""

def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)

def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"<a href='tg://user?id={user.id}'>{full_name}</a>"

@PY.UBOT(["stats"])
async def _(c, m):
    stat = await m.reply("<b>ᴍᴇɴɢᴜᴍᴘᴜʟᴋᴀɴ ꜱᴛᴀᴛɪꜱᴛɪᴋ ᴄᴇꜱꜱ...</b>")
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    async for dialog in c.get_dialogs():
        entity = dialog.chat
        if getattr(entity, 'type', None) == 'channel' and getattr(entity, 'broadcast', False):
            broadcast_channels += 1
            if getattr(entity, 'creator', False) or getattr(entity, 'admin_rights', None):
                admin_in_broadcast_channels += 1
            if getattr(entity, 'creator', False):
                creator_in_channels += 1
        elif (getattr(entity, 'type', None) == 'supergroup' or getattr(entity, 'type', None) == 'group'):
            groups += 1
            if getattr(entity, 'creator', False) or getattr(entity, 'admin_rights', None):
                admin_in_groups += 1
            if getattr(entity, 'creator', False):
                creator_in_groups += 1
        elif getattr(entity, 'type', None) == 'private':
            private_chats += 1
            if getattr(entity, 'is_bot', False):
                bots += 1
        unread_mentions += getattr(dialog, 'unread_mentions_count', 0)
        unread += getattr(dialog, 'unread_count', 0)
    stop_time = time.time() - start_time
    try:
        blocked = await c.get_blocked_users()
        ct = len(blocked)
    except Exception:
        ct = 0
    # Sticker pack count is not available in Pyrogram, so set to '-'
    sp_count = '-'
    full_name = inline_mention(await c.get_me())
    response = f"📊 <b>ꜱᴛᴀᴛɪꜱᴛɪᴋ ᴜɴᴛᴜᴋ {full_name}</b>\n\n"
    response += f"<b>ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ:</b> {private_chats}\n"
    response += f"<b> •• ᴜꜱᴇʀ:</b> {private_chats - bots}\n"
    response += f"<b> •• ʙᴏᴛ:</b> {bots}\n"
    response += f"<b>ɢʀᴏᴜᴘ:</b> {groups}\n"
    response += f"<b>ᴄʜᴀɴɴᴇʟ:</b> {broadcast_channels}\n"
    response += f"<b>ᴀᴅᴍɪɴ ᴅɪ ɢʀᴏᴜᴘ:</b> {admin_in_groups}\n"
    response += f"<b> •• ᴄʀᴇᴀᴛᴏʀ:</b> {creator_in_groups}\n"
    response += f"<b> •• ᴀᴅᴍɪɴ ʀɪɢʜᴛꜱ:</b> {admin_in_groups - creator_in_groups}\n"
    response += f"<b>ᴀᴅᴍɪɴ ᴅɪ ᴄʜᴀɴɴᴇʟ:</b> {admin_in_broadcast_channels}\n"
    response += f"<b> •• ᴄʀᴇᴀᴛᴏʀ:</b> {creator_in_channels}\n"
    response += f"<b> •• ᴀᴅᴍɪɴ ʀɪɢʜᴛꜱ:</b> {admin_in_broadcast_channels - creator_in_channels}\n"
    response += f"<b>ᴜɴʀᴇᴀᴅ:</b> {unread}\n"
    response += f"<b>ᴜɴʀᴇᴀᴅ ᴍᴇɴᴛɪᴏɴꜱ:</b> {unread_mentions}\n"
    response += f"<b>ʙʟᴏᴄᴋᴇᴅ ᴜꜱᴇʀꜱ:</b> {ct}\n"
    response += f"<b>ᴛᴏᴛᴀʟ ꜱᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ ᴛᴇʀɪɴꜱᴛᴀʟ:</b> <code>{sp_count}</code>\n\n"
    response += f"⏱ <b>ᴡᴀᴋᴛᴜ ᴘʀᴏꜱᴇꜱ:</b> {stop_time:.02f}s \n"
    await stat.edit(response)

@PY.UBOT(["ustat", "ustats", "deteksi"])
async def _(c, m):
    input_str = m.text.split(None, 1)[1] if len(m.command) > 1 else None
    reply_message = m.reply_to_message
    if not input_str and not reply_message:
        return await m.reply("<b>ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ᴍᴀꜱᴜᴋᴋᴀɴ ᴜꜱᴇʀɴᴀᴍᴇ/ɪᴅ!</b>")
    if input_str:
        try:
            uid = int(input_str)
        except ValueError:
            try:
                u = await c.get_users(input_str)
                uid = u.id
            except Exception:
                return await m.reply("<b>ᴍᴀꜱᴜᴋᴋᴀɴ ᴜꜱᴇʀɴᴀᴍᴇ/ɪᴅ ʏᴀɴɢ ᴠᴀʟɪᴅ!</b>")
    else:
        uid = reply_message.from_user.id
    chat = "@tgscanrobot"
    proses = await m.reply("<b>ᴍᴇɴɢᴀᴍʙɪʟ ʀɪᴡᴀʏᴀᴛ ɢʀᴏᴜᴘ ᴄᴇꜱꜱ...</b>")
    try:
        async with c.conversation(chat) as conv:
            msg = await conv.send_message(str(uid))
            response = await conv.get_response()
            await c.send_read_action(conv.chat_id, "typing")
            await proses.edit(response.text)
            await c.delete_messages(conv.chat_id, [msg.id, response.id])
    except Exception:
        await proses.edit("<b>ᴜɴʙʟᴏᴄᴋ @tgscanrobot ᴅᴀɴ ᴄᴏʙᴀ ʟᴀɢɪ ᴄᴇꜱꜱ!</b>")
