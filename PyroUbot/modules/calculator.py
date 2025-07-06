import ast
from pyrogram import Client, filters
from PyroUbot import PY

__MODULE__ = "ᴄᴀʟᴄᴜʟᴀᴛᴏʀ"
__HELP__ = """
<blockquote><b>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴋᴀʟᴋᴜʟᴀᴛᴏʀ</b>

ᴘᴇʀɪɴᴛᴀʜ:
<code>{0}ᴄᴀʟᴄ [ᴇᴋꜱᴘʀᴇꜱɪ]</code> → ᴍᴇɴɢʜɪᴛᴜɴɢ ᴇᴋꜱᴘʀᴇꜱɪ ᴍᴀᴛᴇᴍᴀᴛɪᴋᴀ  
ᴄᴏɴᴛᴏʜ: <code>.ᴄᴀʟᴄ 5 + 10 * 2</code>

ꜰɪᴛᴜʀ ɪɴɪ ʙɪꜱᴀ ᴅɪɢᴜɴᴀᴋᴀɴ ᴏʟᴇʜ ꜱɪᴀᴘᴀ ꜱᴀᴊᴀ.</blockquote></b>
"""

@PY.UBOT("calc")
@PY.TOP_CMD
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        return await message.reply("❌ ꜰᴏʀᴍᴀᴛ ꜱᴀʟᴀʜ! ɢᴜɴᴀᴋᴀɴ: <code>.ᴄᴀʟᴄ [ᴇᴋꜱᴘʀᴇꜱɪ]</code>")

    expression = args[1]

    try:
        # Parsing ekspresi dengan AST (Agar lebih aman)
        result = eval(compile(ast.parse(expression, mode="eval"), "<string>", "eval"))
        await message.reply(f"✅ ʜᴀꜱɪʟ: <code>{result}</code>")
    except Exception as e:
        await message.reply(f"❌ ᴇʀʀᴏʀ: {str(e)}")