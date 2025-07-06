from PyroUbot import *

__MODULE__ = "ғɪʟᴛᴇʀ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ғɪʟᴛᴇʀs ᴄᴇꜱꜱ 』</b>

<b>ɴᴏᴛᴇs: ᴛʜɪs ɪs ᴏɴʟʏ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ</b>

<b>⌲ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}pfilter</code> ᴏʀ <code>{0}filter</code>
   <code>ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴀᴛᴀᴜ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ғɪʟᴛᴇʀs ᴘʀɪᴠᴀᴛᴇ ᴏʀ ɢʀᴏᴜᴘ</code>

<b>⌲ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}paddfilter</code> ᴏʀ <code>{0}addfilter</code>
   <code>ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ғɪʟᴛᴇʀs ᴋᴇ ᴅᴀᴛᴀʙᴀsᴇ</code>

<b>⌲ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}pdelfilter</code> ᴏʀ <code>{0}delfilter</code>
   <code>ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ғɪʟᴛᴇʀs ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀsᴇ</b>

<b>⌲ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}pfilters</code> ᴏʀ <code>{0}filters</code>
   <code>ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ sᴇᴍᴜᴀ ᴅᴀғᴛᴀʀ ғɪʟᴛᴇʀs</code>

<b>ɴᴏᴛᴇs</b> : <b>ᴘ ᴜɴᴛᴜᴋ ᴄʜᴀᴛ ᴘʀɪᴠᴀᴛᴇ ᴅᴀɴ sᴇʙᴀʟɪᴋɴʏᴀ</b></blockquote>
"""
@PY.NO_CMD_UBOT("FILTER_MSG", ubot)
async def _(client, message):
    try:
        chat_logs = client.me.id
        all_filters = await all_vars(client.me.id, "FILTERS") or {}
        
        for key, value in all_filters.items():
            if key == message.text.split()[0]:
                msg = await client.get_messages(int(chat_logs), int(value))
                return await msg.copy(message.chat.id, reply_to_message_id=message.id)
    except BaseException:
        pass

@PY.UBOT("filter")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    txt = await message.reply(f"{prs}<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴄᴇꜱꜱ...</b>")
    arg = get_arg(message)

    if not arg or arg.lower() not in ["off", "on"]:
        return await txt.edit(f"{ggl}<b>ɢᴜɴᴀᴋᴀɴ ᴏɴ/ᴏғғ</b>")

    type = True if arg.lower() == "on" else False
    await set_vars(client.me.id, "FILTER_ON_OFF", type)
    return await txt.edit(f"<b>{sks}ғɪʟᴛᴇʀs ʙᴇʀʜᴀsɪʟ ᴅɪ sᴇᴛᴛɪɴɢs ᴋᴇ {type}</b>")


@PY.UBOT("addfilter")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    txt = await message.reply(f"<b>{prs}sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴄᴇꜱꜱ...</b>")
    type, reply = extract_type_and_msg(message)

    if not type and message.reply_to_message:
        return await txt.edit(f"{ggl}<b>ʜᴀʀᴀᴘ ʙᴀʟᴀs ᴘᴇsᴀɴ ᴅᴀɴ ᴋᴀsɪʜ ɴᴀᴍᴀ</b>")

    logs = client.me.id
    if bool(logs):
        try:
            msg = await reply.copy(int(logs))
            await set_vars(client.me.id, type, msg.id, "FILTERS")
            await txt.edit(f"<b>{sks}ғɪʟᴛᴇʀs {type} ʙᴇʀʜᴀsɪʟ ᴅɪ sɪᴍᴘᴀɴ ᴄᴇꜱꜱ</b>")
        except Exception as error:
            await txt.edit(error)
    else:
        return await txt.edit(f"<b>{ggl}ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴜᴀᴛ ғɪʟᴛᴇʀs ʙᴀʀᴜ ᴄᴇꜱꜱ</b>")


@PY.UBOT("delfilter")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    txt = await message.reply(f"<b>{prs}ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ ᴄᴇꜱꜱ..</b>")
    arg = get_arg(message)

    if not arg:
        return await txt.edit(f"{ggl}<code>{message.text.split()[0]}</code> <b>ɴᴀᴍᴀ ғɪʟᴛᴇʀ</b>")

    logs = client.me.id
    all = await all_vars(client.me.id, "FILTERS")

    if arg not in all:
        return await txt.edit(f"<b>{ggl}ғɪʟᴛᴇʀ {arg} ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴄᴇꜱꜱ</b>")

    await remove_vars(client.me.id, arg, "FILTERS")
    await client.delete_messages(logs, all[arg])
    return await txt.edit(f"<b>ғɪʟᴛᴇʀ {arg} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs ᴄᴇꜱꜱ{sks}</b>")


@PY.UBOT("filters")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    vars = await all_vars(client.me.id, "FILTERS")
    if vars:
        msg = "<emoji id=5411165185253592513>📝</emoji> ᴅᴀғᴛᴀʀ ғɪʟᴛᴇʀs\n"
        for x in vars.keys():
            msg += f"├<emoji id=5316946234278169031>⏩</emoji> {x}\n"
        msg += f" ⤿ ᴛᴏᴛᴀʟ ғɪʟᴛᴇʀs: {len(vars)}"
    else:
        msg = "<emoji id=6114014038960638990>❌</emoji> ᴛɪᴅᴀᴋ ᴀᴅᴀ ғɪʟᴛᴇʀs ʏᴀɴɢ ᴛᴇʀsɪᴍᴘᴀɴ ᴄᴇꜱꜱ"

    return await message.reply(msg, quote=True)
