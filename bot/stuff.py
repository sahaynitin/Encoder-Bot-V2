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
                Button.url("ABOUT", data="about"),
            ],
        [Button.inline("Close", data="close")],
  ],
    )

async def zylern(event):
    await event.reply(
        f"""
**Available Commands 🤖**

/start - __Check Bot is Working Or Not__
/help - __Get Detailed Help__
/setcode - __Set Custom FFMPEG Code__
/getcode - __Print Current FFMPEG Code__
/ping - __Check Ping__
/leech - __Leech Links And Compress Video__
/renew - __Clear Cached Downloads__
/clear - __Clear Queued Files__
/showthumb - __Show Current Thumbnail__
/speed - __Do A SpeedTest__
"""
    )

async def close(event):
    await event.edit(
        f"""**Closed**"""
    )
async def about(event):
    await event.edit(
        f"**🤖 <b>Bot :** URL Uploader</b>\n
 **👲 <b>Developer :** [Tellybots_4u](https://telegram.me/tellybots_4u)</b>\n
 **👥 <b>Channel :** [Tellybots_4u](https://telegram.me/tellybots_4u)</b>\n
 **❄️ <b>Credits :** Everyone in this journey</b>\n
 **🍴 <b>Source :** [Click here](https://t.me/tellybots_digital)</b>\n
 **📝 <b>Language :** [Python3](https://python.org)</b>\n
 **📚 <b>Library :** [Pyrogram v1.2.0](https://pyrogram.org)</b>\n
 **🌟 <b>Server :** [Heroku](https://heroku.com)</b>\n**",
        buttons=[
            
            [Button.inline("HOME", data="start"),
                Button.url("HELP", data="help"),
            ],
        [Button.inline("Close", data="close")],
  ],
    )
async def help(event):
    await event.edit(
        f"**A Video Encoder Bot

✶ This Bot Compress Videos With Negligible Quality Change.

✶ Due to Quality Settings Bot Takes Time To Compress.

✶ So Be patience And Send videos One By One After Completing.

✶ Dont Spam Bot.

✶ Choose Custom Compress For Rename And Custom Thumbnail.

✶ Just Forward Video To Get Options**",
        buttons=[
            
            [Button.inline("HOME", data="start"),
                Button.url("ABOUT", data="about"),
            ],
        [Button.inline("Close", data="close")],
  ],
    )
