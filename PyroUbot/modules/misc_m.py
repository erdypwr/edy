import asyncio
import os
import requests

from asyncio import sleep
from pyrogram.raw.functions.messages import DeleteHistory, StartBot

from bs4 import BeautifulSoup
from io import BytesIO

from telegraph import Telegraph, exceptions, upload_file

from PyroUbot import *



__MODULE__ = "ᴍɪꜱᴄ"
__HELP__ = """
<blockquote>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍɪꜱᴄ ᴄᴇss

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}limit</code>
    ᴍᴇɴɢᴇᴄᴇᴋ sᴛᴀᴛᴜs ᴀᴋᴜɴ ᴀᴘᴀᴋᴀʜ ᴛᴇʀᴋᴇɴᴀ ʟɪᴍɪᴛ ᴀᴛᴀᴜ ᴛɪᴅᴀᴋ ᴄᴇss

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}carbon</code>
    ᴍᴇᴍʙᴜᴀᴛ ᴛᴇxᴛ ᴄᴀʀʙᴏɴᴀʀᴀ ᴄᴇss

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}qrGen</code>
    ᴍᴇʀᴜʙᴀʜ Qʀᴄᴏᴅᴇ ᴛᴇxᴛ ᴍᴇɴᴊᴀᴅɪ ɢᴀᴍʙᴀʀ ᴄᴇss

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}qrRead</code>
    ᴍᴇʀᴜʙᴀʜ Qʀᴄᴏᴅᴇ ᴍᴇᴅɪᴀ ᴍᴇɴᴊᴀᴅɪ ᴛᴇxᴛ ᴄᴇss

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}font</code>
    ᴍᴇʀᴜʙᴀʜ ᴛᴇxᴛ ᴍᴇɴᴊᴀᴅɪ ʙᴇʀʙᴇᴅᴀ ᴄᴇss</blockquote>
"""

@PY.UBOT("limit")
@PY.TOP_CMD
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    pong = await EMO.PING(client)
    tion = await EMO.MENTION(client)
    yubot = await EMO.UBOT(client)
    await client.unblock_user("SpamBot")
    bot_info = await client.resolve_peer("SpamBot")
    msg = await message.reply(f"{prs}ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ . . .")
    response = await client.invoke(
        StartBot(
            bot=bot_info,
            peer=bot_info,
            random_id=client.rnd_id(),
            start_param="start",
        )
    )
    await sleep(1)
    await msg.delete()
    status = await client.get_messages("SpamBot", response.updates[1].message.id + 1) 
    if status and hasattr(status, "text"):
        pjg = len(status.text)
        print(pjg)
        if pjg <= 100:
            if client.me.is_premium:
                text = f"""
<blockquote><b>{pong} sᴛᴀᴛᴜs ᴀᴋᴜɴ ᴘʀᴇᴍɪᴜᴍ : ᴛʀᴜᴇ</b>
<b>{tion} ʟɪᴍɪᴛ ᴄʜᴇᴄᴋ : ᴀᴋᴜɴ ᴇʟᴜ ᴛɪᴅᴀᴋ ᴅɪʙᴀᴛᴀsɪ ᴄᴇꜱꜱ</b>
<b>{yubot} ᴜʙᴏᴛ : {bot.me.mention}</b></blockquote>

<blockquote><b></b></blockquote>
"""
            else:
                text = f"""
<blockquote><b>sᴛᴀᴛᴜs ᴀᴋᴜɴ  : ʙᴇʟɪ ᴘʀᴇᴍ ᴅᴜʟᴜ ᴄᴜᴋɪ</b>
<b>ʟɪᴍɪᴛ ᴄʜᴇᴄᴋ : ᴀᴋᴜɴ ᴇʟᴜ ᴛɪᴅᴀᴋ ᴅɪʙᴀᴛᴀsɪ ᴄᴇꜱꜱ</b>
<b>ᴜʙᴏᴛ : {bot.me.mention}</b></blockquote>

<blockquote><b></b></blockquote>
"""
            await client.send_message(message.chat.id, text)
            return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
        else:
            if client.me.is_premium:
                text = f"""
<blockquote><b>{pong} sᴛᴀᴛᴜs ᴀᴋᴜɴ ᴘʀᴇᴍɪᴜᴍ : ᴛʀᴜᴇ</b>
<b>{tion} ʟɪᴍɪᴛ ᴄʜᴇᴄᴋ : ᴀᴋᴜɴ ᴇʟᴜ ʙᴇʀᴍᴀsᴀʟᴀʜ ᴄᴇꜱꜱ</b>
<b>{yubot} ᴜʙᴏᴛ : {bot.me.mention}</b></blockquote>

<blockquote><b></b></blockquote>
"""
            else:
                text = f"""
<blockquote><b>sᴛᴀᴛᴜs ᴀᴋᴜɴ  : ʙᴇʟɪ ᴘʀᴇᴍ ᴅᴜʟᴜ ᴄᴜᴋɪ</b>
<b>ʟɪᴍɪᴛ ᴄʜᴇᴄᴋ : ᴀᴋᴜɴ ᴇʟᴜ ʙᴇʀᴍᴀsᴀʟᴀʜ ᴄᴇꜱꜱ</b>
<b>ᴜʙᴏᴛ : {bot.me.mention}</b></blockquote>

<blockquote><b></b></blockquote>
"""
            await client.send_message(message.chat.id, text)
            return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
    else:
        print("Status Tidak Valid Atau Status.Text Tidak Ada Cess")

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@PY.UBOT("carbon")
@PY.TOP_CMD
async def carbon_func(client, message):
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await message.delete()
    ex = await message.reply("ᴘʀᴏꜱᴇꜱꜱ ᴄᴇss...")
    carbon = await make_carbon(text)
    await ex.edit("ᴜᴘʟᴏᴀᴅɪɴɢ ᴄᴇss...")
    await asyncio.gather(
        ex.delete(),
        client.send_photo(
            message.chat.id,
            carbon,
            caption=f"Carboniꜱed By :{client.me.mention}",
        ),
    )
    carbon.close()


