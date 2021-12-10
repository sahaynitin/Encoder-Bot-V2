# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from .worker import *
from datetime import datetime

START_TIME = datetime.now()

async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"Ping = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    await event.reply(
        f"**Hey {event.sender.first_name}\n\nThis is A CompressorBot Which Can Encode Videos.\n\nReduce Size of Videos With Negligible Quality Change\n**",
        buttons=[
            
            [Button.inline("HELP", data="help"),
                Button.inline("ABOUT", data="about"),
            ],
        [Button.inline("CLOSE", data="close")],
  ],
    )

async def zylern(event):
    await event.reply(
        f"""
**Available Commands 🤖**

/start - Check Bot is Working Or Not
/help - Get Detailed Help__
/setcode - Set Custom FFMPEG Code
/getcode - Print Current FFMPEG Code
/ping - Check Ping
/leech - Leech Links And Compress Video
/renew - Clear Cached Downloads
/clear - Clear Queued Files
/showthumb - Show Current Thumbnail
/speed - Do A SpeedTest
"""
    )

async def close(event):
    await event.edit(
        f"""**Closed 🔒**"""
    )
async def about(event):
    await event.edit(
        f"**My Name : Encoder Bot\n\nSource : [Click Here](https://t.me/tellybots_digital)\n\nFramework : [Pyrogram](docs.pyrogram.org)\n\nLanguage : [Python](www.python.org)\n\nDeveloper : [Tellybots](https://t.me/tellybots_4u)**",
        buttons=[
            
            [Button.inline("HOME", data="start"),
                Button.inline("HELP", data="help"),
            ],
        [Button.inline("CLOSE", data="close")],
  ],
    )
async def help(event):
    await event.edit(
        f"**A Video Encoder Bot\n\n✶ This Bot Compress Videos With Negligible Quality Change.\n\n✶ Due to Quality Settings Bot Takes Time To Compress.\n\n✶ So Be patience And Send videos One By One After Completing.\n\n✶ Dont Spam Bot.\n\n✶ Choose Compress For Rename And Custom Thumbnail.\n\n✶ Just Forward Video To Get Options**",
        buttons=[
            
            [Button.inline("HOME", data="start"),
                Button.inline("ABOUT", data="about"),
            ],
        [Button.inline("CLOSE", data="close")],
  ],
    )
