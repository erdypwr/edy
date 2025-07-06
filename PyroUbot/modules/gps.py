from geopy.geocoders import Nominatim
from PyroUbot import *

__MODULE__ = "ɢᴍᴀᴘs"
__HELP__ = """
<b>✮Folder Untuk Maps Cess✮</b>

<blockquote><b>♛Perintah : <code>{0}gps</code>
Penjelasan : Buat Mencari Lokasi Menggunakan Maps Cess/Gps</b></blockquote>
"""

@PY.UBOT("gps|maps")
async def gps(client, message):
    input_str = message.text.split(" ", 1)
    
    if len(input_str) < 2:
        return await message.reply("<blockquote><b>Mohon Berikan Tempat Yang Dicari Cess.</b></blockquote>")

    input_str = input_str[1]
    await message.reply("<blockquote><b>Menemukan Lokasi Ini Di Server Map Cess...</b></blockquote>")

    geolocator = Nominatim(user_agent="bot")
    geoloc = geolocator.geocode(input_str)
    
    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await message.reply_location(latitude=lat, longitude=lon)
    else:
        await message.reply("<blockquote><b>`Gua Tidak Dapat Menemukannya Cess`.</b></blockquote>")
