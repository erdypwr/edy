from pyrogram import Client, filters
from PyroUbot import PY

__MODULE__ = "ᴀᴜᴛᴏʀᴇᴘᴏʀᴛ"
__HELP__ = """
<blockquote><b>📌 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜰɪᴛᴜʀ ᴀᴜᴛᴏ ʀᴇᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ, ᴛᴇʟᴇɢʀᴀᴍ, ᴅᴀɴ ɢʀᴜᴘ ᴘʀɪᴠᴀᴛ</b>

- ᴋɪʀɪᴍ ʟᴀᴘᴏʀᴀɴ ᴏᴛᴏᴍᴀᴛɪꜱ ᴋᴇ **ᴄʜᴀɴɴᴇʟ, ɢʀᴜᴘ ᴘʀɪᴠᴀᴛ, ᴅᴀɴ @ɴᴏᴛᴏꜱᴄᴀᴍ ᴛᴇʟᴇɢʀᴀᴍ**.
- ᴄᴏɴᴛᴏʜ: <code>.ᴀᴜᴛᴏʀᴇᴘᴏʀᴛ ᴛᴀʀɢᴇᴛ_ᴜꜱᴇʀɴᴀᴍᴇ ᴀᴛᴀᴜ https://t.me/channel_link</code>

<b>📌 ᴘᴇʀɪɴᴛᴀʜ:</b>
- <code>{0}ʀᴇᴘᴏʀᴛ ᴛᴀʀɢᴇᴛ_ᴜꜱᴇʀɴᴀᴍᴇ</code> → ʀᴇᴘᴏʀᴛ ᴜꜱᴇʀ/ᴀᴋᴜɴ.
- <code>{0}ʀᴇᴘᴏʀᴛ https://t.me/channel_link</code> → ʀᴇᴘᴏ��ᴛ ᴄʜᴀɴɴᴇʟ ᴀᴛᴀᴜ ɢʀᴜᴘ</b></blockquote>.
"""

@PY.UBOT("report")
@PY.TOP_CMD
async def _(client, message):
    msg = await message.reply("🔍 ᴍᴇᴍᴘʀᴏꜱᴇꜱ ʟᴀᴘᴏʀᴀɴ ᴏᴛᴏᴍᴀᴛɪꜱ ᴄᴇꜱꜱ...")
    
    try:
        args = message.text.split(" ", 1)
        if len(args) < 2:
            return await msg.edit("❌ ᴍᴀꜱᴜᴋᴋᴀɴ ᴜꜱᴇʀɴᴀᴍᴇ ᴀᴛᴀᴜ ʟɪɴᴋ ᴄʜᴀɴɴᴇʟ/ɢʀᴜᴘ!\nᴄᴏɴᴛᴏʜ: <code>.ʀᴇᴘᴏʀᴛ ᴛᴀʀɢᴇᴛ_ᴜꜱᴇʀɴᴀᴍᴇ</code>")

        target = args[1]

        # 🔹 Kirim laporan ke Grup Privat
        private_group = "https://t.me/+PrivateGroupLink"  # Ganti dengan link grup privat
        report_text = f"""
🚨 <b>⚠️ ʟᴀᴘᴏʀᴀɴ ᴏᴛᴏᴍᴀᴛɪꜱ ⚠️</b> 🚨
🔹 ᴛᴀʀɢᴇᴛ: {target}
🔹 ᴀʟᴀꜱᴀɴ: ꜱᴘᴀᴍ, ᴘᴇɴɪᴘᴜᴀɴ, ᴀᴛᴀᴜ ᴋᴏɴᴛᴇɴ ʙᴇʀʙᴀʜᴀʏᴀ
🔹 ᴅɪʟᴀᴘᴏʀᴋᴀɴ ᴏʟᴇʜ: {message.from_user.mention}

⚠️ ꜱɪʟᴀᴋᴀɴ ᴄᴇᴋ ᴅᴀɴ ᴛɪɴᴅᴀᴋ ʟᴀɴᴊᴜᴛ ᴊɪᴋᴀ ᴅɪᴘᴇʀʟᴜᴋᴀɴ.
        """
        await client.send_message(private_group, report_text)

        # 🔹 Kirim laporan ke Channel (jika ada)
        report_channel = "@YourReportChannel"  # Ganti dengan channel report
        await client.send_message(report_channel, report_text)

        # 🔹 Kirim laporan ke Telegram @NoToScam (Official Scam Report)
        await client.send_message("@NoToScam", f"/report {target} ᴘᴇɴɪᴘᴜᴀɴ, ꜱᴘᴀᴍ, ᴀᴛᴀᴜ ᴋᴏɴᴛᴇɴ ʙᴇʀʙᴀʜᴀʏᴀ.")

        await msg.edit(f"✅ ʟᴀᴘᴏʀᴀɴ ʙᴇʀʜᴀꜱɪʟ ᴅɪᴋɪʀɪᴍ ᴋᴇ:\n- **ɢʀᴜᴘ ᴘʀɪᴠᴀᴛ**\n- **ᴄʜᴀɴɴᴇʟ ʀᴇᴘᴏʀᴛ**\n- **@ɴᴏᴛᴏꜱᴄᴀᴍ ᴛᴇʟᴇɢʀᴀᴍ**")

    except Exception as e:
        await msg.edit(f"❌ ɢᴀɢᴀʟ ᴍᴇɴɢɪʀɪᴍ ʟᴀᴘᴏʀᴀɴ ᴄᴇꜱꜱ:\n<code>{str(e)}</code>")
