from pyrogram.types import *

from PyroUbot import *

__MODULE__ = "ɴᴏᴛᴇ"
__HELP__ = """
<blockquote>Bantuan Untuk Notes Cess

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}addnote</code> [name]
    Menyimpan Sebuah Catatan Cess

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}addcb</code> [name]
    Menyimpan Sebuah Callback Cess

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}get</code> [name]
    Mendapatkan Catatan Yang Di Simpan Cess

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}delnote</code> [name]
    Menghapus Catatan Yang Di Simpan Cess

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}delcb</code> [name]
    Menghapus Callback Yang Di Simpan Cess

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}listnote</code>
   Melihat Daftar Catatan Yang Di Simpan Cess

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}listcb</code>
   Melihat Daftar Callback Yang Di Simpan Cess

for button:
    format | nama tombol - url/callback |

payment | dana - dana | | bank - bank # | 
catatan : untuk Membuat Button Menyamping Adalah #

contoh menggunakan callback/tombol : <a href='https://t.me/TESTIPRIBADIBOYSZ/1605'>tutorial</a></blockquote>
"""


@PY.UBOT("addnote|addcb")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if len(message.command) != 2:
        return await message.reply(f"{ggl}Woi Cuki Mohon Gunakan {message.text.split()[0]} namacatatan/namacb")
    args = get_arg(message)
    reply = message.reply_to_message
    query = "notes_cb" if message.command[0] == "addcb" else "notes"

    if not args or not reply:
        return await message.reply(
            f"{message.text.split()[0]} [name] [text/reply]"
        )

    vars = await get_vars(client.me.id, args, query)

    if vars:
        return await message.reply(f"{ggl}Catatan {args} Sudah Ada Cess</n>")

    value = None
    type_mapping = {
        "text": reply.text,
        "photo": reply.photo,
        "voice": reply.voice,
        "audio": reply.audio,
        "video": reply.video,
        "animation": reply.animation,
        "sticker": reply.sticker,
    }

    for media_type, media in type_mapping.items():
        if media:
            send = await reply.copy(client.me.id)
            value = {
                "type": media_type,
                "message_id": send.id,
            }
            break

    if value:
        await set_vars(client.me.id, args, value, query)
        return await message.reply(
            f"{brhsl}Catatan {args} Berhasil Tersimpan Cess"
        )
    else:
        return await message.reply(
            f"{message.text.split()[0]} [name] [text/reply]"
        )


@PY.UBOT("delnote|delcb")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    args = get_arg(message)

    if not args:
        return await message.reply(
            f"{message.text.split()[0]} [name]"
        )

    query = "notes_cb" if message.command[0] == "delcb" else "notes"
    vars = await get_vars(client.me.id, args, query)

    if not vars:
        return await message.reply(f"{ggl}Catatan {args} Tidak Ditemukan Cess")

    await remove_vars(client.me.id, args, query)
    await client.delete_messages(client.me.id, int(vars["message_id"]))
    return await message.reply(f"<brhsl>{brhsl}Catatan {args} Berhasil Dihapus Cess</brhsl>")


@PY.UBOT("get")
@PY.TOP_CMD
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    msg = message.reply_to_message or message
    args = get_arg(message)

    if not args:
        return await message.reply(
            f"{message.text.split()[0]} [name]"
        )

    data = await get_vars(client.me.id, args, "notes")

    if not data:
        return await message.reply(
            f"{ggl}Catatan {args} Tidak Ditemukan Cess"
        )

    m = await client.get_messages(client.me.id, int(data["message_id"]))

    if data["type"] == "text":
        if matches := re.findall(r"\| ([^|]+) - ([^|]+) \|", m.text):
            try:
                x = await client.get_inline_bot_results(
                    bot.me.username, f"get_notes {client.me.id} {args}"
                )
                return await client.send_inline_bot_result(
                    message.chat.id,
                    x.query_id,
                    x.results[0].id,
                    reply_to_message_id=msg.id,
                )
            except Exception as error:
                await message.reply(error)
        else:
            return await m.copy(message.chat.id, reply_to_message_id=msg.id)
    else:
        return await m.copy(message.chat.id, reply_to_message_id=msg.id)


@PY.UBOT("listnote|listcb")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    query = "notes_cb" if message.command[0] == "listcb" else "notes"
    vars = await all_vars(client.me.id, query)
    if vars:
        msg = f"{brhsl}Daftar Catatan\n\n"
        for x, data in vars.items():
            msg += f" {x} |({data['type']})\n"
        msg += f"\n{ktrng}Total Catatan: {len(vars)}"
    else:
        msg = f"{ggl}Tidak Ada Catatan Tersimpan Cess"

    return await message.reply(msg, quote=True)


@PY.INLINE("^get_notes")
async def _(client, inline_query):
    query = inline_query.query.split()
    data = await get_vars(int(query[1]), query[2], "notes")
    item = [x for x in ubot._ubot if int(query[1]) == x.me.id]
    for me in item:
        m = await me.get_messages(int(me.me.id), int(data["message_id"]))
        buttons, text = create_inline_keyboard(m.text, f"{int(query[1])}_{query[2]}")
        return await client.answer_inline_query(
            inline_query.id,
            cache_time=0,
            results=[
                (
                    InlineQueryResultArticle(
                        title="get notes!",
                        reply_markup=buttons,
                        input_message_content=InputTextMessageContent(text),
                    )
                )
            ],
        )


@PY.CALLBACK("_gtnote")
async def _(client, callback_query):
    _, user_id, *query = callback_query.data.split()
    data_key = "notes_cb" if bool(query) else "notes"
    query_eplit = query[0] if bool(query) else user_id.split("_")[1]
    data = await get_vars(int(user_id.split("_")[0]), query_eplit, data_key)
    item = [x for x in ubot._ubot if int(user_id.split("_")[0]) == x.me.id]
    for me in item:
        try:
            m = await me.get_messages(int(me.me.id), int(data["message_id"]))
            buttons, text = create_inline_keyboard(
                m.text, f"{int(user_id.split('_')[0])}_{user_id.split('_')[1]}", bool(query)
            )
            return await callback_query.edit_message_text(text, reply_markup=buttons)

        except TypeError:
            return await callback_query.answer("Maaf User ErrCessBot Sangat Tolol Saat Mengisi Callback", show_alert=True)
