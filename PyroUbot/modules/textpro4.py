import os
import requests
from PyroUbot import *

# Masukkan API Key Anda di sini
API_KEY = "Btz-bxwol"  # Ganti dengan API key yang benar

__MODULE__ = "ᴛᴇxᴛᴘʀᴏ 4"
__HELP__ = """
<b>TextPro 4 Commands</b>

<blockquote><b>Perintah : <code>letters</code>
Penjelasan : Membuat gambar dengan efek letters.</b></blockquote>
<blockquote><b>Perintah : <code>dragonfire</code>
Penjelasan : Membuat gambar dengan efek Paper Cut.</b></blockquote>
"""

def fetch_image(api_url, text):
    """
    Fungsi untuk mengambil gambar dari API
    """
    params = {"text": text, "apikey": API_KEY}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()

        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            print("Response bukan gambar:", response.text)  # Debugging
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image: {e}")  # Debugging jika ada kesalahan
        return None

async def process_image_command(client, message, api_url, command_name):
    """
    Fungsi umum untuk menangani perintah pembuatan gambar
    """
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text(f"<b><i>Gunakan perintah /{command_name} <teks> untuk membuat gambar.</i></b>")
        return

    request_text = args[1]
    await message.reply_text("<b><i>Sedang memproses, mohon tunggu...</i></b>")

    image_content = fetch_image(api_url, request_text)
    if image_content:
        temp_file = f"{command_name}.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)
        await message.reply_photo(photo=temp_file)
        os.remove(temp_file)
    else:
        await message.reply_text("Gagal Membuat Gambar. Coba Lagi Nanti Cess")

# Handler untuk setiap perintah
@PY.UBOT("letters")
async def letters_command(client, message):
    api_url = "https://api.betabotz.eu.org/api/ephoto/letters"
    await process_image_command(client, message, api_url, "letters")

@PY.UBOT("dragonfire")
async def dragonfire_command(client, message):
    api_url = "https://api.betabotz.eu.org/api/ephoto/dragonfire"
    await process_image_command(client, message, api_url, "dragonfire")
