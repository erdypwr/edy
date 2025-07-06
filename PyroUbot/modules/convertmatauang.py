import requests
from pyrogram import Client, filters
from PyroUbot import PY
from pyrogram.types import Message

__MODULE__ = "ᴄᴏɴᴠᴇʀᴛ ᴄᴜʀʀᴇɴᴄʏ"
__HELP__ = """
<blockquote><b>Bantuan Untuk Convert Currency Cess</b>

Perintah:
<code>{0}Convert 10000 IDR USD</code> → Mengubah 10.000 IDR Ke USD Cess.

Sumber: Menggunakan API Exchange Rate Cess.</blockquote></b>
"""

API_URL = "https://api.exchangerate-api.com/v4/latest/"

@PY.UBOT("convert")
@PY.TOP_CMD
async def convert_currency(client: Client, message: Message):
    args = message.text.split()
    
    if len(args) != 4:
        return await message.reply("❌ Format Salah! Gunakan: `/convert [Jumlah] [Dari] [Ke]`.\n\nContoh: `/convert 10000 IDR USD`")

    try:
        amount = float(args[1])
        from_currency = args[2].upper()
        to_currency = args[3].upper()

        # Ambil data nilai tukar terbaru
        response = requests.get(f"{API_URL}{from_currency}")
        data = response.json()

        if "rates" not in data:
            return await message.reply("⚠️ Mata Uang Tidak Ditemukan atau Tidak Didukung Cess!")

        # Hitung konversi
        if to_currency not in data["rates"]:
            return await message.reply("⚠️ Mata Uang Tujuan Tidak Tersedia Cess!")

        converted_amount = amount * data["rates"][to_currency]
        await message.reply(f"💰 **Konversi Mata Uang Cess** 💱\n\n💵 {amount} {from_currency} ≈ **{converted_amount:.2f} {to_currency}**")

    except ValueError:
        await message.reply("❌ Jumlah Harus Berupa Angka Cess!")
    except Exception as e:
        await message.reply(f"⚠️ Terjadi Kesalahan Cess: {e}")