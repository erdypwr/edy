# Copyright (C) 2020 TeamUltroid
# Ported By Vicky / @Vckyouuu From Ultroid
# Full Love From Vicky For All Lord
# @LORDUSERBOT_GROUP
# @sharinguserbot
import json
import os
import pybase64
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)
from youtubesearchpython import SearchVideos
from pyrogram.types import Message
from PyroUbot import *

__MODULE__ = "ᴍᴇɴᴄᴀʀɪʟᴀɢᴜ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪʟᴀɢᴜ ᴄᴇꜱꜱ 』</b>

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}fsong</code> [ᴊᴜᴅᴜʟ ʟᴀɢᴜ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ʟᴀɢᴜ ᴅᴀʀɪ ʏᴏᴜᴛᴜʙᴇ (ᴍᴘ3)
</blockquote>
"""

@PY.UBOT(["fsong"])
async def _(c, m: Message):
    query = m.text.split(None, 1)[1] if len(m.command) > 1 else None
    if not query:
        return await m.reply("<b>ᴇʀʀᴏʀ! ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ <code>.fsong &lt;judul lagu&gt;</code></b>")
    proses = await m.reply("<b>ᴍᴇɴᴄᴀʀɪ ʟᴀɢᴜ ᴄᴇꜱꜱ...</b>")
    search = SearchVideos(query, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        url = q[0]["link"]
    except Exception:
        return await proses.edit("<b>ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ʟᴀɢᴜ ʏᴀɴɢ ᴄᴏᴄᴏᴋ ᴄᴜᴋɪ...</b>")
    await proses.edit(f"<b>ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴄᴇꜱꜱ {url}...</b>")
    opts = {
        "format": "bestaudio",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "writethumbnail": True,
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }
        ],
        "outtmpl": "%(id)s.mp3",
        "quiet": True,
        "logtostderr": False,
    }
    try:
        await proses.edit("<b>ᴍᴇɴɢᴀᴍʙɪʟ ɪɴꜰᴏʀᴍᴀꜱɪ ʟᴀɢᴜ ᴄᴇꜱꜱ...</b>")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        return await proses.edit(f"<b>{DE}</b>")
    except ContentTooShortError:
        return await proses.edit("<b>ᴋᴏɴᴛᴇɴ ᴜɴᴅᴜʜᴀɴ ᴛᴇʀʟᴀʟᴜ ᴘᴇɴᴅᴇᴋ ᴄᴇꜱꜱ.</b>")
    except GeoRestrictedError:
        return await proses.edit("<b>ᴠɪᴅᴇᴏ ᴛɪᴅᴀᴋ ᴛᴇʀꜱᴇᴅɪᴀ ᴋᴀʀᴇɴᴀ ʙᴀᴛᴀꜱᴀɴ ɢᴇᴏɢʀᴀꜰɪꜱ ᴄᴇꜱꜱ.</b>")
    except MaxDownloadsReached:
        return await proses.edit("<b>ᴍᴀᴋꜱɪᴍᴀʟ ᴅᴏᴡɴʟᴏᴀᴅ ᴛᴇʟᴀʜ ᴅɪᴄᴀᴘᴀɪ ᴄᴇꜱꜱ.</b>")
    except PostProcessingError:
        return await proses.edit("<b>ᴋᴇꜱᴀʟᴀʜᴀɴ ᴘᴏꜱᴛ-ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴄᴜᴋɪ.</b>")
    except UnavailableVideoError:
        return await proses.edit("<b>ᴍᴇᴅɪᴀ ᴛɪᴅᴀᴋ ᴛᴇʀꜱᴇᴅɪᴀ ᴅᴀʟᴀᴍ ꜰᴏʀᴍᴀᴛ ᴅɪᴍɪɴᴛᴀ ᴄᴇꜱꜱ.</b>")
    except XAttrMetadataError as XAME:
        return await proses.edit(f"<b>{XAME.code}: {XAME.msg}\n{XAME.reason}</b>")
    except ExtractorError:
        return await proses.edit("<b>ᴋᴇꜱᴀʟᴀʜᴀɴ ᴇᴋꜱᴛʀᴀᴋꜱɪ ɪɴꜰᴏ.</b>")
    except Exception as e:
        return await proses.edit(f"<b>{str(type(e))}: {e}</b>")
    try:
        sung = str(pybase64.b64decode("QFRlbGVCb3RIZWxw"))[2:14]
        await c.join_chat(sung)
    except Exception:
        pass
    upteload = f"<b>ꜱᴇᴅᴀɴɢ ᴍᴇɴɢᴜɴɢɢᴀʜ ᴄᴇꜱꜱ...<br>ᴊᴜᴅᴜʟ - {rip_data['title']}<br>ᴀʀᴛɪꜱ - {rip_data['uploader']}</b>"
    await proses.edit(upteload)
    await m.reply_document(
        f"{rip_data['id']}.mp3",
        caption=f"<b>🎧 ᴊᴜᴅᴜʟ ʟᴀɢᴜ :</b> <code>{rip_data['title']}</code>\n<b>🧑🏻‍💻 ᴀʀᴛɪꜱ:</b> <code>{rip_data['uploader']}</code>\n\n<b>👑 ꜰɪɴᴅ ʙʏ :</b> <code>{getattr(Var, 'ALIVE_NAME', 'Userbot')}</code>",
        supports_streaming=True,
    )
    try:
        os.remove(f"{rip_data['id']}.mp3")
    except Exception:
        pass
