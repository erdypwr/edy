import re
import aiohttp
from PyroUbot import *
from pyrogram.types import Message

__MODULE__ = "ꜱᴜʙғɪɴᴅᴇʀ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱᴜʙғɪɴᴅᴇʀ ᴄᴇꜱꜱ 』

 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ꜱᴜʙꜰɪɴ</code>
 ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴄᴇᴋ ꜱᴜʙᴅᴏᴍᴀɪɴ ᴅᴀʀɪ ᴅᴏᴍᴀɪɴ ᴜᴛᴀᴍᴀ</b></blockquote>
"""

async def get_subdomains(domain):
    """Mengambil daftar subdomain dari API."""
    params = {"query": domain, "apikey": API_KEY}
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL, params=params) as response:
            if response.status == 200:
                data = await response.json()
                if data.get("status") and "result" in data:
                    return data["result"]
    return None

@PY.UBOT("subfin")
@PY.TOP_CMD
async def subfinder(client, message):
    command_parts = message.text.split(maxsplit=1)

    if len(command_parts) < 2:
        await message.reply("ᴄᴏɴᴛᴏʜ: .ꜱᴜʙꜰɪɴ ᴄᴏɴᴛᴏʜ.ᴄᴏᴍ")
        return

    domain = command_parts[1].strip()

    if not re.match(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", domain):
        await message.reply("ᴅᴏᴍᴀɪɴ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ.")
        return

    processing_msg = await message.reply(f"`ᴘʀᴏꜱᴇꜱ ᴍᴇɴᴄᴀʀɪ ꜱᴜʙᴅᴏᴍᴀɪɴ ᴅᴀʀɪ {domain}...`")

    subdomains = await get_subdomains(domain)

    await processing_msg.delete()  

    if subdomains:
        result_text = f"**ꜱᴜʙᴅᴏᴍᴀɪɴ {domain}:**\n\n"
        result_text += "\n".join(f"- `{sub}`" for sub in subdomains)
        await message.reply(result_text)
    else:
        await message.reply("ɢᴀɢᴀʟ ᴍᴇɴᴄᴀʀɪ ꜱᴜʙᴅᴏᴍᴀɪɴ ᴅᴀʀɪ {domain}.")  # noqa: E501

API_KEY = "025a6ef0" 
API_URL = "https://api.botcahx.eu.org/api/tools/subdomain-finder"
