import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "ᴄᴜᴀᴄᴀ"
__HELP__ = """
<blockquote><b>『 ᴄᴜᴀᴄᴀ 』</b>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}ᴄᴜᴀᴄᴀ</code>
   <i>ᴘᴇɴᴊᴇʟᴀꜱᴀɴ ᴄᴇꜱꜱ:</b> ᴄᴇᴋ ɪɴꜰᴏ ᴄᴜᴀᴄᴀ ᴅɪ ᴋᴏᴛᴀ ᴋᴏᴛᴀ ʙᴇꜱᴀʀ ᴄᴇꜱꜱ.</i>
』</b></blockquote>

"""

@PY.UBOT("cuaca")
async def cuaca(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)

    jalan = await message.reply(f"{prs} ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    a = message.text.split(' ', 1)[1]
    chat_id = message.chat.id
    url = f"https://api.betabotz.eu.org/api/tools/cuaca?query={a}&apikey=Btz-bxwol"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            hasil = data['result']
            location = hasil['location']
            country = hasil['country']
            weather = hasil['weather']
            currentTemp = hasil['currentTemp']
            maxTemp = hasil['maxTemp']
            minTemp = hasil['minTemp']
            humidity = hasil['humidity']
            windSpeed = hasil['windSpeed']
            photoUrl = f"https://telegra.ph//file/9354c197366cde09650fd.jpg"
            caption = f"""
<blockquote>╭─ •  「 <b>Info Cuaca Terkini Cess</b> 」
│  ◦ <b>ᴋᴏᴛᴀ: <code>{location}</code></b>
│  ◦ <b>ɴᴇɢᴀʀᴀ: <code>{country}</code></b>
│  ◦ <b>ᴄᴜᴀᴄᴀ: <code>{weather}</code></b>
│  ◦ <b>sᴜʜᴜ sᴀᴀᴛ ɪɴɪ: <code>{currentTemp}</code></b>
│  ◦ <b>sᴜʜᴜ ᴍᴀᴋs/ᴍɪɴ: <code>{maxTemp}, {minTemp}</code></b>
│  ◦ <b>ᴋᴇᴄᴇᴘᴀᴛᴀɴ ᴀɴɢɪɴ: <code>{windSpeed}</code></b></blockquote>
╰──── •
"""
            photo_path = wget.download(photoUrl)
            await client.send_photo(chat_id, caption=caption, photo=photo_path)
            if os.path.exists(photo_path):
                os.remove(photo_path)
            
            await jalan.delete()
        else:
            await jalan.edit(f"{ggl} Tidak Ada Kunci 'Hasil' Yang Ditemukan Dalam Respons Cess.")

    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} Permintaan Gagal Cess: {e}")

    except Exception as e:
        await jalan.edit(f"{ggl} Terjadi Kesalahan Cess: {e}")
