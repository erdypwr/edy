import platform
import sys
from datetime import datetime
import psutil
from asyncio import create_subprocess_exec as asyncrunapp
from pyrogram import filters, Client
from pyrogram import __version__
from pyrogram.types import Message
from PyroUbot import *

__MODULE__ = "ꜱʏꜱᴛᴇᴍ"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱʏꜱᴛᴇᴍ ᴄᴇꜱꜱ 』</b>
<blockquote>
⎆ ᴘᴇʀɪɴᴛᴀʜ :
ᚗ <code>{0}ꜱᴘᴄ</code>

⎆ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ:
⊶ ᴍᴇʟɪʜᴀᴛ ꜱᴛᴀᴛɪꜱᴛɪᴋ ꜱɪꜱᴛᴇᴍ.
</blockquote>
"""

async def get_readable_time(seconds: int) -> str: 
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

@PY.UBOT("spc")
@PY.TOP_CMD
async def psu(client: Client, message: Message):
    uname = platform.uname()
    softw = f"""<blockquote><b>ɪɴꜰᴏʀᴍᴀꜱɪ ꜱɪꜱᴛᴇᴍ</b></blockquote>\n"""
    softw += f"ᚗ ꜱɪꜱᴛᴇᴍ   : {uname.system}\n"
    softw += f"ᚗ ʀɪʟɪꜱ    : {uname.release}\n"
    softw += f"ᚗ ᴠᴇʀꜱɪ    : {uname.version}\n"
    softw += f"ᚗ ᴍᴇꜱɪɴ    : {uname.machine}\n"
    # Boot Time
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"ᚗ ᴡᴀᴋᴛᴜ ʜɪᴅᴜᴘ: {bt.day}/{bt.month}/{bt.year}  {bt.hour}:{bt.minute}:{bt.second}\n"
    # CPU Cores
    cpuu = f"""<blockquote><b>ɪɴꜰᴏʀᴍᴀꜱɪ ᴄᴘᴜ</b></blockquote>\n"""
    cpuu += "ᚗ ᴘʜʏꜱɪᴄᴀʟ ᴄᴏʀᴇꜱ   : " + \
        str(psutil.cpu_count(logical=False)) + "\n"
    cpuu += "ᚗ ᴛᴏᴛᴀʟ ᴄᴏʀᴇꜱ      : " + \
        str(psutil.cpu_count(logical=True)) + "\n"
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    cpuu += f"ᚗ ᴍᴀx ꜰʀᴇǫᴜᴇɴᴄʏ    : {cpufreq.max:.2f}ᴍʜᴢ\n"
    cpuu += f"ᚗ ᴍɪɴ ꜰʀᴇǫᴜᴇɴᴄʏ    : {cpufreq.min:.2f}ᴍʜᴢ\n"
    cpuu += f"ᚗ ᴄᴜʀʀᴇɴᴛ ꜰʀᴇǫᴜᴇɴᴄʏ: {cpufreq.current:.2f}ᴍʜᴢ\n\n"
    # CPU usage
    cpuu += f"""<blockquote><b>ᴄᴘᴜ ᴜꜱᴀɢᴇ ᴘᴇʀ ᴄᴏʀᴇ</b></blockquote>\n"""
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpuu += f"ᚗ ᴄᴏʀᴇ {i}  : {percentage}%\n"
    cpuu += f"ᚗ ꜱᴇᴍᴜᴀ ᴄᴏʀᴇ: {psutil.cpu_percent()}%\n"
    # RAM Usage
    svmem = psutil.virtual_memory()
    memm = f"""<blockquote><b>ᴍᴇᴍᴏʀɪ ᴅɪɢᴜɴᴀᴋᴀɴ</b></blockquote>\n"""
    memm += f"ᚗ ᴛᴏᴛᴀʟ     : {get_size(svmem.total)}\n"
    memm += f"ᚗ ᴀᴠᴀɪʟᴀʙʟᴇ : {get_size(svmem.available)}\n"
    memm += f"ᚗ ᴜꜱᴇᴅ      : {get_size(svmem.used)}\n"
    memm += f"ᚗ ᴘᴇʀᴄᴇɴᴛᴀɢᴇ: {svmem.percent}%\n"
    # Bandwidth Usage
    bw = f"""<blockquote><b>ʙᴀɴᴅᴡɪᴛʜ ᴅɪɢᴜɴᴀᴋᴀɴ**</b></blockquote>\n"""
    bw += f"ᚗ ᴜɴɢɢᴀʜ  : {get_size(psutil.net_io_counters().bytes_sent)}\n"
    bw += f"ᚗ ᴅᴏᴡɴʟᴏᴀᴅ: {get_size(psutil.net_io_counters().bytes_recv)}\n"
    help_string = f"{str(softw)}\n"
    help_string += f"{str(cpuu)}\n"
    help_string += f"{str(memm)}\n"
    help_string += f"{str(bw)}\n"
    help_string += f"""<blockquote><b>ɪɴꜰᴏʀᴍᴀꜱɪ ᴍᴇꜱɪɴ</b></blockquote>\n"""
    help_string += f"ᚗ ᴘʏᴛʜᴏɴ {sys.version}\n"
    help_string += f"ᚗ ᴘʏʀᴏɢʀᴀᴍ {__version__}\n\n"
    help_string += f"**ᴘᴏᴡᴇʀᴇᴅ ʙʏ {client.me.mention}**\n"
    await message.reply(help_string)
