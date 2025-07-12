# 🍀 © @tofik_dn
# ⚠️ Do not remove credits
import requests
from googletrans import Translator
from PyroUbot import *
from PyroUbot.modules.sql_helper.tede_chatbot_sql import is_tede, rem_tede, set_tede

__MODULE__ = "ᴄʜᴀᴛʙᴏᴛ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄʜᴀᴛʙᴏᴛ ᴄᴇꜱꜱ 』</b>

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}chatbot</code> <on/off>
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴɢᴀᴋᴛɪꜰᴋᴀɴ/ᴍᴇɴᴏɴᴀᴋᴛɪꜰᴋᴀɴ ᴄʜᴀᴛʙᴏᴛ ᴀɪ ᴅɪ ɢʀᴏᴜᴘ/ᴘʀɪʙᴀᴅɪ
</blockquote>
"""

translator = Translator()
LANGUAGE = "id"
url = "https://api-tede.herokuapp.com/api/chatbot?message={message}"

def get_chatbot_reply(message):
    hayulo_link_apa = url.format(message=message)
    try:
        data = requests.get(hayulo_link_apa)
        if data.status_code == 200:
            return data.json().get("msg")
    except Exception:
        return None
    return None

@PY.UBOT(["chatbot"])
async def _(c, m):
    if len(m.command) < 2:
        return await m.reply("<b>ᴘᴇɴɢɢᴜɴᴀᴀɴ: <code>.chatbot on/off</code></b>")
    status = m.command[1].lower()
    chat_id = m.chat.id
    if status == "on":
        if not is_tede(chat_id):
            set_tede(chat_id)
            return await m.reply("<b>ᴄʜᴀᴛʙᴏᴛ ʙᴇʀʜᴀꜱɪʟ ᴅɪᴀᴋᴛɪꜰᴋᴀɴ!</b>")
        return await m.reply("<b>ᴄʜᴀᴛʙᴏᴛ ꜱᴜᴅᴀʜ ᴀᴋᴛɪꜰ.</b>")
    elif status == "off":
        if is_tede(chat_id):
            rem_tede(chat_id)
            return await m.reply("<b>ᴄʜᴀᴛʙᴏᴛ ʙᴇʀʜᴀꜱɪʟ ᴅɪɴᴏɴᴀᴋᴛɪꜰᴋᴀɴ!</b>")
        return await m.reply("<b>ᴄʜᴀᴛʙᴏᴛ ꜱᴜᴅᴀʜ ᴅɪɴᴏɴᴀᴋᴛɪꜰᴋᴀɴ.</b>")
    else:
        return await m.reply("<b>ᴘᴇɴɢɢᴜɴᴀᴀɴ: <code>.chatbot on/off</code></b>")

@PY.UBOT(incoming=True, group_only=False)
async def _(c, m):
    if not m.text or not is_tede(m.chat.id):
        return
    if m.from_user and m.from_user.is_self:
        return
    rep = get_chatbot_reply(m.text)
    if rep:
        tr = translator.translate(rep, LANGUAGE)
        await m.reply(tr.text)
