from PyroUbot import *

__MODULE__ = "ᴄᴏɴᴛʀᴏʟ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴏɴᴛʀᴏʟ 』

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ᴘʀᴇꜰɪx</code>
   ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ᴘʀᴇꜰɪx/ʜᴀɴᴅʟᴇʀ ᴘᴇʀɪɴᴛᴀʜ

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ᴄʀᴇᴀᴛ</code>
   ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ɢʀᴜᴘ ᴀᴛᴀᴜ ᴄʜᴀɴɴᴇʟ

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ᴇᴍᴏᴊɪ</code> ǫᴜᴇʀʏ ᴇᴍᴏᴊɪᴘʀᴇᴍ
   ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ᴇᴍᴏᴊɪ ᴘᴀᴅᴀ ᴛᴀᴍᴘɪʟᴀɴ ᴛᴇʀᴛᴇɴᴛᴜ

ǫᴜᴇʀʏ:
    ><code>{0}ᴘᴏɴɢ</code>
    ><code>{0}ᴏᴡɴᴇʀ</code>
    ><code>{0}ᴜʙᴏᴛ</code>
    ><code>{0}ɢᴄᴀꜱᴛ</code>
    ><code>{0}ꜱᴜᴋꜱᴇꜱ</code>
    ><code>{0}ɢᴀɢᴀʟ</code>
    ><code>{0}ᴘʀᴏꜱᴇꜱ</code>
    ><code>{0}ɢʀᴏᴜᴘ</code>
    ><code>{0}ᴄᴀᴛᴀᴛᴀɴ</code>
    ><code>{0}ᴀꜰᴋ</code>
    ><code>{0}ᴡᴀᴋᴛᴜ</code>
    ><code>{0}ᴀʟᴀꜱᴀɴ</code></b></blockquote>
"""


@PY.UBOT("creat")
@PY.TOP_CMD
async def _(client, message):
    if len(message.command) < 3:
        return await message.reply(
            f"{message.text} [group/channel] [name/titlee]")
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    xd = await message.reply("ᴘʀᴏsᴇs ᴄᴇss...")
    desc = "sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴅɪ " + ("ɢʀᴏᴜᴘ" if group_type == "gc" else "ᴄʜᴀɴɴᴇʟ")
    if group_type == "group":
        _id = await client.create_supergroup(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"ʙᴇʀʜᴀsɪʟ ᴍᴇᴍʙᴜᴀᴛ ɢʀᴜᴘ ᴛᴇʟᴇɢʀᴀᴍ: [{group_name}]({link.invite_link})",
            disable_web_page_preview=True,
        )
    elif group_type == "channel":
        _id = await client.create_channel(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"ʙᴇʀʜᴀsɪʟ ᴍᴇᴍʙᴜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴇʟᴇɢʀᴀᴍ: [{group_name}]({link.invite_link})",
            disable_web_page_preview=True,
        )


@PY.UBOT("prefix")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    Tm = await message.reply(f"{prs}ᴘʀᴏsᴇs ᴄᴇss...", quote=True)
    if len(message.command) < 2:
        return await Tm.edit(f"{ggl}{message.text} [simbol]")
    else:
        ub_prefix = []
        for prefix in message.command[1:]:
            if prefix.lower() == "threnone":
                ub_prefix.append("")
            else:
                ub_prefix.append(prefix)
        try:
            client.set_prefix(message.from_user.id, ub_prefix)
            await set_pref(message.from_user.id, ub_prefix)
            parsed_prefix = " ".join(f"{prefix}" for prefix in ub_prefix)
            return await Tm.edit(f"<blockquote><b>{brhsl}prefix telah diubah ke: {parsed_prefix}</blockquote></b>\n\n<blockquote><b>ᴀᴡᴀs ᴋᴀʟᴏ ʙᴜᴀᴛ ᴘʀᴇғɪx ᴊᴀɴɢᴀɴ sᴀᴍᴘᴇ ʟᴜᴘᴀ ᴘʀᴇғɪx ʏᴀɴɢ ʟᴜ ɢᴀɴᴛɪ ᴀᴘᴀ !!</blockquote></b>")
        except Exception as error:
            return await Tm.edit(str(error))


@PY.UBOT("afk")
@PY.TOP_CMD
async def _(client, message):
    tion = await EMO.AEFKA(client)
    ktrng = await EMO.ALASAN(client)
    reason = get_arg(message)
    db_afk = {"time": time(), "reason": reason}
    msg_afk = (
        f"<blockquote><b>{tion}sᴇᴅᴀɴɢ ᴀꜰᴋ\n{ktrng}ᴀʟᴀsᴀɴ: {reason}</blockquote></b>"
        if reason
        else f"{tion}sᴇᴅᴀɴɢ ᴀꜰᴋ"
      )
    await set_vars(client.me.id, "AFK", db_afk)
    return await message.reply(msg_afk)



@PY.NO_CMD_UBOT("AFK", ubot)
async def _(client, message):
    tion = await EMO.AEFKA(client)
    ktrng = await EMO.ALASAN(client)
    mng = await EMO.WAKTU(client)
    vars = await get_vars(client.me.id, "AFK")
    if vars:
        afk_time = vars.get("time")
        afk_reason = vars.get("reason")
        afk_runtime = await get_time(time() - afk_time)
        rpk = f"[{message.from_user.first_name} {message.from_user.last_name or ''}](tg://user?id={message.from_user.id})"
        afk_text = (
            f"<blockquote><b>{tion}sᴇᴅᴀɴɢ ᴀꜰᴋ\n{mng}ᴡᴀᴋᴛᴜ: {afk_runtime}\n{ktrng}ᴀʟᴀsᴀɴ: {afk_reason}</blockquote></b>"
            if afk_reason
            else f"""
