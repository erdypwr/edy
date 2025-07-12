from datetime import datetime as dt
from pytz import country_names as c_n, country_timezones as c_tz, timezone as tz
from PyroUbot import *

__MODULE__ = "ᴡᴀᴋᴛᴜ-ᴛᴀɴɢɢᴀʟ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴡᴀᴋᴛᴜ-ᴛᴀɴɢɢᴀʟ ᴄᴇꜱꜱ 』</b>

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}negara</code> [ɴᴀᴍᴀ ɴᴇɢᴀʀᴀ] [ɴᴏᴍᴏʀ ᴢᴏɴᴀ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴᴀᴍᴘɪʟᴋᴀɴ ᴡᴀᴋᴛᴜ ᴅᴀɴ ᴛᴀɴɢɢᴀʟ ᴅɪ ɴᴇɢᴀʀᴀ/ᴢᴏɴᴀ ᴛᴇʀᴛᴇɴᴛᴜ
</blockquote>
"""

def get_tz(con):
    for c_code in c_n:
        if con == c_n[c_code]:
            return c_tz[c_code]
    try:
        if c_n[con]:
            return c_tz[con]
    except KeyError:
        return

@PY.UBOT(["negara"])
async def _(c, m):
    args = m.text.split()
    con = args[1].title() if len(args) > 1 else ""
    tz_num = int(args[2]) if len(args) > 2 and args[2].isdigit() else None
    t_form = "%H:%M"
    d_form = "%d/%m/%y - %A"
    if con:
        timezones = get_tz(con)
    else:
        now = dt.now()
        await m.reply(f"<b>ꜱᴇᴋᴀʀᴀɴɢ ᴊᴀᴍ</b> <code>{now.strftime(t_form)}</code>\n<b>ꜱᴇᴋᴀʀᴀɴɢ ᴛᴀɴɢɢᴀʟ</b> <code>{now.strftime(d_form)}</code> <b>ᴅɪꜱɪɴɪ</b>")
        return
    if not timezones:
        await m.reply("<b>ɴᴇɢᴀʀᴀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ!</b>")
        return
    if len(timezones) == 1:
        time_zone = timezones[0]
    elif len(timezones) > 1:
        if tz_num:
            time_zone = timezones[tz_num - 1]
        else:
            return_str = f"<b>{con} ᴘᴜɴʏᴀ ʙᴇʙᴇʀᴀᴘᴀ ᴢᴏɴᴀ ᴡᴀᴋᴛᴜ:</b>\n\n"
            for i, item in enumerate(timezones):
                return_str += f"{i+1}. <code>{item}</code>\n"
            return_str += "\n<code>ᴘɪʟɪʜ ᴅᴇɴɢᴀɴ ᴍᴇɴɢᴇᴛɪᴋ ɴᴏᴍᴏʀɴʏᴀ ᴅɪ ᴘᴇʀɪɴᴛᴀʜ.</code>\n"
            return_str += f"ᴄᴏɴᴛᴏʜ: .negara {con} 2"
            await m.reply(return_str)
            return
    now = dt.now(tz(time_zone))
    await m.reply(f"<b>ꜱᴇᴋᴀʀᴀɴɢ ᴊᴀᴍ</b> <code>{now.strftime(t_form)}</code>\n<b>ꜱᴇᴋᴀʀᴀɴɢ ᴛᴀɴɢɢᴀʟ</b> <code>{now.strftime(d_form)}</code> <b>ᴅɪ {con} ({time_zone})</b>")
