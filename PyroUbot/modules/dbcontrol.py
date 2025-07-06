from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone


from PyroUbot import *

__MODULE__ = "ᴅʙ ᴄᴏɴᴛʀᴏʟ"
__HELP__ = """
<blockquote><b>Bantuan Untuk DB Control Cess</blockquote></b>

<b>ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ᴛɪᴍᴇ</code>
    ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜ - ᴍᴇɴɢᴜʀᴀɴɢɪ ᴍᴀꜱᴀ ᴀᴋᴛɪꜰ ᴜꜱᴇʀ</b>

<b>ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ᴄᴇᴋ</code>
    ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴍᴀꜱᴀ ᴀᴋᴛɪꜰ ᴜꜱᴇʀ</b>

<b>ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ᴀᴅᴅᴀᴅᴍɪɴ</code> - <code>{0}ᴜɴᴀᴅᴍɪɴ</code> - <code>{0}ɢᴇᴛᴀᴅᴍɪɴ</code></b>

<b>ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ꜱᴇʟᴇꜱ</code> - <code>{0}ᴜɴꜱᴇʟᴇꜱ</code> - <code>{0}ɢᴇᴛꜱᴇʟᴇꜱ</code></b></blockquote>

"""

@PY.BOT("prem")
@PY.SELLER
async def _(client, message):
    user_id, get_bulan = await extract_user_and_reason(message)
    msg = await message.reply("ᴘʀᴏsᴇs ᴄᴇss...")
    if not user_id:
        return await msg.edit(f"<b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ - ʙᴜʟᴀɴ</b>")

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)
    if not get_bulan:
        get_bulan = 1

    prem_users = await get_list_from_vars(client.me.id, "PREM_USERS")

    if user.id in prem_users:
        return await msg.edit(f"""
<blockquote><b>ɴᴀᴍᴀ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: {user.id}</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: sᴜᴅᴀʜ ᴘʀᴇᴍɪᴜᴍ</b>
<bᴋᴀᴅᴀʟᴜᴡᴀʀsᴀ: {get_bulan} ʙᴜʟᴀɴ</b></blockquote>
"""
        )

    try:
        now = datetime.now(timezone("Asia/Jakarta"))
        expired = now + relativedelta(months=int(get_bulan))
        await set_expired_date(user_id, expired)
        await add_to_vars(client.me.id, "PREM_USERS", user.id)
        await msg.edit(f"""
<blockquote><b>ɴᴀᴍᴀ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: {user.id}</b>
<b>ᴋᴀᴅᴀʟᴜᴡᴀʀsᴀ: {get_bulan} ʙᴜʟᴀɴ</b>
<b>sɪʟᴀʜᴋᴀɴ ʙᴜᴋᴀ @{client.me.username} ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ ᴄᴇss</b></blockquote>

<blockquote>ᴄᴀʀᴀ ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ :
- sɪʟᴀʜᴋᴀɴ /start ᴅᴜʟᴜ ʙᴏᴛ @ubotjella_bot
- ᴋᴀʟᴀᴜ sᴜᴅᴀʜ sᴛᴀʀᴛ ʙᴏᴛ ᴀʙɪsᴛᴜ ᴘᴇɴᴄᴇᴛ ᴛᴏᴍʙᴏʟ ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ 
- ɴᴀʜ ɴᴀɴᴛɪ ᴀᴅᴀ ᴀʀᴀʜᴀɴ ᴅᴀʀɪ ʙᴏᴛ ɴʏᴀ ɪᴛᴜ ɪᴋᴜᴛɪɴ</blockquote>
<blockquote><b>ᴄᴀᴛᴀᴛᴀɴ : ɢᴜɴᴀᴋᴀɴ ʟᴜᴘᴀ ʙᴀᴄᴀ ᴀʀᴀʜᴀɴ ᴅᴀʀɪ ʙᴏᴛ ɴʏᴀ</b></blockquote>
"""
        )
        return await bot.send_message(
            OWNER_ID,
            f"🆔 id-seller: {message.from_user.id}\n\n🆔 id-customer: {user_id}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🔱 Seller",
                            callback_data=f"profil {message.from_user.id}",
                        ),
                        InlineKeyboardButton(
                            "Customer ⚜️", callback_data=f"profil {user_id}"
                        ),
                    ],
                ]
            ),
        )
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("unprem")
@PY.SELLER
async def _(client, message):
    msg = await message.reply("ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<b>{message.text} user_id/username</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    prem_users = await get_list_from_vars(client.me.id, "PREM_USERS")

    if user.id not in prem_users:
        return await msg.edit(f"""
 ɪɴғᴏʀᴍᴀᴛɪᴏɴ :
 <blockquote><b>name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
 <b>id: {user.id}</b>
 <b>keterangan: tidak dalam daftar</b></blockquote>
 """
        )
    try:
        await remove_from_vars(client.me.id, "PREM_USERS", user.id)
        await rem_expired_date(user_id)
        return await msg.edit(f"""
 ɪɴғᴏʀᴍᴀᴛɪᴏɴ :
 <blockquote><b>name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
 <b>id: {user.id}</b>
 <b>keterangan: unpremium</b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)
        

@PY.BOT("getprem")
@PY.SELLER
async def _(client, message):
    text = ""
    count = 0
    prem = await get_list_from_vars(client.me.id, "PREM_USERS")
    prem_users = []

    for user_id in prem:
        try:
            user = await bot.get_users(user_id)
            count += 1
            userlist = f"• {count}: <a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"<blockquote><b>{userlist}\n</blockquote></b>"
    if not text:
        await message.reply_text("ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇɴɢɢᴜɴᴀ ʏᴀɴɢ ᴅɪ ᴛᴇᴍᴜᴋᴀɴ ᴄᴇꜱꜱ")
    else:
        await message.reply_text(text)


@PY.BOT("seles")
@PY.ADMIN
async def _(client, message):
    msg = await message.reply("ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<b>{message.text} user_id/username</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = await get_list_from_vars(client.me.id, "SELER_USERS")

    if user.id in sudo_users:
        return await msg.edit(f"""
 ɪɴғᴏʀᴍᴀᴛɪᴏɴ :
 <blockquote><b>name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
 <b>id: {user.id}</b>
 <b>keterangan: Sudah Seller Cess</b></blockquote>
"""
        )

    try:
        await add_to_vars(client.me.id, "SELER_USERS", user.id)
        return await msg.edit(f"""
 ɪɴғᴏʀᴍᴀᴛɪᴏɴ :
 <blockquote><b>name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
 <b>id: {user.id}</b>
 <b>keterangan: Seller</b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("unseles")
@PY.ADMIN
async def _(client, message):
    msg = await message.reply("ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<b>{message.text} user_id/username</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    seles_users = await get_list_from_vars(client.me.id, "SELER_USERS")

    if user.id not in seles_users:
        return await msg.edit(f"""
 ɪɴғᴏʀᴍᴀᴛɪᴏɴ Cess :
 <blockquote><b>name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
 </b>id: {user.id}</b>
 </b>keterangan: Tidak Dalam Daftar</b></blockquote>
"""
        )

    try:
        await remove_from_vars(client.me.id, "SELER_USERS", user.id)
        return await msg.edit(f"""
 ɪɴғᴏʀᴍᴀᴛɪᴏɴ Cess :
 <blockquote><b>name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
 </b>id: {user.id}</b>
 </b>keterangan: Unseller</b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("getseles")
@PY.ADMIN
async def _(client, message):
    Sh = await message.reply("ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    seles_users = await get_list_from_vars(client.me.id, "SELER_USERS")

    if not seles_users:
        return await Sh.edit("Daftar Seller Kosong Cess")

    seles_list = []
    for user_id in seles_users:
        try:
            user = await client.get_users(int(user_id))
            seles_list.append(
                f"<blockquote><b>👤 [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | <code>{user.id}</code></blockquote></b>"
            )
        except:
            continue

    if seles_list:
        response = (
            "📋 ᴅᴀғᴛᴀʀ sᴇʟʟᴇʀ ᴄᴇꜱꜱ:\n\n"
            + "\n".join(seles_list)
            + f"\n\n<blockquote.⚜️ Total Seller Cess: {len(seles_list)}</blockquote>"
        )
        return await Sh.edit(response)
    else:
        return await Sh.edit("Tidak Dapat Mengambil Daftar Seller Cess")


@PY.BOT("time")
@PY.SELLER
async def _(client, message):
    Tm = await message.reply("ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ . . .")
    bajingan = message.command
    if len(bajingan) != 3:
        return await Tm.edit(f"Woi Cuki ! \n🗿Mohon Gunakan /set_time user_id hari")
    user_id = int(bajingan[1])
    get_day = int(bajingan[2])
    print(user_id , get_day)
    try:
        get_id = (await client.get_users(user_id)).id
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    if not get_day:
        get_day = 30
    now = datetime.now(timezone("Asia/Jakarta"))
    expire_date = now + timedelta(days=int(get_day))
    await set_expired_date(user_id, expire_date)
    await Tm.edit(f"""
 ɪɴғᴏʀᴍᴀᴛɪᴏɴ :
 name: {user.mention}
 id: {get_id}
 aktifkan_selama: {get_day} hari
"""
    )


@PY.BOT("cek")
@PY.SELLER
async def _(client, message):
    Sh = await message.reply("ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ . . .")
    user_id = await extract_user(message)
    if not user_id:
        return await Sh.edit("Pengguna Tidak Ditemukan Cess\n\nGunakan ᴘᴇʀɪɴᴛᴀʜ: /cek [user_id/username]")
    try:
        get_exp = await get_expired_date(user_id)
        sh = await client.get_users(user_id)
    except Exception as error:
        return await Sh.edit(error)
    if get_exp is None:
        await Sh.edit(f"""
INFORMATION Cess
name : {sh.mention}
plan : none
id : {user_id}
prefix : .
expired : Nonaktif
""")
    else:
        SH = await ubot.get_prefix(user_id)
        exp = get_exp.strftime("%d-%m-%Y")
        if user_id in await get_list_from_vars(client.me.id, "ULTRA_PREM"):
            status = "SuperUltra"
        else:
            status = "Premium"
        await Sh.edit(f"""
INFORMATION Cess
name : {sh.mention}
plan : {status}
id : {user_id}
prefix : {' '.join(SH)}
expired : {exp}
"""
        )


@PY.BOT("addadmin")
@PY.OWNER
async def _(client, message):
    msg = await message.reply("ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"{message.text} user_id/username"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    admin_users = await get_list_from_vars(client.me.id, "ADMIN_USERS")

    if user.id in admin_users:
        return await msg.edit(f"""
💬 INFORMATION Cess
name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
id: {user.id}
keterangan: Sudah Dalam Daftar Admin
"""
        )

    try:
        await add_to_vars(client.me.id, "ADMIN_USERS", user.id)
        return await msg.edit(f"""
💬 INFORMATION Cess
name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
id: {user.id}
keterangan: Admin
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("unadmin")
@PY.OWNER
async def _(client, message):
    msg = await message.reply("ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"{message.text} user_id/username"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    admin_users = await get_list_from_vars(client.me.id, "ADMIN_USERS")

    if user.id not in admin_users:
        return await msg.edit(f"""
💬 INFORMATION Cess
name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
id: {user.id}
keterangan: Tidak Dalam Daftar
"""
        )

    try:
        await remove_from_vars(client.me.id, "ADMIN_USERS", user.id)
        return await msg.edit(f"""
💬 INFORMATION Cess
name: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
id: {user.id}
keterangan: Unadmin
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("getadmin")
@PY.OWNER
async def _(client, message):
    Sh = await message.reply("ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    admin_users = await get_list_from_vars(client.me.id, "ADMIN_USERS")

    if not admin_users:
        return await Sh.edit("<s>Daftar Admin Kosong Cess</s>")

    admin_list = []
    for user_id in admin_users:
        try:
            user = await client.get_users(int(user_id))
            admin_list.append(
                f"👤 [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | {user.id}"
            )
        except:
            continue

    if admin_list:
        response = (
            "📋 Daftar Admin Cess:\n\n"
            + "\n".join(admin_list)
            + f"\n\n⚜️ Total Admin: {len(admin_list)}"
        )
        return await Sh.edit(response)
    else:
        return await Sh.edit("Tidak Dapat Mengambil Daftar Admin Cess")

@PY.BOT("superultra")
@PY.SELLER
async def _(client, message):
    user_id, get_bulan = await extract_user_and_reason(message)
    msg = await message.reply("ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    if not user_id:
        return await msg.edit(f"{message.text} user_id/username")

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)
    if not get_bulan:
        get_bulan = 1

    prem_users = await get_list_from_vars(client.me.id, "ULTRA_PREM")

    if user.id in prem_users:
        return await msg.edit(f"""
<b>name:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>id:</b> {user.id}
<b>keterangan: sudah</b> <code>[SuperUltra]</code>
<b>expired:</b> <code>{get_bulan}</code> <b>bulan</b>
"""
        )

    try:
        now = datetime.now(timezone("Asia/Jakarta"))
        expired = now + relativedelta(months=int(get_bulan))
        await set_expired_date(user_id, expired)
        await add_to_vars(client.me.id, "ULTRA_PREM", user.id)
        await msg.edit(f"""
<b>name:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>id:</b> <code>{user.id}</code>
<b>expired:</b> <code>{get_bulan}</code> <b>bulan</b>
<b>ꜱilahkan buka</b> @{client.me.mention} <b>untuk membuat userbot cess</b>
<b>status : </b><code>[SuperUltra]</code>
"""
        )
        return await bot.send_message(
            OWNER_ID,
            f"🆔 id-seller: {message.from_user.id}\n\n🆔 id-customer: {user_id}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🔱 Seller",
                            callback_data=f"profil {message.from_user.id}",
                        ),
                        InlineKeyboardButton(
                            "Customer ⚜️", callback_data=f"profil {user_id}"
                        ),
                    ],
                ]
            ),
        )
    except Exception as error:
        return await msg.edit(error)

@PY.BOT("rmultra")
@PY.SELLER
async def _(client, message):
    msg = await message.reply("ᴘʀᴏꜱᴇꜱꜱ ᴄᴇꜱꜱ...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"{message.text} user_id/username"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    prem_users = await get_list_from_vars(client.me.id, "ULTRA_PREM")

    if user.id not in prem_users:
        return await msg.edit(f"""
<b>name:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>id:</b> <code>{user.id}</code>
<b>keterangan: Tidak Dalam Daftar</b>
"""
        )
    try:
        await remove_from_vars(client.me.id, "ULTRA_PREM", user.id)
        await rem_expired_date(user_id)
        return await msg.edit(f"""
<b>name:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>id:</b> <code>{user.id}</code>
<b>keterangan: None Superultra</b>
"""
        )
    except Exception as error:
        return await msg.edit(error)
        

@PY.BOT("getultra")
@PY.SELLER
async def _(client, message):
    prem = await get_list_from_vars(client.me.id, "ULTRA_PREM")
    prem_users = []

    for user_id in prem:
        try:
            user = await client.get_users(user_id)
            prem_users.append(
                f"👤 [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | {user.id}"
            )
        except Exception as error:
            return await message.reply(str(error))

    total_prem_users = len(prem_users)
    if prem_users:
        prem_list_text = "\n".join(prem_users)
        return await message.reply(
            f"📋 Daftar Superultra:\n\n{prem_list_text}\n\n⚜️ Total Superultra: {total_prem_users}"
        )
    else:
        return await message.reply("Tidak Ada Pengguna Superultra Saat Ini Cess")
