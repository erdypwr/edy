import os
from PyroUbot import *
import requests

__MODULE__ = "ᴘʟᴀʏʙᴜᴛᴛᴏɴ"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘʟᴀʏʙᴜᴛᴛᴏɴ ᴄᴇꜱꜱ 』</b>
<blockquote><b>
⎆ ᴘᴇʀɪɴᴛᴀʜ :
ᚗ <code>{0}ʏᴛɢᴏʟᴅ</code>  
⊷ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ɢᴏʟᴅ ᴘʟᴀʏʙᴜᴛᴛᴏɴ ʏᴏᴜᴛᴜʙᴇ  

ᚗ <code>{0}ʏᴛsɪʟᴠᴇʀ</code>  
⊷ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ sɪʟᴠᴇʀ ᴘʟᴀʏʙᴜᴛᴛᴏɴ ʏᴏᴜᴛᴜʙᴇ  

ᚗ <code>{0}ɪɢɢᴏʟᴅ</code>  
⊷ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ɢᴏʟᴅ ᴘʟᴀʏʙᴜᴛᴛᴏɴ ɪɴsᴛᴀɢʀᴀᴍ  

ᚗ <code>{0}ɪɢsɪʟᴠᴇʀ</code>  
⊷ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ sɪʟᴠᴇʀ ᴘʟᴀʏʙᴜᴛᴛᴏɴ ɪɴsᴛᴀɢʀᴀᴍ  

ᚗ <code>{0}ғʙɢᴏʟᴅ</code>  
⊷ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ɢᴏʟᴅ ᴘʟᴀʏʙᴜᴛᴛᴏɴ ꜰᴀᴄᴇʙᴏᴏᴋ  

ᚗ <code>{0}ғʙsɪʟᴠᴇʀ</code>  
⊷ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ sɪʟᴠᴇʀ ᴘʟᴀʏʙᴜᴛᴛᴏɴ ꜰᴀᴄᴇʙᴏᴏᴋ  

ᚗ <code>{0}ᴛᴡɢᴏʟᴅ</code>  
⊷ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ɢᴏʟᴅ ᴘʟᴀʏʙᴜᴛᴛᴏɴ ᴛᴡɪᴛᴛᴇʀ  

ᚗ <code>{0}ᴛᴡsɪʟᴠᴇʀ</code>  
⊷ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ sɪʟᴠᴇʀ ᴘʟᴀʏʙᴜᴛᴛᴏɴ ᴛᴡɪᴛᴛᴇʀ  
⊷ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ sɪʟᴠᴇʀ ᴘʟᴀʏʙᴜᴛᴛᴏɴ ʏᴏᴜᴛᴜʙᴇ

