import re
from pyrogram import *
from pyrogram import Client, filters
from PyroUbot import PY

__MODULE__ = "ᴛᴏᴏʟs ʀᴇᴋᴀᴘ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʀᴇᴋᴀᴘ & ᴡɪɴ ᴄᴇꜱꜱ 』</b>

ᴘᴇʀɪɴᴛᴀʜ:
<code>{0}ʀᴇᴋᴀᴘ</code> → ʀᴇᴋᴀᴘ ꜱᴀʟᴅᴏ ᴅᴀʀɪ ᴘᴇꜱᴀɴ ʏᴀɴɢ ᴅɪʀᴇᴘʟʏ.  
<code>{0}ᴡɪɴ 5</code> → ʜɪᴛᴜɴɢ ᴋᴇᴍᴇɴᴀɴɢᴀɴ ᴅᴇɴɢᴀɴ ꜰᴇᴇ 5% (ɢᴀɴᴛɪ ᴀɴɢᴋᴀ ꜱᴇꜱᴜᴀɪ ᴋᴇʙᴜᴛᴜʜᴀɴ).  

ꜰɪᴛᴜʀ ɪɴɪ ʙᴇʀɢᴜɴᴀ ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀᴛᴀᴛ ᴘᴇʀʙᴀɴᴅɪɴɢᴀɴ ꜱᴀʟᴅᴏ ᴅɪ ɢʀᴜᴘ ᴀᴛᴀᴜ ᴄʜᴀᴛ ᴘʀɪʙᴀᴅɪ.</blockquote></b>
"""

def rekap_data(text):
    kecil = []
    besar = []
    kecil_total = 0
    besar_total = 0

    for match in re.finditer(r"(\w+)\s*:\s*(\d+)", text):
        nama, nominal = match.groups()
        nominal = int(nominal)

        if nama.lower() in ["k", "kecil"]:
            kecil.append({"nama": nama, "nominal": nominal})
            kecil_total += nominal
        elif nama.lower() in ["b", "besar"]:
            besar.append({"nama": nama, "nominal": nominal})
            besar_total += nominal

    return {"kecil": kecil, "besar": besar, "kecil_total": kecil_total, "besar_total": besar_total}

def format_number(num):
    return f"{num:,}".replace(",", ".")

@PY.UBOT("rekap")
@PY.TOP_CMD
async def rekap_command(client, message):
    if not message.reply_to_message or not message.reply_to_message.text:
        return await message.reply("❌ ʀᴇᴘʟʏ ᴘᴇsᴀɴ ʏᴀɴɢ ʙᴇʀɪsɪ ᴅᴀᴛᴀ ᴜɴᴛᴜᴋ ᴍᴇʀᴇᴋᴀᴘ ᴄᴜᴋɪ.")

    text = message.reply_to_message.text
    data = rekap_data(text)
    kecil, besar = data["kecil"], data["besar"]
    kecil_total, besar_total = data["kecil_total"], data["besar_total"]
    total_saldo = kecil_total + besar_total
    selisih = kecil_total - besar_total

    if selisih > 0:
        analisis_selisih = f"⚖️ sᴀʟᴅᴏ: ʙᴇsᴀʀ ᴋᴇᴛɪɴɢɢᴀʟᴀɴ ᴄᴜᴋɪ {format_number(selisih)} ɴɪʜ!"
    elif selisih < 0:
        analisis_selisih = f"⚖️ sᴀʟᴅᴏ: ᴋᴇᴄɪʟ ᴋᴇᴛɪɴɢɢᴀʟᴀɴ ᴄᴜᴋɪ {format_number(abs(selisih))} ɴɪʜ!"
    else:
        analisis_selisih = "⚖️ sᴀʟᴅᴏ: ᴋᴇᴄɪʟ ᴅᴀɴ ʙᴇsᴀʀ sᴇɪᴍʙᴀɴɢ ɴɪʜ! 🎉"

    result = f"⚪ 𝗞 : [{', '.join(format_number(item['nominal']) for item in kecil)}] = {format_number(kecil_total)}\n\n"
    result += f"🔵 𝗕 : [{', '.join(format_number(item['nominal']) for item in besar)}] = {format_number(besar_total)}\n\n"
    result += f"{analisis_selisih}\n\n"
    result += f"💲 ᴛᴏᴛᴀʟ sᴀʟᴅᴏ: {format_number(total_saldo)} ᴋ"

    await message.reply(result)

def hitung_win(data, fee_percent):
    hasil = []
    for item in data:
        final_nominal = item["nominal"] - (item["nominal"] * fee_percent / 100)
        hasil.append({"nama": item["nama"], "nominal": item["nominal"], "final_nominal": round(final_nominal)})
    return hasil

@PY.UBOT("win")
@PY.TOP_CMD
async def win_command(client, message):
    args = message.text.split()
    if len(args) < 2 or not args[1].isdigit():
        return await message.reply("ғᴏʀᴍᴀᴛ: <code>.win 5</code>\nғᴇᴇ ʜᴀʀᴜs ᴀɴɢᴋᴀ ᴀɴᴛᴀʀᴀ 1-10% ᴄᴇss.")

    fee_percent = int(args[1])
    if fee_percent < 1 or fee_percent > 10:
        return await message.reply("❌ ғᴇᴇ ʜᴀʀᴜs ᴅɪ ᴀɴᴛᴀʀᴀ 1-10% ᴄᴇss.")

    if not message.reply_to_message or not message.reply_to_message.text:
        return await message.reply("❌ ʀᴇᴘʟʏ ᴘᴇsᴀɴ ʏᴀɴɢ ʙᴇʀɪsɪ ᴅᴀᴛᴀ ᴜɴᴛᴜᴋ ᴍᴇɴɢʜɪᴛᴜɴɢ ʜᴀsɪʟ ᴀᴋʜɪʀ ᴄᴇss.")

    text = message.reply_to_message.text
    data = rekap_data(text)
    hasil_kecil = hitung_win(data["kecil"], fee_percent)
    hasil_besar = hitung_win(data["besar"], fee_percent)

    result = "\n\n𝗞𝗘𝗖𝗜𝗟:\n"
    result += "\n".join(f"{item['nama']}: {format_number(item['nominal'])} // {format_number(item['final_nominal'])}" for item in hasil_kecil)

    result += "\n\n𝗕𝗘𝗦𝗔𝗥:\n"
    result += "\n".join(f"{item['nama']}: {format_number(item['nominal'])} // {format_number(item['final_nominal'])}" for item in hasil_besar)

    await message.reply(result)