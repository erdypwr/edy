from PyroUbot import *
from pyrogram.enums import ChatType, ChatMemberStatus


__MODULE__ = " 𝙶𝙲𝙰𝚂𝚃 𝙽𝙴𝚆"
__HELP__ = f"""
<b>『 Bantuan Untuk Gcastnew Cess 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>.bc</code> gc balas ke pesan
  <b>• penjelasan:</b> gc[grup], adm[khusus admin], pv [private chat]

"""

def get_message(message):
    msg = (
        message.reply_to_message
        if message.reply_to_message
        else ""
        if len(message.command) < 2
        else " ".join(message.command[1:])
    )
    return msg
    
@PY.UBOT("bc")
async def _(c, m):
    done = 0
    if len(m.command) != 2:
        await m.reply(f"**<emoji id =5929358014627713883>❌</emoji> Mohon Gunakan Format Cess: bc [gc adm pv] **")
        return
    send = get_message(m)
    if not send:
        await m.reply_text(f"<emoji id=5911461474315802019>⭐</emoji> **Mohon Balas Ke Pesan Cess** !", quote=True)
        return
    if not m.reply_to_message:
        await m.reply_text(f"<emoji id=5911461474315802019>⭐</emoji> **Mohon Balas Ke Pesan Cess** !", quote=True)
        return
    blacklist = await c.get_chat(c.me.id)
    try:
        if m.command[1] == "gc":
            Haku = await m.reply(f"<emoji id=6010111371251815589>⏳</emoji> **Prossess Cess...**")
            async for dialog in c.get_dialogs():
                if dialog.chat.type in (ChatType.SUPERGROUP, ChatType.GROUP):
                    chat_id = dialog.chat.id
                    await asyncio.sleep(0.1)
                    if chat_id not in blacklist:
                        try:
                            await send.copy(chat_id)
                            done += 1
                        except Exception:
                            pass

            await Haku.edit(
                f"<emoji id =5888974760720732797>💥</emoji> **berhasil mengirim ke {done} grup** <emoji id=5798623990436074786>✅</emoji>\n\n"
                f"<emoji id =5888974760720732797>💥</emoji> **powered by @ʏᴅʜɪᴀᴋ** <emoji id =5895583431194054511>🌟</emoji>\n")

        elif m.command[1] == "pv":
            Haku = await m.reply(f"<emoji id=6010111371251815589>⏳</emoji> **Prossess Cess...**")
            async for dialog in c.get_dialogs():
                if dialog.chat.type == ChatType.PRIVATE:
                    chat_id = dialog.chat.id
                    await asyncio.sleep(0.1)
                    if chat_id not in blacklist:
                        try:
                            await send.copy(chat_id)
                            done += 1
                        except Exception:
                            pass

            await Haku.edit(
                f"<emoji id =5888974760720732797>💥</emoji> **Berhasil Mengirim Ke {done} Chat Pribadi Cess** <emoji id=5798623990436074786>✅</emoji>\n\n"
                f"<emoji id =5888974760720732797>💥</emoji> **Powered By @ʏᴅʜɪᴀᴋ** <emoji id =5895583431194054511>🌟</emoji>\n")

        elif m.command[1] == "adm":
            Haku = await m.reply(f"<emoji id=6010111371251815589>⏳</emoji> **Prossess Cess...**")
            async for dialog in c.get_dialogs():
                if dialog.chat.type in (ChatType.SUPERGROUP, ChatType.GROUP):
                    chat_id = dialog.chat.id
                    await asyncio.sleep(0.1)
                    try:
                        member = await c.get_chat_member(chat_id, "me")
                        if member.status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
                            await send.copy(chat_id)
                            done += 1
                    except Exception:
                        pass
            await Haku.edit(
                f"<emoji id =5888974760720732797>💥</emoji> **Berhasil Mengirim Ke {done} Khusus Admin Cess** <emoji id=5798623990436074786>✅</emoji>\n\n"
                f"<emoji id =5888974760720732797>💥</emoji> **powered by @ʏᴅʜɪᴀᴋ** <emoji id =5895583431194054511>🌟</emoji>\n")


    except IndexError:
        await m.reply(f"<emoji id =5929358014627713883>❌</emoji>**Mohon Gunakan BC gc/adm/pv Balas Ke Pesan Cess**")
