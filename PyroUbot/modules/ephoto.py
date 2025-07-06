import os
from PyroUbot import *
import requests

__MODULE__ = "ᴇᴘʜᴏᴛᴏ"
__HELP__ = """**「 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍᴏᴅᴜʟᴇ ᴇᴘꜰᴏᴛᴏ ᴄᴇꜱꜱ 」**

𖠇➛ **ᴘᴇʀɪɴᴛᴀʜ: .television (ᴛᴇxᴛ)**
𖠇➛ **ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇxᴛ ᴛᴇʟᴇᴠɪꜱɪᴏɴ**

𖠇➛ **ᴘᴇʀɪɴᴛᴀʜ: .glasse (ᴛᴇxᴛ)**
𖠇➛ **ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇxᴛ ɢʟᴀꜱꜱᴇ**

𖠇➛ **ᴘᴇʀɪɴᴛᴀʜ: .blackpink (ᴛᴇxᴛ)**
𖠇➛ **ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇxᴛ ʙʟᴀᴄᴋᴘɪɴᴋ**

𖠇➛ **ᴘᴇʀɪɴᴛᴀʜ: .blackpink2 (ᴛᴇxᴛ)**
𖠇➛ **ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇxᴛ ʙʟᴀᴄᴋᴘɪɴᴋ2**

𖠇➛ **ᴘᴇʀɪɴᴛᴀʜ: .coverpubg (ᴛᴇxᴛ)**
𖠇➛ **ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇxᴛ ʙʟᴀᴄᴋᴘɪɴᴋ2**

𖠇➛ **ᴘᴇʀɪɴᴛᴀʜ: .hororr (ᴛᴇxᴛ)**
𖠇➛ **ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇxᴛ ʜᴏʀᴏʀʀʀ**"""

