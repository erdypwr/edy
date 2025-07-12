from PyroUbot import *
from pyrogram.errors import PeerIdInvalid

__MODULE__ = "ɪɴꜰᴏ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ɪɴꜰᴏ 』</b>

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}info</code> [ɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴɢᴀᴍʙɪʟ ɪɴꜰᴏʀᴍᴀꜱɪ ᴘᴇɴɢɢᴜɴᴀ ᴛᴇʟᴇɢʀᴀᴍ
</blockquote>
"""

@PY.UBOT(["whois", "info"])
async def _(c, m):
    xx = await m.reply("<b>ᴍᴇɴɢᴀᴍʙɪʟ ɪɴꜰᴏʀᴍᴀꜱɪ ᴘᴇɴɢɢᴜɴᴀ...</b>")
    try:
        if len(m.command) < 2:
            return await xx.edit("<b>ᴘᴇɴɢɢᴜɴᴀᴀɴ: <code>.ɪɴꜰᴏ &lt;ɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ&gt;</code></b>")
        users = m.text.split(" ", 1)[1]
        try:
            target = await c.get_users(users)
        except PeerIdInvalid:
            return await xx.edit("<b>ᴇʀʀᴏʀ: ᴜꜱᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ!</b>")
        name = target.first_name + (" " + target.last_name if target.last_name else "")
        uname = f"@{target.username}" if target.username else "⊗"
        dc_id = getattr(target, 'dc_id', '-')
        group_count = getattr(target, 'common_chats_count', '-')
        created_date = getattr(target, 'date', None)
        if created_date:
            created_date = created_date.strftime('%d-%m-%Y %H:%M:%S')
        else:
            created_date = '-'
        bio = getattr(target, 'bio', None) or getattr(target, 'about', '-')
        status = getattr(target, 'status', None)
        if status:
            if hasattr(status, 'was_online'):
                status_str = f"ᴛᴇʀᴀᴋʜɪʀ ᴏɴʟɪɴᴇ: {status.was_online.strftime('%d-%m-%Y %H:%M:%S')}"
            elif status.__class__.__name__ == 'UserStatusOnline':
                status_str = "ꜱᴇᴅᴀɴɢ ᴏɴʟɪɴᴇ"
            elif status.__class__.__name__ == 'UserStatusRecently':
                status_str = "ʙᴀʀᴜ ꜱᴀᴊᴀ ᴏɴʟɪɴᴇ"
            elif status.__class__.__name__ == 'UserStatusOffline':
                status_str = f"ᴏꜰꜰʟɪɴᴇ: {status.was_online.strftime('%d-%m-%Y %H:%M:%S')}"
            elif status.__class__.__name__ == 'UserStatusLastMonth':
                status_str = "ᴏɴʟɪɴᴇ ᴅᴀʟᴀᴍ ꜱᴇʙᴜʟᴀɴ ᴛᴇʀᴀᴋʜɪʀ"
            elif status.__class__.__name__ == 'UserStatusLastWeek':
                status_str = "ᴏɴʟɪɴᴇ ᴅᴀʟᴀᴍ ꜱᴇᴍɪɴɢɢᴜ ᴛᴇʀᴀᴋʜɪʀ"
            else:
                status_str = str(status)
        else:
            status_str = "-"
        out_str = (
            f"""
<b>⇒ ɪɴꜰᴏʀᴍᴀꜱɪ ᴘᴇɴɢɢᴜɴᴀ ⇐</b>

<b>ɴᴀᴍᴀ:</b> <code>{name}</code>
<b>ᴜꜱᴇʀɴᴀᴍᴇ:</b> {uname}
<b>ᴜꜱᴇʀ ɪᴅ:</b> <code>{target.id}</code>
<b>ᴅᴄ ɪᴅ:</b> <code>{dc_id}</code>
<b>ʙɪᴏ:</b> <code>{bio}</code>
<b>ꜱᴛᴀᴛᴜꜱ:</b> <code>{status_str}</code>
<b>ᴊᴜᴍʟᴀʜ ɢʀᴜᴘ ᴅᴀɴ ᴄʜᴀɴɴᴇʟ:</b> <code>{group_count}</code>
<b>ᴛᴀɴɢɢᴀʟ ᴀᴋᴜɴ ᴅɪʙᴜᴀᴛ:</b> <code>{created_date}</code>
<b>ᴘʀᴇᴍɪᴜᴍ:</b> <code>{getattr(target, 'is_premium', False)}</code>
<b>ᴘʀᴏꜰɪʟ:</b> <a href='tg://user?id={target.id}'>{name}</a>
"""
        )
        await xx.edit(out_str)
    except Exception as ex:
        return await xx.edit(f"<b>ᴇʀʀᴏʀ: {ex}</b>")
