import asyncio
import datetime

from PyroUbot import *

__MODULE__ = "ᴅᴏɴᴇ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴅᴏɴᴇ ᴄᴇꜱꜱ 』</b>

• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}ᴅᴏɴᴇ</code> <b>[ɴᴀᴍᴇ ɪᴛᴇᴍ],[ʜᴀʀɢᴀ] [ᴘᴇᴍʙᴀʏᴀʀᴀɴ]</b>
• <b>ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴋᴏɴꜰɪʀᴍᴀꜱɪ ᴘᴇᴍʙᴀʏᴀʀᴀɴ.</blockquote></b>

"""


@PY.UBOT("done")
async def done_command(client, message):
    izzy_ganteng = await message.reply("<blockquote>ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...</blockquote>")
    await asyncio.sleep(5)
    try:
        args = message.text.split(" ", 1)
        if len(args) < 2 or "," not in args[1]:
            await message.reply_text("<blockquote>Penggunaan: .done name item,price,payment</blockquote>")
            return

        parts = args[1].split(",", 2)

        if len(parts) < 2:
            await message.reply_text("<blockquote>Penggunaan: .done name item,price,payment</blockquote>")
            return

        name_item = parts[0].strip()
        price = parts[1].strip()
        payment = parts[2].strip() if len(parts) > 2 else "Lainnya"
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = (
            f"<blockquote>「 𝗧𝗥𝗔𝗡𝗦𝗔𝗞𝗦𝗜 𝗕𝗘𝗥𝗛𝗔𝗦𝗜𝗟 」\n</blockquote>"
            f"<blockquote>📦 <b>ʙᴀʀᴀɴɢ : {name_item}</b>\n"
            f"💸 <b>ʜᴀʀɢᴀ : {price}</b>\n"
            f"🕰️ <b>ᴡᴀᴋᴛᴜ : {time}</b>\n"
            f"💳 <b>ᴘᴇᴍʙᴀʏᴀʀᴀɴ : {payment}</b>\n</blockquote>"
            f"<blockquote>ᴛᴇʀɪᴍᴀᴋᴀsɪʜ ᴛᴇʟᴀʜ ᴏʀᴅᴇʀ</blockquote>"
        )
        await izzy_ganteng.edit(response)

    except Exception as e:
        await izzy_ganteng.edit(f"error: {e}")