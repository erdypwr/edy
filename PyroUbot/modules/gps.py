from geopy.geocoders import Nominatim
from PyroUbot import *

__MODULE__ = "ɢᴍᴀᴘs"
__HELP__ = """
<b>✮ꜰᴏʟᴅᴇʀ ᴜɴᴛᴜᴋ ᴍᴀᴘs ᴄᴇss✮</b>

<blockquote><b>♛ᴘᴇʀɪɴᴛᴀʜ : <code>{0}gps</code>
ᴘᴇɴᴊᴇʟᴀsᴀɴ : ʙᴜᴀᴛ ᴍᴇɴᴄᴀʀɪ ʟᴏᴋᴀsɪ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴍᴀᴘs ᴄᴇss/ɢᴘs</b></blockquote>
"""

@PY.UBOT("gps|maps")
async def gps(client, message):
    input_str = message.text.split(" ", 1)
    
    if len(input_str) < 2:
        return await message.reply("<blockquote><b>ᴍᴏʜᴏɴ ʙᴇʀɪᴋᴀɴ ᴛᴇᴍᴘᴀᴛ ʏᴀɴɢ ᴅɪᴄᴀʀɪ ᴄᴇss.</b></blockquote>")

    input_str = input_str[1]
    await message.reply("<blockquote><b>ᴍᴇɴᴇᴍᴜᴋᴀɴ ʟᴏᴋᴀsɪ ɪɴɪ ᴅɪ sᴇʀᴠᴇʀ ᴍᴀᴘ ᴄᴇss...</b></blockquote>")

    geolocator = Nominatim(user_agent="bot")
    geoloc = geolocator.geocode(input_str)
    
    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await message.reply_location(latitude=lat, longitude=lon)
    else:
        await message.reply("<blockquote><b>`ɢᴜᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴɴʏᴀ ᴄᴇss`.</b></blockquote>")
