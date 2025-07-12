import os
from PIL import Image, ImageOps, ImageFilter
from PyroUbot import *

__MODULE__ = "ᴛʀᴀɴꜱꜰᴏʀᴍ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴛʀᴀɴꜱꜰᴏʀᴍ 』</b>

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}mirror</code> [ʙᴀʟᴀꜱ ɢᴀᴍʙᴀʀ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴɢᴄᴇʀᴍɪɴᴋᴀɴ ɢᴀᴍʙᴀʀ

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}flip</code> [ʙᴀʟᴀꜱ ɢᴀᴍʙᴀʀ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇᴍʙᴀʟɪᴋ ɢᴀᴍʙᴀʀ ᴠᴇʀᴛɪᴋᴀʟ

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ghost</code> [ʙᴀʟᴀꜱ ɢᴀᴍʙᴀʀ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴɢɪɴᴠᴇʀᴛ ɢᴀᴍʙᴀʀ

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}bw</code> [ʙᴀʟᴀꜱ ɢᴀᴍʙᴀʀ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴɢᴜʙᴀʜ ɢᴀᴍʙᴀʀ ᴋᴇ ʙʟᴀᴄᴋ ᴀɴᴅ ᴡʜɪᴛᴇ

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}poster</code> [ʙᴀʟᴀꜱ ɢᴀᴍʙᴀʀ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴɢᴜʙᴀʜ ɢᴀᴍʙᴀʀ ᴋᴇ ᴇꜰᴇᴋ ᴘᴏꜱᴛᴇʀ

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}rotate</code> [ᴅᴇʀᴀᴊᴀᴛ] [ʙᴀʟᴀꜱ ɢᴀᴍʙᴀʀ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇᴍᴜᴛᴀʀ ɢᴀᴍʙᴀʀ ᴅᴇɴɢᴀɴ ᴅᴇʀᴀᴊᴀᴛ ᴛᴇʀᴛᴇɴᴛᴜ

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}resize</code> [ʟᴇʙᴀʀ] [ᴛɪɴɢɢɪ] [ʙᴀʟᴀꜱ ɢᴀᴍʙᴀʀ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴɢᴜʙᴀʜ ᴜᴋᴜʀᴀɴ ɢᴀᴍʙᴀʀ

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}crop</code> [x1] [y1] [x2] [y2] [ʙᴀʟᴀꜱ ɢᴀᴍʙᴀʀ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇᴍᴏᴛᴏɴɢ ɢᴀᴍʙᴀʀ

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}blur</code> [ʀᴀᴅɪᴜꜱ] [ʙᴀʟᴀꜱ ɢᴀᴍʙᴀʀ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴɢʙʟᴜʀ ɢᴀᴍʙᴀʀ

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}hd2</code> [ʙᴀʟᴀꜱ ɢᴀᴍʙᴀʀ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴɪɴɢᴋᴀᴛᴋᴀɴ ʀᴇꜱᴏʟᴜꜱɪ ɢᴀᴍʙᴀʀ ᴍᴇɴᴊᴀᴅɪ ꜱᴀɴɢᴀᴛ ʜᴅ (ᴜᴘꜱᴄᴀʟᴇ 2x)
</blockquote>
"""

def download_image_from_reply(m):
    if not m.reply_to_message or not m.reply_to_message.media:
        return None
    return m.reply_to_message.download()

@PY.UBOT(["mirror", "flip", "ghost", "bw", "poster"])
async def _(c, m):
    cmd = m.command[0]
    file = await download_image_from_reply(m)
    if not file:
        return await m.reply("<b>ʙᴀʟᴀꜱ ᴋᴇ ɢᴀᴍʙᴀʀ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪᴛʀᴀɴꜱꜰᴏʀᴍ!</b>")
    await m.reply("<b>ᴍᴇɴɢᴏʟᴀʜ ɢᴀᴍʙᴀʀ...</b>")
    im = Image.open(file).convert("RGB")
    if cmd == "mirror":
        IMG = ImageOps.mirror(im)
    elif cmd == "flip":
        IMG = ImageOps.flip(im)
    elif cmd == "ghost":
        IMG = ImageOps.invert(im)
    elif cmd == "bw":
        IMG = ImageOps.grayscale(im)
    elif cmd == "poster":
        IMG = ImageOps.posterize(im, 2)
    else:
        IMG = im
    out_file = "transformed.png"
    IMG.save(out_file, quality=95)
    await c.send_document(m.chat.id, out_file, reply_to_message_id=m.reply_to_message.message_id if m.reply_to_message else None)
    os.remove(file)
    os.remove(out_file)

@PY.UBOT(["resize"])
async def _(c, m):
    args = m.text.split()
    if len(args) < 3 or not args[1].isdigit() or not args[2].isdigit():
        return await m.reply("<b>ᴘᴇɴɢɢᴜɴᴀᴀɴ: .resize [ʟᴇʙᴀʀ] [ᴛɪɴɢɢɪ] (ʙᴀʟᴀꜱ ɢᴀᴍʙᴀʀ)</b>")
    width, height = int(args[1]), int(args[2])
    file = await download_image_from_reply(m)
    if not file:
        return await m.reply("<b>ʙᴀʟᴀꜱ ᴋᴇ ɢᴀᴍʙᴀʀ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪʀᴇꜱɪᴢᴇ!</b>")
    await m.reply("<b>ᴍᴇɴɢᴜʙᴀʜ ᴜᴋᴜʀᴀɴ ɢᴀᴍʙᴀʀ...</b>")
    im = Image.open(file).convert("RGB")
    IMG = im.resize((width, height))
    out_file = "resized.png"
    IMG.save(out_file, quality=95)
    await c.send_document(m.chat.id, out_file, reply_to_message_id=m.reply_to_message.message_id if m.reply_to_message else None)
    os.remove(file)
    os.remove(out_file)

@PY.UBOT(["crop"])
async def _(c, m):
    args = m.text.split()
    if len(args) < 5 or not all(a.isdigit() for a in args[1:5]):
        return await m.reply("<b>ᴘᴇɴɢɢᴜɴᴀᴀɴ: .crop [x1] [y1] [x2] [y2] (ʙᴀʟᴀꜱ ɢᴀᴍʙᴀʀ)</b>")
    x1, y1, x2, y2 = map(int, args[1:5])
    file = await download_image_from_reply(m)
    if not file:
        return await m.reply("<b>ʙᴀʟᴀꜱ ᴋᴇ ɢᴀᴍʙᴀʀ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪᴄʀᴏᴘ!</b>")
    await m.reply("<b>ᴍᴇᴍᴏᴛᴏɴɢ ɢᴀᴍʙᴀʀ...</b>")
    im = Image.open(file).convert("RGB")
    IMG = im.crop((x1, y1, x2, y2))
    out_file = "cropped.png"
    IMG.save(out_file, quality=95)
    await c.send_document(m.chat.id, out_file, reply_to_message_id=m.reply_to_message.message_id if m.reply_to_message else None)
    os.remove(file)
    os.remove(out_file)

@PY.UBOT(["blur"])
async def _(c, m):
    args = m.text.split()
    radius = int(args[1]) if len(args) > 1 and args[1].isdigit() else 5
    file = await download_image_from_reply(m)
    if not file:
        return await m.reply("<b>ʙᴀʟᴀꜱ ᴋᴇ ɢᴀᴍʙᴀʀ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪʙʟᴜʀ!</b>")
    await m.reply(f"<b>ᴍᴇɴɢʙʟᴜʀ ɢᴀᴍʙᴀʀ (radius={radius})...</b>")
    im = Image.open(file).convert("RGB")
    IMG = im.filter(ImageFilter.GaussianBlur(radius=radius))
    out_file = "blurred.png"
    IMG.save(out_file, quality=95)
    await c.send_document(m.chat.id, out_file, reply_to_message_id=m.reply_to_message.message_id if m.reply_to_message else None)
    os.remove(file)
    os.remove(out_file)

@PY.UBOT(["rotate"])
async def _(c, m):
    args = m.text.split()
    value = 90
    if len(args) > 1 and args[1].isdigit():
        value = int(args[1])
        if value > 360:
            value = 90
    file = await download_image_from_reply(m)
    if not file:
        return await m.reply("<b>ʙᴀʟᴀꜱ ᴋᴇ ɢᴀᴍʙᴀʀ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪʀᴏᴛᴀꜱɪ!</b>")
    await m.reply("<b>ᴍᴇᴍᴜᴛᴀʀ ɢᴀᴍʙᴀʀ...</b>")
    im = Image.open(file).convert("RGB")
    IMG = im.rotate(value, expand=1)
    out_file = "rotated.png"
    IMG.save(out_file, quality=95)
    await c.send_document(m.chat.id, out_file, reply_to_message_id=m.reply_to_message.message_id if m.reply_to_message else None)
    os.remove(file)
    os.remove(out_file)

@PY.UBOT(["hd2"])
async def _(c, m):
    file = await download_image_from_reply(m)
    if not file:
        return await m.reply("<b>ʙᴀʟᴀꜱ ᴋᴇ ɢᴀᴍʙᴀʀ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪʜᴅᴋᴀɴ ᴄᴜᴋɪ!</b>")
    await m.reply("<b>ᴍᴇɴɪɴɢᴋᴀᴛᴋᴀɴ ʀᴇꜱᴏʟᴜꜱɪ ɢᴀᴍʙᴀʀ ᴄᴇꜱꜱ...</b>")
    im = Image.open(file).convert("RGB")
    width, height = im.size
    IMG = im.resize((width*2, height*2), resample=Image.LANCZOS)
    out_file = "hd2.png"
    IMG.save(out_file, quality=95)
    await c.send_document(m.chat.id, out_file, reply_to_message_id=m.reply_to_message.message_id if m.reply_to_message else None)
    os.remove(file)
    os.remove(out_file)
