from base64 import b64decode as kc
from random import choice

import requests
from pyrogram import filters


from PyroUbot import *

__MODULE__ = "ᴄᴇᴋ ɪᴘ ᴀᴅʀᴇss"
__HELP__ = """
<blockquote><b>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴇᴋ ɪᴘ ᴀᴅʀᴇss ᴄᴇss</b>

ᴘᴇʀɪɴᴛᴀʜ: <code>{0}ipaddress</code> [ɪᴘ ᴀᴅᴅʀᴇss]
ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴀʟᴀᴍᴀᴛ ɪᴘ ᴅᴀʀɪ ɪᴘ ᴀᴅᴅʀᴇss ʏᴀɴɢ ᴅɪʙᴇʀɪᴋᴀɴ ᴄᴇss</blockquote></b>
"""

@PY.UBOT("ipaddress")
@PY.TOP_CMD
async def hacker_lacak_target(client, message):
    apikey = kc("M0QwN0UyRUFBRjU1OTQwQUY0NDczNEMzRjJBQzdDMUE=").decode("utf-8")
    ran = await message.reply_text("<code>ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ</code>")
    ipddres = message.text.split(None, 1)[1] if len(message.command) != 1 else None
    if not ipddres:
        await ran.edit_text(
            "ᴇxᴀᴍᴘʟᴇ: <code>+ipaddress ʏᴏᴜʀ ɪᴘ ᴀᴅᴅʀᴇss ʜᴇʀᴇ : 1592.401.xxx</code>"
        )
        return

    if not apikey:
        await ran.edit_text("ʟᴏᴋᴀsɪ ɪᴘ ᴀᴘɪᴋᴇʏ ʜɪʟᴀɴɢ ᴄᴇss")
        return

    location_link = "https"
    location_api = "api.ip2location.io"
    location_key = f"key={apikey}"
    location_search = f"ip={ipddres}"
    location_param = (
        f"{location_link}://{location_api}/?{location_key}&{location_search}"
    )
    response = requests.get(location_param)
    if response.status_code == 200:
        data_location = response.json()
        try:
            location_ip = data_location["ip"]
            location_code = data_location["country_code"]
            location_name = data_location["country_name"]
            location_region = data_location["region_name"]
            location_city = data_location["city_name"]
            location_zip = data_location["zip_code"]
            location_zone = data_location["time_zone"]
            location_card = data_location["as"]
        except Exception as e:
            await ran.edit_text(f"ᴇʀʀᴏʀ ʀᴇQᴜᴇsᴛ ᴄᴇss {e}")
            return
        if (
            location_ip
            and location_code
            and location_name
            and location_region
            and location_city
            and location_zip
            and location_zone
            and location_card
        ):
            location_target = ""
            location_target += f"<b>IP address:</b> {location_ip}\n"
            location_target += f"<b>Country code:</b> {location_code}\n"
            location_target += f"<b>Country name:</b> {location_name}\n"
            location_target += f"<b>Region name:</b> {location_region}\n"
            location_target += f"<b>City name:</b> {location_city}\n"
            location_target += f"<b>Zip code:</b> {location_zip}\n"
            location_target += f"<b>Time Zone:</b> {location_zone}\n"
            location_target += f"<b>Data card:</b> {location_card}\n"
            await ran.edit_text(location_target)
        else:
            await ran.edit_text("ɴᴏᴛ ᴅᴀᴛᴀ ɪᴘ ᴀᴅᴅʀᴇss")
    else:
        await ran.edit_text(
            "ᴍᴀᴀꜰ, ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ sᴀᴀᴛ ᴍᴇᴍᴘʀᴏsᴇs ᴘᴇʀᴍɪɴᴛᴀᴀɴ ᴇʟᴜ. sɪʟᴀᴋᴀɴ ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ ᴄᴇss"
        )
