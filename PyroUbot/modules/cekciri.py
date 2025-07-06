import asyncio
import random

from PyroUbot import *

@PY.UBOT("cekkontol|cekkntl")
@PY.TOP_CMD
async def cekkhodam(client, message):
    try:
        nama = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
        if not nama:
            await message.edit("<blockquote><b>ɴᴀᴍᴀɴʏᴀ ᴍᴀɴᴀ ᴄᴜᴋɪ<emoji id=6325790754543241229>🪨</emoji></b></blockquote>")
            return

        def pick_random(options):
            return random.choice(options)

        hasil = f"""
<b>𖤐 ᴄᴇᴋ ᴋᴏɴᴛᴏʟ {nama} </b>
<blockquote><b>╭───「 ʜᴀꜱɪʟ ᴄᴇᴋ ᴋᴏɴᴛᴏʟ 」───</b>
<b>┆• ᴡᴀʀɴᴀ ᴋᴏɴᴛᴏʟ : {pick_random(['ɪʀᴇɴᴋ', 'ᴘɪɴᴋ', 'ʀᴀɪɴʙᴏᴡ', 'ɪᴛᴀᴍ ᴄᴏᴋ', 'ᴋᴜɴɪɴɢ'])}</b>
<b>┆• ᴡᴀʀɴᴀ ᴊᴇᴍʙᴜᴛ : {pick_random(['ɪʀᴇɴᴋ', 'ᴘɪɴᴋ', 'ʀᴀɪɴʙᴏᴡ', 'ɪᴛᴀᴍ ᴄᴏᴋ', 'ᴋᴜɴɪɴɢ'])}</b>
<b>┆• ᴜᴋᴜʀᴀɴ ᴋᴏɴᴛᴏʟ : {pick_random(['16 ᴄᴍ', '10 ᴄᴍ', '15 ᴄᴍ', '6 ᴄᴍ', '1 ᴄᴍ', '3 ᴄᴍ'])}</b>
<b>┆• ᴄɪʀɪ ᴄɪʀɪɴʏᴀ : {pick_random(['ʙᴇɴɢᴋᴏᴋ', 'ʙᴇɴɢᴋᴏᴋ ᴅɪᴋɪᴛ', 'ʟᴜʀᴜꜱ', 'ᴘᴀɴᴊᴀɴɢ ᴋᴇᴄɪʟ', 'ʟᴇʙᴀʀ', 'ᴛᴜᴍᴘᴜʟ'])}</b>
<b>╰──────────────────────</b></blockquote>   
      """
        await message.edit(hasil)
    except BaseException:
        pass

@PY.UBOT("cekmemek|cekmmk")
@PY.TOP_CMD
async def cekkhodam(client, message):
    try:
        nama = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
        if not nama:
            await message.edit("<blockquote><b>ɴᴀᴍᴀɴʏᴀ ᴍᴀɴᴀ ᴄᴜᴋɪ<emoji id=6325790754543241229>🪨</emoji></b></blockquote>")
            return

        def pick_random(options):
            return random.choice(options)

        hasil = f"""
<b>𖤐 ᴄᴇᴋ ᴍᴇᴍᴇᴋ {nama} </b>
<blockquote><b>╭───「 ʜᴀꜱɪʟ ᴄᴇᴋ ᴍᴇᴍᴇᴋ 」───</b>
<b>┆• ᴡᴀʀɴᴀ ᴍᴇᴍᴇᴋ : {pick_random(['ɪʀᴇɴᴋ', 'ᴘɪɴᴋ', 'ʀᴀɪɴʙᴏᴡ', 'ɪᴛᴀᴍ ᴄᴏᴋ', 'ᴋᴜɴɪɴɢ'])}</b>
<b>┆• ᴡᴀʀɴᴀ ᴊᴇᴍʙᴜᴛ : {pick_random(['ɪʀᴇɴᴋ', 'ᴘɪɴᴋ', 'ʀᴀɪɴʙᴏᴡ', 'ɪᴛᴀᴍ ᴄᴏᴋ', 'ᴋᴜɴɪɴɢ'])}</b>
<b>┆• ᴜᴋᴜʀᴀɴ ʟᴏʙᴀɴɢ : {pick_random(['16 ɪɴᴄ', '10 ɪɴᴄ', '15 ɪɴᴄ', '6 ɪɴᴄ', '1 ɪɴᴄ', '3 ɪɴᴄ'])}</b>
<b>┆• ᴄɪʀɪ ᴄɪʀɪɴʏᴀ : {pick_random(['ʙᴇʀᴊᴇᴍʙᴜᴛ', 'ᴅᴀʜ ᴊᴇʙᴏʟ', 'ʙᴀᴜ ᴛʀᴀꜱɪ', 'ʙᴇʀʟᴇɴᴅɪʀ', 'ʟᴇʙᴀʀ ɪᴛᴀᴍ', 'ꜱᴇᴍᴘɪᴛ'])}</b>
<b>╰──────────────────────</b></blockquote>   
      """
        await message.edit(hasil)
    except BaseException:
        pass

@PY.UBOT("ceksange|ceksagne")
@PY.TOP_CMD
async def cekkhodam(client, message):
    try:
        nama = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
        if not nama:
            await message.edit("<blockquote><b>ɴᴀᴍᴀɴʏᴀ ᴍᴀɴᴀ ᴄᴜᴋɪ<emoji id=6325790754543241229>🪨</emoji></b></blockquote>")
            return

        def pick_random(options):
            return random.choice(options)

        hasil = f"""
<b>𖤐 ᴄᴇᴋ ꜱᴀɴɢᴇ</b>
<blockquote><b>╭───「 ʜᴀꜱɪʟ ᴄᴇᴋ ꜱᴀɴɢᴇ 」───</b>
<b>┆• ɴᴀᴍᴀ :  {nama} </b>
<b>┆• ꜱᴀɴɢᴇ : {pick_random(['90%', '95%', '75%', '85%', '100%'])}</b>
<b>┆• ꜱᴀɴɢᴇᴀɴ ᴋᴏɴᴛᴏʟ </b>
<b>╰──────��───────────────</b></blockquote>   
      """
        await message.edit(hasil)
    except BaseException:
        pass
__MODULE__ = "ᴄᴇᴋ ᴄɪʀɪ"
__HELP__ = """<blockquote><b>「 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍᴏᴅᴜʟᴇ ᴄᴇᴋ ᴄɪʀɪ 」</b>

<b>♛ ᴘᴇʀɪɴᴛᴀʜ: .ᴄᴇᴋᴋᴏɴᴛᴏʟ</b>
<b>卍 ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴄᴇᴋ ᴋᴏɴᴛᴏʟ ᴅᴇɴɢᴀɴ ɴᴀᴍᴀ ᴏʀᴀɴɢɴʏᴀ</b>

<b>♛ ᴘᴇʀɪɴᴛᴀʜ: .ᴄᴇᴋᴍᴇᴍᴇᴋ</b>
<b>卍 ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴄᴇᴋ ᴍᴇᴍᴇᴋ ᴅᴇɴɢᴀɴ ɴᴀᴍᴀ ᴏʀᴀɴɢɴʏᴀ</b>

<b>♛ ᴘᴇʀɪɴᴛᴀʜ: .ᴄᴇᴋꜱᴀɴɢᴇ</b>
<b>卍 ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴄᴇᴋ ꜱᴀɴɢᴇ ᴅᴇɴɢᴀɴ ɴᴀᴍᴀ ᴏʀᴀɴɢɴʏᴀ</b></blockquote>
  """
