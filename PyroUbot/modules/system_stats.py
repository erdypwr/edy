import platform
import sys
import time
import psutil
from datetime import datetime
from PyroUbot import *

__MODULE__ = "ꜱʏꜱᴛᴇᴍ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ꜱʏꜱᴛᴇᴍ 』</b>

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}spc</code>
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴᴀᴍᴘɪʟᴋᴀɴ ꜱᴘᴇꜱɪꜰɪᴋᴀꜱɪ ꜱɪꜱᴛᴇᴍ ᴅᴇᴛᴀɪʟ

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}sysd</code>
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴᴀᴍᴘɪʟᴋᴀɴ ɪɴꜰᴏ ꜱɪꜱᴛᴇᴍ ᴅᴇɴɢᴀɴ ɴᴇᴏꜰᴇᴛᴄʜ

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}botver</code>
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴᴀᴍᴘɪʟᴋᴀɴ ᴠᴇʀꜱɪ ʙᴏᴛ

• ᴘᴇʀɪɴᴛᴀʜ : <code>{0}alive2</code>
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴᴀᴍᴘɪʟᴋᴀɴ ꜱᴛᴀᴛᴜꜱ ʙᴏᴛ
</blockquote>
"""

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

@PY.UBOT(["spc"])
async def _(c, m):
    uname = platform.uname()
    softw = f"<b>ɪɴꜰᴏʀᴍᴀꜱɪ ꜱɪꜱᴛᴇᴍ</b>\n"
    softw += f"ꜱɪꜱᴛᴇᴍ : {uname.system}\n"
    softw += f"ʀɪʟɪꜱ : {uname.release}\n"
    softw += f"ᴠᴇʀꜱɪ : {uname.version}\n"
    softw += f"ᴍᴇꜱɪɴ : {uname.machine}\n"
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"ᴡᴀᴋᴛᴜ ʜɪᴅᴜᴘ: {bt.day}/{bt.month}/{bt.year} {bt.hour}:{bt.minute}:{bt.second}\n"
    cpuu = f"<b>ɪɴꜰᴏʀᴍᴀꜱɪ CPU</b>\n"
    cpuu += f"ᴘʜʏꜱɪᴄᴀʟ ᴄᴏʀᴇꜱ : {psutil.cpu_count(logical=False)}\n"
    cpuu += f"ᴛᴏᴛᴀʟ ᴄᴏʀᴇꜱ : {psutil.cpu_count(logical=True)}\n"
    cpufreq = psutil.cpu_freq()
    cpuu += f"ᴍᴀx ꜰʀᴇQᴜᴇɴᴄʏ : {cpufreq.max:.2f}Mhz\n"
    cpuu += f"ᴍɪɴ ꜰʀᴇQᴜᴇɴᴄʏ : {cpufreq.min:.2f}Mhz\n"
    cpuu += f"ᴄᴜʀʀᴇɴᴛ ꜰʀᴇQᴜᴇɴᴄʏ: {cpufreq.current:.2f}Mhz\n\n"
    cpuu += f"<b>CPU Usage Per Core</b>\n"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpuu += f"ᴄᴏ��ᴇ {i} : {percentage}%\n"
    cpuu += f"<b>Total CPU Usage</b>\n"
    cpuu += f"ꜱᴇᴍᴜᴀ ᴄᴏʀᴇ: {psutil.cpu_percent()}%\n"
    svmem = psutil.virtual_memory()
    memm = f"<b>ᴍᴇᴍᴏʀɪ ᴅɪɢᴜɴᴀᴋᴀɴ</b>\n"
    memm += f"ᴛᴏᴛᴀʟ : {get_size(svmem.total)}\n"
    memm += f"ᴀᴠᴀɪʟᴀʙʟᴇ : {get_size(svmem.available)}\n"
    memm += f"ᴜꜱᴇᴅ : {get_size(svmem.used)}\n"
    memm += f"ᴘᴇʀꜱᴇɴᴛᴀꜱᴇ: {svmem.percent}%\n"
    bw = f"<b>ʙᴀɴᴅᴡɪᴛʜ ᴅɪɢᴜɴᴀᴋᴀɴ</b>\n"
    bw += f"ᴜɴɢɢᴀʜ : {get_size(psutil.net_io_counters().bytes_sent)}\n"
    bw += f"ᴅᴏᴡɴʟᴏᴀᴅ: {get_size(psutil.net_io_counters().bytes_recv)}\n"
    help_string = f"{softw}\n{cpuu}\n{memm}\n{bw}\n"
    help_string += f"<b>ɪɴꜰᴏʀᴍᴀꜱɪ ᴍᴇꜱɪɴ</b>\n"
    help_string += f"Python {sys.version}\n"
    help_string += f"Pyrogram {c.__version__}\n"
    await m.reply(help_string)

@PY.UBOT(["sysd"])
async def _(c, m):
    try:
        proc = await asyncio.create_subprocess_exec(
            "neofetch", "--stdout",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        result = stdout.decode().strip() + stderr.decode().strip()
        await m.reply(f"<b>ɴᴇᴏꜰᴇᴛᴄʜ ʀᴇꜱᴜʟᴛ:</b>\n<code>{result}</code>")
    except FileNotFoundError:
        await m.reply("<b>ɪɴꜱᴛᴀʟʟ ɴᴇᴏꜰᴇᴛᴄʜ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ!</b>")

@PY.UBOT(["botver"])
async def _(c, m):
    if os.system("git --version") == 0:
        proc = await asyncio.create_subprocess_exec(
            "git", "describe", "--all", "--long",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        verout = stdout.decode().strip() + stderr.decode().strip()
        proc2 = await asyncio.create_subprocess_exec(
            "git", "rev-list", "--all", "--count",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout2, stderr2 = await proc2.communicate()
        revout = stdout2.decode().strip() + stderr2.decode().strip()
        await m.reply(f"✥ <b>Userbot Versi :</b> <code>{verout}</code>\n✥ <b>Revisi :</b> <code>{revout}</code>")
    else:
        await m.reply("<b>ɢɪᴛ ᴛɪᴅᴀᴋ ᴛᴇʀᴘᴀꜱᴀɴɢ, ʙᴏᴛ ᴅɪᴊᴀʟᴀɴᴋᴀɴ ᴅɪ ᴠ1.ʙᴇᴛᴀ.4</b>")

@PY.UBOT(["alive2"])
async def _(c, m):
    user = await c.get_me()
    uptime = int(time.time() - getattr(c, 'StartTime', time.time()))
    output = (
        f"<b>ᴘʀᴏɢʀᴀᴍ ᴀᴋᴛɪꜰ! ʙᴏᴛ ꜱɪᴀᴘ ᴅɪɢᴜɴᴀᴋᴀɴ</b>\n\n"
        f" ◉ <b>ᴍᴀꜱᴛᴇʀ :</b> <a href='tg://user?id={user.id}'>{user.first_name}</a>\n"
        f" ◉ <b>ᴍᴏᴅᴜʟᴇꜱ :</b> <code>{len(CMD_HELP)}</code>\n"
        f" ◉ <b>ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪ :</b> <code>{platform.python_version()}</code>\n"
        f" ◉ <b>ʙᴏᴛ ᴜᴘᴛɪᴍᴇ :</b> <code>{uptime}s</code>\n"
    )
    await m.reply(output)