def qr_gen(content):
    return {
        "data": content,
        "config": {
            "body": "circle-zebra",
            "eye": "frame13",
            "eyeBall": "ball14",
            "erf1": [],
            "erf2": [],
            "erf3": [],
            "brf1": [],
            "brf2": [],
            "brf3": [],
            "bodyColor": "#000000",
            "bgColor": "#FFFFFF",
            "eye1Color": "#000000",
            "eye2Color": "#000000",
            "eye3Color": "#000000",
            "eyeBall1Color": "#000000",
            "eyeBall2Color": "#000000",
            "eyeBall3Color": "#000000",
            "gradientColor1": "",
            "gradientColor2": "",
            "gradientType": "linear",
            "gradientOnEyes": "true",
            "logo": "",
            "logoMode": "default",
        },
        "size": 1000,
        "download": "imageUrl",
        "file": "png",
    }


@PY.UBOT("qrgen")
@PY.TOP_CMD
async def _(client, message):
    ID = message.reply_to_message or message
    if message.reply_to_message:
        data = qr_gen(message.reply_to_message.text)
    else:
        if len(message.command) < 2:
            return await message.delete()
        else:
            data = qr_gen(message.text.split(None, 1)[1])
    Tm = await message.reply("sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ʙᴜᴀᴛ Qʀᴄᴏᴅᴇ....")
    try:
        QRcode = (
            requests.post(
                "https://api.qrcode-monkey.com//qr/custom",
                json=data,
            )
            .json()["imageUrl"]
            .replace("//api", "https://api")
        )
        await client.send_photo(message.chat.id, QRcode, reply_to_message_id=ID.id)
        await Tm.delete()
    except Exception as error:
        await Tm.edit(error)



@PY.UBOT("qrread")
@PY.TOP_CMD
async def _(client, message):
    replied = message.reply_to_message
    if not (replied and replied.media and (replied.photo or replied.sticker)):
        await message.reply("ʙᴀʟᴀs ᴋᴏᴅᴇ Qʀ ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴅᴀᴛᴀ ᴄᴇss...")
        return
    if not os.path.isdir("premiumQR/"):
        os.makedirs("premiumQR/")
    AM = await message.reply("ᴍᴇɴɢᴜɴᴅᴜʜ ᴍᴇᴅɪᴀ ᴄᴇss...")
    down_load = await client.download_media(message=replied, file_name="premiumQR/")
    await AM.edit("ᴍᴇᴍᴘʀᴏsᴇs ᴋᴏᴅᴇ Qʀ ᴇʟᴜ...")
    cmd = [
        "curl",
        "-X",
        "POST",
        "-F",
        "f=@" + down_load + "",
        "https://zxing.org/w/decode",
    ]
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    out_response = stdout.decode().strip()
    err_response = stderr.decode().strip()
    os.remove(down_load)
    if not (out_response or err_response):
        await AM.edit("ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴅᴀᴛᴀ ᴋᴏᴅᴇ Qʀ ɪɴɪ ᴄᴇss...")
        return
    try:
        soup = BeautifulSoup(out_response, "html.parser")
        qr_contents = soup.find_all("pre")[0].text
    except IndexError:
        await AM.edit("ɪɴᴅᴇᴋs ᴅᴀꜰᴛᴀʀ ᴅɪ ʟᴜᴀʀ ᴊᴀɴɢᴋᴀᴜᴀɴ ᴄᴇss")
        return
    await AM.edit(f"ᴅᴀᴛᴀ Qʀᴄᴏᴅᴇ:\n{qr_contents}")
  

