import os
import base64
import requests
from pyrogram import Client, filters
from PyroUbot import PY

__MODULE__ = "ᴜᴘʟᴏᴀᴅ ᴋᴇ ɢɪᴛʜᴜʙ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴜᴘʟᴏᴀᴅ ꜰɪʟᴇ ᴋᴇ ɢɪᴛʜᴜʙ ᴄᴇꜱꜱ 』</b>

ᴘᴇʀɪɴᴛᴀʜ:
<code>{0}upgh [email] [password]</code> → ʟᴏɢɪɴ ᴋᴇ ɢɪᴛʜᴜʙ.
ʟᴀʟᴜ, ʀᴇᴘʟʏ ꜰɪʟᴇ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪᴜɴɢɢᴀʜ.

ꜱᴜᴍʙᴇʀ: ɢɪᴛʜᴜʙ API.</blockquote></b>
"""

GITHUB_API = "https://api.github.com"

user_sessions = {}  # Menyimpan sesi user sementara

@PY.UBOT("upgh")
async def github_login(client, message):
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        return await message.reply_text("⚠️ ʜᴀʀᴀᴘ ᴍᴀꜱᴜᴋᴋᴀɴ ᴇᴍᴀɪʟ ᴅᴀɴ ᴘᴀꜱꜱᴡᴏʀᴅ ɢɪᴛʜᴜʙ ᴄᴜᴋɪ.\nᴄᴏɴᴛᴏʜ: `.upgh email@gmail.com password123`")
    
    email = args[1]
    password = args[2]
    
    # Mendapatkan token akses dengan Basic Auth
    auth = base64.b64encode(f"{email}:{password}".encode()).decode()
    headers = {"Authorization": f"Basic {auth}"}
    
    user_response = requests.get(f"{GITHUB_API}/user", headers=headers)
    
    if user_response.status_code != 200:
        return await message.reply_text("🚫 ʟᴏɢɪɴ ɢᴀɢᴀʟ ᴄᴜᴋɪ. ᴘᴀꜱᴛɪᴋᴀɴ ᴇᴍᴀɪʟ ᴅᴀɴ ᴘᴀꜱꜱᴡᴏʀᴅ ʙᴇɴᴀʀ ᴄᴇꜱꜱ.")
    
    user_data = user_response.json()
    username = user_data["login"]
    user_sessions[message.chat.id] = {"email": email, "password": password, "username": username}
    
    await message.reply_text(f"✅ ʟᴏɢɪɴ ʙᴇʀʜᴀꜱɪʟ ᴄᴇꜱꜱ!\n👤 ɢɪᴛʜᴜʙ ᴜꜱᴇʀ: `{username}`\n🔹 ꜱɪʟᴀᴋᴀɴ ʀᴇᴘʟʏ ꜰɪʟᴇ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪ-ᴜᴘʟᴏᴀᴅ ᴄᴇꜱꜱ.")


@PY.UBOT(filters.document & filters.reply)
async def upload_to_github(client, message):
    chat_id = message.chat.id
    if chat_id not in user_sessions:
        return await message.reply_text("⚠️ ᴇʟᴜ ʙᴇʟᴜᴍ ʟᴏɢɪɴ! ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ `.upgh email password` ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ ᴄᴇꜱꜱ.")
    
    user_data = user_sessions[chat_id]
    email, password, username = user_data["email"], user_data["password"], user_data["username"]

    file = await message.download()
    file_name = os.path.basename(file)
    
    with open(file, "rb") as f:
        file_content = f.read()
    
    encoded_content = base64.b64encode(file_content).decode()
    
    repo_name = "UserbotUploads"
    file_path = f"uploads/{file_name}"
    
    headers = {"Authorization": f"Basic {base64.b64encode(f'{email}:{password}'.encode()).decode()}"}
    
    repo_check = requests.get(f"{GITHUB_API}/repos/{username}/{repo_name}", headers=headers)
    
    if repo_check.status_code == 404:
        create_repo = requests.post(
            f"{GITHUB_API}/user/repos",
            json={"name": repo_name, "private": False},
            headers=headers,
        )
        if create_repo.status_code != 201:
            return await message.reply_text("🚫 ɢᴀɢᴀʟ ᴍᴇᴍʙᴜᴀᴛ ʀᴇᴘᴏꜱɪᴛᴏʀɪ ᴄᴜᴋɪ.")
    
    upload_url = f"{GITHUB_API}/repos/{username}/{repo_name}/contents/{file_path}"
    
    upload_data = {
        "message": f"Upload {file_name}",
        "content": encoded_content
    }
    
    upload_response = requests.put(upload_url, json=upload_data, headers=headers)
    
    if upload_response.status_code == 201:
        file_url = upload_response.json()["content"]["html_url"]
        await message.reply_text(f"✅ ꜰɪʟᴇ ʙᴇʀʜᴀꜱɪʟ ᴅɪᴜɴɢɢᴀʜ ᴋᴇ ɢɪᴛʜᴜʙ ᴄᴇꜱꜱ!\n🔗 {file_url}")
    else:
        await message.reply_text("🚫 ɢᴀɢᴀʟ ᴍᴇɴɢᴜɴɢɢᴀʜ ꜰɪʟᴇ ᴄᴜᴋɪ.")