"""

def tweet(text):
    url = "https://api.botcahx.eu.org/api/ephoto/twtsilverbutton"
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
    url = "https://api.botcahx.eu.org/api/ephoto/twtgoldbutton"
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
    url = "https://api.botcahx.eu.org/api/ephoto/fbsilverbutton"
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
    url = "https://api.botcahx.eu.org/api/ephoto/fbgoldbutton"
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
        
def robott(text):
    url = "https://api.botcahx.eu.org/api/ephoto/ytsilverbutton"
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
    url = "https://api.botcahx.eu.org/api/ephoto/igsilverbutton"
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
def robotttg(text):
    url = "https://api.botcahx.eu.org/api/ephoto/iggoldbutton"
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
def horor(text):
    url = "https://api.botcahx.eu.org/api/ephoto/ytgoldbutton"
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

# YOYTUBE        
@PY.UBOT("ytgold")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("ᴄᴏɴᴛᴏʜ : .ʏᴛɢᴏʟᴅ ᴍᴏɪʀᴇ")
        return

    request_text = args[1]
    await message.reply_text("sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs, ᴍᴏʜᴏɴ ᴛᴜɴɢɢᴜ ᴄᴇss...")


    image_content = horor(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("ᴀᴘɪᴋᴇʏ sᴇᴅᴀɴɢ ʙᴇʀᴍᴀsᴀʟᴀʜ ᴄᴇss")
                              
@PY.UBOT("ytsilver")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("ᴄᴏɴᴛᴏʜ : .ʏᴛsɪʟᴠᴇʀ ᴍᴏɪʀᴇ")
        return

    request_text = args[1]
    await message.reply_text("ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ, ᴍᴏʜᴏɴ ᴛᴜɴɢɢᴜ ᴄᴇꜱꜱ...")


    image_content = robott(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("ᴀᴘɪᴋᴇʏ ꜱᴇᴅᴀɴɢ ʙᴇʀᴍᴀꜱᴀʟᴀʜ ᴄᴜᴋɪ!")

# INSTAGRAM                                
@PY.UBOT("iggold")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("ᴄᴏɴᴛᴏʜ : .ɪɢɢᴏʟᴅ ᴍᴏɪʀᴇ")
        return

    request_text = args[1]
    await message.reply_text("ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ, ᴍᴏʜᴏɴ ᴛᴜɴɢɢᴜ ᴄᴇꜱꜱ...")


    image_content = robotttg(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("ᴀᴘɪᴋᴇʏ ꜱᴇᴅᴀɴɢ ʙᴇʀᴍᴀꜱᴀʟᴀʜ ᴄᴜᴋɪ!")

@PY.UBOT("igsilver")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("ᴄᴏɴᴛᴏʜ : .ɪɢsɪʟᴠᴇʀ ᴍᴏɪʀᴇ")
        return

    request_text = args[1]
    await message.reply_text("ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ, ᴍᴏʜᴏɴ ᴛᴜɴɢɢᴜ ᴄᴇꜱꜱ...")


    image_content = robottt(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("ᴀᴘɪᴋᴇʏ ꜱᴇᴅᴀɴɢ ʙᴇʀᴍᴀꜱᴀʟᴀʜ ᴄᴜᴋɪ!")

# FACEBOOK                                   
@PY.UBOT("fbsilver")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("ᴄᴏɴᴛᴏʜ : .ғʙsɪʟᴠᴇʀ ᴍᴏɪʀᴇ")
        return

    request_text = args[1]
    await message.reply_text("ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ, ᴍᴏʜᴏɴ ᴛᴜɴɢɢᴜ ᴄᴇꜱꜱ...")


    image_content = fb(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("ᴀᴘɪᴋᴇʏ ꜱᴇᴅᴀɴɢ ʙᴇʀᴍᴀꜱᴀʟᴀʜ ᴄᴜᴋɪ!")

@PY.UBOT("fbgold")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("ᴄᴏɴᴛᴏʜ : .ғʙɢᴏʟᴅ ᴍᴏɪʀᴇ")
        return

    request_text = args[1]
    await message.reply_text("ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ, ᴍᴏʜᴏɴ ᴛᴜɴɢɢᴜ ᴄᴇꜱꜱ...")


    image_content = fbs(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("ᴀᴘɪᴋᴇʏ ꜱᴇᴅᴀɴɢ ʙᴇʀᴍᴀꜱᴀʟᴀʜ ᴄᴜᴋɪ!")

# TWITTER
@PY.UBOT("twtsilver")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("ᴄᴏɴᴛᴏʜ : .ᴛᴡᴛsɪʟᴠᴇʀ ᴍᴏɪʀᴇ")
        return

    request_text = args[1]
    await message.reply_text("ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ, ᴍᴏʜᴏɴ ᴛᴜɴɢɢᴜ ᴄᴇꜱꜱ...")


    image_content = tweet(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("ᴀᴘɪᴋᴇʏ ꜱᴇᴅᴀɴɢ ʙᴇʀᴍᴀꜱᴀʟᴀʜ ᴄᴜᴋɪ!")

@PY.UBOT("twtgold")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("ᴄᴏɴᴛᴏʜ : .ᴛᴡᴛɢᴏʟᴅ ᴍᴏɪʀᴇ")
        return

    request_text = args[1]
    await message.reply_text("ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ, ᴍᴏʜᴏɴ ᴛᴜɴɢɢᴜ ᴄᴇꜱꜱ...")


    image_content = tweets(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("ᴀᴘɪᴋᴇʏ ꜱᴇᴅᴀɴɢ ʙᴇʀᴍᴀꜱᴀʟᴀʜ ᴄᴜᴋɪ!")