def tweet(text):
    url = "https://api.botcahx.eu.org/api/ephoto/televisi"
    params = {
        "text": text,
        "apikey": "045705b1"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None
        
def rob(text):
    url = "https://api.botcahx.eu.org/api/ephoto/coverpubg"
    params = {
        "text": text,
        "apikey": "045705b1"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None
        
def robottt(text):
    url = "https://api.botcahx.eu.org/api/ephoto/horor"
    params = {
        "text": text,
        "apikey": "045705b1"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def fb(text):
    url = "https://api.botcahx.eu.org/api/ephoto/blackpink"
    params = {
        "text": text,
        "apikey": "045705b1"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def fbs(text):
    url = "https://api.botcahx.eu.org/api/ephoto/blackpink2"
    params = {
        "text": text,
        "apikey": "045705b1"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def tweets(text):
    url = "https://api.botcahx.eu.org/api/ephoto/glasse"
    params = {
        "text": text,
        "apikey": "045705b1"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None

          
@PY.UBOT("hororr")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("ᴄᴏɴᴛᴏʜ : .ʜᴏʀᴏʀʀʀ ᴘᴇɴᴏ")
        return

    request_text = args[1]
    processing_msg = await message.edit("ʟᴏᴀᴅɪɪɪɴɢ..........")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▱▱▱▱▱ 𝟸𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▱▱▱▱ 𝟺𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▱▱▱ 𝟼𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▱▱ 𝟾𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▰▰ 𝟷𝟶𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("✦ sᴜᴄᴄᴇssғᴜʟʟʏ ✦")
    await asyncio.sleep(0.1)
    image_content = robottt(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("ᴀᴘɪᴋᴇʏ sᴇᴅᴀɴɢ ʙᴇʀᴍᴀsᴀʟᴀʜ ᴄᴇss")

@PY.UBOT("coverpubg")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("ᴄᴏɴᴛᴏʜ : .ᴄᴏᴠᴇʀᴘᴜʙɢ ᴘᴇɴᴏ")
        return

    request_text = args[1]
    processing_msg = await message.edit("ʟᴏᴀᴅɪɪɪɴɢ..........")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▱▱▱▱▱ 𝟸𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▱▱▱▱ 𝟺𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▱▱▱ 𝟼𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▱▱ 𝟾𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▰▰ 𝟷𝟶𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("✦ sᴜᴄᴄᴇssғᴜʟʟʏ ✦")
    await asyncio.sleep(0.1)
    image_content = rob(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("ᴀᴘɪᴋᴇʏ sᴇᴅᴀɴɢ ʙᴇʀᴍᴀsᴀʟᴀʜ ᴄᴇss")

@PY.UBOT("blackpink")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("ᴄᴏɴᴛᴏʜ : .ʙʟᴀᴄᴋᴘɪɴᴋ ᴘᴇɴᴏ")
        return

    request_text = args[1]
    processing_msg = await message.edit("ʟᴏᴀᴅɪɪɪɴɢ..........")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▱▱▱▱▱ 𝟸𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▱▱▱▱ 𝟺𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▱▱▱ 𝟼𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▱▱ 𝟾𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▰▰ 𝟷𝟶𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("✦ sᴜᴄᴄᴇssғᴜʟʟʏ ✦")
    await asyncio.sleep(0.1)
    image_content = fb(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("ᴀᴘɪᴋᴇʏ sᴇᴅᴀɴɢ ʙᴇʀᴍᴀsᴀʟᴀʜ ᴄᴇss")
@PY.UBOT("blackpink2")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("ᴄᴏɴᴛᴏʜ : .ʙʟᴀᴄᴋᴘɪɴᴋ ᴘᴇɴᴏ")
        return

    request_text = args[1]
    processing_msg = await message.edit("ʟᴏᴀᴅɪɪɪɴɢ..........")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▱▱▱▱▱ 𝟸𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▱▱▱▱ 𝟺𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▱▱▱ 𝟼𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▱▱ 𝟾𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▰▰ 𝟷𝟶𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("✦ sᴜᴄᴄᴇssғᴜʟʟʏ ✦")
    await asyncio.sleep(0.1)
    image_content = fbs(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("ᴀᴘɪᴋᴇʏ sᴇᴅᴀɴɢ ʙᴇʀᴍᴀsᴀʟᴀʜ ᴄᴇss")
@PY.UBOT("television")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("ᴄᴏɴᴛᴏʜ : .ᴛᴇʟᴇᴠɪsɪᴏɴ ᴘᴇɴᴏ")
        return

    request_text = args[1]
    processing_msg = await message.edit("ʟᴏᴀᴅɪɪɪɴɢ..........")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▱▱▱▱▱ 𝟸𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▱▱▱▱ 𝟺𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▱▱▱ 𝟼𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▱▱ 𝟾𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▰▰ 𝟷𝟶𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("✦ sᴜᴄᴄᴇssғᴜʟʟʏ ✦")
    await asyncio.sleep(0.1)
    image_content = tweet(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("ᴀᴘɪᴋᴇʏ sᴇᴅᴀɴɢ ʙᴇʀᴍᴀsᴀʟᴀʜ ᴄᴇss")

@PY.UBOT("glasse")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("ᴄᴏɴᴛᴏʜ : .ɢʟᴀssᴇ ᴘᴇɴᴏ")
        return

    request_text = args[1]
    processing_msg = await message.edit("ʟᴏᴀᴅɪɪɪɴɢ..........")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▱▱▱▱▱ 𝟸𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▱▱▱▱ 𝟺𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▱▱▱ 𝟼𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▱▱ 𝟾𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▰▰ 𝟷𝟶𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("✦ sᴜᴄᴄᴇssғᴜʟʟʏ ✦")
    await asyncio.sleep(0.1)
    image_content = tweets(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("ᴀᴘɪᴋᴇʏ sᴇᴅᴀɴɢ ʙᴇʀᴍᴀsᴀʟᴀʜ ᴄᴇss")
