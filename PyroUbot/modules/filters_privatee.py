from PyroUbot import *

@PY.NO_CMD_UBOT("FILTER_PRIVATE", ubot)
async def _(client, message):
    try:
        chat_logs = client.me.id
        all_filters = await all_vars(client.me.id, "PVT_FILTERS") or {}
        
        # Mengubah pesan teks ke huruf kecil untuk perbandingan
        message_text_lower = message.text.split()[0].lower()
        
        for key, value in all_filters.items():
            # Mengubah kunci filter ke huruf kecil untuk perbandingan
            if key.lower() == message_text_lower:
                msg = await client.get_messages(int(chat_logs), int(value))
                return await msg.copy(message.chat.id, reply_to_message_id=message.id)
    except BaseException as e:
        # Tambahkan logging kesalahan untuk debugging jika diperlukan
        print(f"Error: {e}")
        pass



@PY.UBOT("pfilter")
@PY.TOP_CMD
@PY.PRIVATE
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    txt = await message.reply(f"{prs}<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴄᴇꜱꜱ...</b>")
    arg = get_arg(message)

    if not arg or arg.lower() not in ["off", "on"]:
        return await txt.edit(f"{ggl}<b>ɢᴜɴᴀᴋᴀɴ ᴏɴ/ᴏғғ</b>")

    type = True if arg.lower() == "on" else False
    await set_vars(client.me.id, "FILTER_PVT_ON_OFF", type)
    return await txt.edit(f"<b>{sks}ғɪʟᴛᴇʀs ʙᴇʀʜᴀsɪʟ ᴅɪ sᴇᴛᴛɪɴɢs ᴋᴇ {type}</b>")


@PY.UBOT("paddfilter")
@PY.TOP_CMD
@PY.PRIVATE
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    txt = await message.reply(f"<b>{prs}sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴄᴇꜱꜱ...</b>")
    type, reply = extract_type_and_msg(message)

    if not type and message.reply_to_message:
        return await txt.edit(f"{ggl}<b>ʜᴀʀᴀᴘ ʙᴀʟᴀs ᴘᴇsᴀɴ ᴅᴀɴ ᴋᴀsɪʜ ɴᴀᴍᴀ ᴄᴇꜱꜱ</b>")

    logs = client.me.id
    if bool(logs):
        try:
            msg = await reply.copy(int(logs))
            await set_vars(client.me.id, type, msg.id, "PVT_FILTERS")
            await txt.edit(f"<b>{sks}ғɪʟᴛᴇʀs {type} ʙᴇʀʜᴀsɪʟ ᴅɪ sɪᴍᴘᴀɴ ᴄᴇꜱꜱ</b>")
        except Exception as error:
            await txt.edit(error)
    else:
        return await txt.edit(f"<b>{ggl}ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴜᴀᴛ ғɪʟᴛᴇʀs ʙᴀʀᴜ ᴄᴇꜱꜱ</b>")


@PY.UBOT("pdelfilter")
@PY.TOP_CMD
@PY.PRIVATE
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    txt = await message.reply(f"<b>{prs}ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ ᴄᴇꜱꜱ..</b>")
    arg = get_arg(message)

    if not arg:
        return await txt.edit(f"{ggl}<code>{message.text.split()[0]}</code> <b>ɴᴀᴍᴀ ғɪʟᴛᴇʀ ᴄᴇꜱꜱ</b>")

    logs = client.me.id
    all = await all_vars(client.me.id, "PVT_FILTERS")

    if arg not in all:
        return await txt.edit(f"<b>{ggl}ғɪʟᴛᴇʀ {arg} ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴄᴇꜱꜱ</b>")

    await remove_vars(client.me.id, arg, "PVT_FILTERS")
    await client.delete_messages(logs, all[arg])
    return await txt.edit(f"<b>ғɪʟᴛᴇʀ {arg} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs ᴄᴇꜱꜱ{sks}</b>")

@PY.UBOT("pfilters")
@PY.TOP_CMD
@PY.PRIVATE
async def _(client, message):
    vars = await all_vars(client.me.id, "PVT_FILTERS")
    if vars:
        msg = "<emoji id=5411165185253592513>📝</emoji> ᴅᴀғᴛᴀʀ ғɪʟᴛᴇʀs ᴄᴇꜱꜱ\n"
        for x in vars.keys():
            msg += f"├<emoji id=5316946234278169031>⏩</emoji> {x}\n"
        msg += f" ⤿ ᴛᴏᴛᴀʟ ғɪʟᴛᴇʀs: {len(vars)}"
    else:
        msg = "<emoji id=6114014038960638990>❌</emoji> ᴛɪᴅᴀᴋ ᴀᴅᴀ ғɪʟᴛᴇʀs ʏᴀɴɢ ᴛᴇʀsɪᴍᴘᴀɴ ᴄᴇꜱꜱ"

    return await message.reply(msg, quote=True)
