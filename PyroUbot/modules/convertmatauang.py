import requests
from pyrogram import Client, filters
from PyroUbot import PY
from pyrogram.types import Message

__MODULE__ = "ᴄᴏɴᴠᴇʀᴛ ᴄᴜʀʀᴇɴᴄʏ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴋᴏɴᴠᴇʀsɪ ᴍᴀᴛᴀ ᴜᴀɴɢ 』

ᴘᴇʀɪɴᴛᴀʜ:
<code>{0}ᴄᴏɴᴠᴇʀᴛ 10000 ɪᴅʀ ᴜꜱᴅ</code> → ᴍᴇɴɢᴜʙᴀʜ 10.000 ɪᴅʀ ᴋᴇ ᴜꜱᴅ ᴄᴇss.

ꜱᴜᴍʙᴇʀ: ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴀᴘɪ ᴇxᴄʜᴀɴɢᴇ ʀᴀᴛᴇ ᴄᴇss.</b></blockquote>

"""

API_URL = "https://api.exchangerate-api.com/v4/latest/"

@PY.UBOT("convert")
@PY.TOP_CMD
async def convert_currency(client: Client, message: Message):
    args = message.text.split()
    
    if len(args) != 4:
        return await message.reply("❌ ꜰᴏʀᴍᴀᴛ sᴀʟᴀʜ! ɢᴜɴᴀᴋᴀɴ: `/convert [jumlah] [dari] [ke]`.\n\nᴄᴏɴᴛᴏʜ: `/convert 10000 idr usd`")

    try:
        amount = float(args[1])
        from_currency = args[2].upper()
        to_currency = args[3].upper()

        # Ambil data nilai tukar terbaru
        response = requests.get(f"{API_URL}{from_currency}")
        data = response.json()

        if "rates" not in data:
            return await message.reply("⚠️ ᴍᴀᴛᴀ ᴜᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴀᴛᴀᴜ ᴛɪᴅᴀᴋ ᴅɪᴅᴜᴋᴜɴɢ ᴄᴇss!")

        # Hitung konversi
        if to_currency not in data["rates"]:
            return await message.reply("⚠️ ᴍᴀᴛᴀ ᴜᴀɴɢ ᴛᴜᴊᴜᴀɴ ᴛɪᴅᴀᴋ ᴛᴇʀsᴇᴅɪᴀ ᴄᴇss!")

        converted_amount = amount * data["rates"][to_currency]
        await message.reply(f"💰 **ᴋᴏɴᴠᴇʀsɪ ᴍᴀᴛᴀ ᴜᴀɴɢ ᴄᴇss** 💱\n\n💵 {amount} {from_currency} ≈ **{converted_amount:.2f} {to_currency}**")

    except ValueError:
        await message.reply("❌ ᴊᴜᴍʟᴀʜ ʜᴀʀᴜs ʙᴇʀᴜᴘᴀ ᴀɴɢᴋᴀ ᴄᴇss!")
    except Exception as e:
        await message.reply(f"⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ᴄᴇss: {e}")