@PY.UBOT("font")
@PY.TOP_CMD
async def _(client, message):
    if message.reply_to_message:
        if message.reply_to_message.text:
            query = id(message)
        else:
            return await message.reply("ʜᴀʀᴀᴘ ʀᴇᴘʟʏ ᴋᴇ ᴛᴇxᴛ ᴄᴇss")
    else:
        if len(message.command) < 2:
            return await message.reply(f"{message.text} [ʀᴇᴘʟʏ/ᴛᴇxᴛ]")
        else:
            query = id(message)
    try:
        x = await client.get_inline_bot_results(bot.me.username, f"get_font {query}")
        return await message.reply_inline_bot_result(x.query_id, x.results[0].id)
    except Exception as error:
        return await message.reply(error)


@PY.INLINE("^get_font")
async def _(client, inline_query):
    get_id = int(inline_query.query.split(None, 1)[1])
    buttons = InlineKeyboard(row_width=3)
    keyboard = []
    for X in query_fonts[0]:
        keyboard.append(
            InlineKeyboardButton(X, callback_data=f"get {get_id} {query_fonts[0][X]}")
        )
    buttons.add(*keyboard)
    buttons.row(InlineKeyboardButton("►", callback_data=f"next {get_id}"))
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get font!",
                    reply_markup=buttons,
                    input_message_content=InputTextMessageContent(
                        "sɪʟᴀʜᴋᴀɴ ᴘɪʟɪʜ sᴀʟᴀʜ sᴀᴛᴜ ꜰᴏɴᴛ ᴅɪʙᴀᴡᴀʜ ᴄᴇss"
                    ),
                )
            )
        ],
    )


@PY.CALLBACK("^get")
async def _(client, callback_query):
    try:
        q = int(callback_query.data.split()[1])
        m = [obj for obj in get_objects() if id(obj) == q][0]
        new = str(callback_query.data.split()[2])
        if m.reply_to_message:
            text = m.reply_to_message.text
        else:
            text = m.text.split(None, 1)[1]
        get_new_font = gens_font(new, text)
        return await callback_query.edit_message_text(get_new_font)
    except Exception as error:
        return await callback_query.answer(f"ᴇʀʀᴏʀ: {error}", True)


@PY.CALLBACK("^next")
async def _(client, callback_query):
    try:
        get_id = int(callback_query.data.split()[1])
        buttons = InlineKeyboard(row_width=3)
        keyboard = []
        for X in query_fonts[1]:
            keyboard.append(
                InlineKeyboardButton(
                    X, callback_data=f"get {get_id} {query_fonts[1][X]}"
                )
            )
        buttons.add(*keyboard)
        buttons.row(InlineKeyboardButton("◄", callback_data=f"prev {get_id}"))
        return await callback_query.edit_message_reply_markup(reply_markup=buttons)
    except Exception as error:
        return await callback_query.answer(f"ᴇʀʀᴏʀ ᴄᴇss: {error}", True)


@PY.CALLBACK("^prev")
async def _(client, callback_query):
    try:
        get_id = int(callback_query.data.split()[1])
        buttons = InlineKeyboard(row_width=3)
        keyboard = []
        for X in query_fonts[0]:
            keyboard.append(
                InlineKeyboardButton(
                    X, callback_data=f"get {get_id} {query_fonts[0][X]}"
                )
            )
        buttons.add(*keyboard)
        buttons.row(InlineKeyboardButton("►", callback_data=f"next {get_id}"))
        return await callback_query.edit_message_reply_markup(reply_markup=buttons)
    except Exception as error:
        return await callback_query.answer(f"❌ ᴇʀʀᴏʀ ᴄᴇss: {error}", True)