<blockquote><b>ʜᴀʟᴏ {rpk}
tᴜᴀɴ ɢᴜᴀ sᴇᴅᴀɴɢ ᴀꜰᴋ sᴇʟᴀᴍᴀ : {afk_runtime}
ᴍᴏʜᴏɴ ᴛᴜɴɢɢᴜ ʙᴇʙᴇʀᴀᴘᴀ ᴡᴀᴋᴛᴜ</blockquote></b>
"""
        )
        return await message.reply(afk_text)


@PY.UBOT("unafk")
@PY.TOP_CMD
async def _(client, message):
    tion = await EMO.AEFKA(client)
    ktrng = await EMO.ALASAN(client)
    mng = await EMO.WAKTU(client)
    vars = await get_vars(client.me.id, "AFK")
    if vars:
        afk_time = vars.get("time")
        afk_runtime = await get_time(time() - afk_time)
        afk_text = f"<blockquote><b>{tion}ᴋᴇᴍʙᴀʟɪ ᴏɴʟɪɴᴇ\n{mng}ᴀꜰᴋ sᴇʟᴀᴍᴀ: {afk_runtime}</blockquote></b>"
        await message.reply(afk_text)
        return await remove_vars(client.me.id, "AFK")


@PY.UBOT("emoji")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    try:
        msg = await message.reply(f"{prs}ᴘʀᴏsᴇs ᴄᴇss...", quote=True)

        if not client.me.is_premium:
            return await msg.edit(
                f"{ggl}ʙᴇʟɪ ᴘʀᴇᴍ ᴅᴜʟᴜ ʙɪᴀʀ ʙɪsᴀ ᴘᴀᴋᴇ ᴇᴍᴏᴊɪ ᴘʀᴇᴍɪᴜᴍ"
            )

        if len(message.command) < 3:
            return await msg.edit(f"{ggl}ᴍᴀsᴜᴋᴋᴀɴ ǫᴜᴇʀʏ ᴅᴀɴ ᴠᴀʟᴜᴇ ɴʏᴀ ᴄᴇss\n\n")

        query_mapping = {
          "pong": "EMOJI_PING",
          "owner": "EMOJI_MENTION",
          "ubot": "EMOJI_USERBOT",
          "proses": "EMOJI_PROSES",
          "gcast": "EMOJI_BROADCAST",
          "sukses": "EMOJI_BERHASIL",
          "gagal": "EMOJI_GAGAL",
          "catatan": "EMOJI_KETERANGAN",
          "group": "EMOJI_GROUP",
          "menunggu": "EMOJI_MENUNGGU",
          "alasan": "EMOJI_ALASAN",
          "waktu": "EMOJI_WAKTU",
          "afk": "EMOJI_AFKA",
        }
        command, mapping, value = message.command[:3]

        if mapping.lower() in query_mapping:
            query_var = query_mapping[mapping.lower()]
            emoji_id = None
            if message.entities:
                for entity in message.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break

            if emoji_id:
                await set_vars(client.me.id, query_var, emoji_id)
                await msg.edit(
                    f"{brhsl}ᴇᴍᴏᴊɪ ʙᴇʀʜᴀsɪʟ ᴅɪsᴇᴛᴇʟ ᴋᴇ: <emoji id={emoji_id}>{value}</emoji>"
                )
            else:
                await msg.edit(f"{ggl}ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴇᴍᴏᴊɪ ᴘʀᴇᴍɪᴜᴍ ᴄᴇss")
        else:
            await msg.edit(f"{ggl}ᴍᴀᴘᴘɪɴɢ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴄᴇss, ɢᴜɴᴀᴋᴀɴ: {', '.join(query_mapping.keys())}")

    except Exception as error:
        await msg.edit(str(error))

