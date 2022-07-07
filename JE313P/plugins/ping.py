import os

from telethon import Button, events

from JE313P import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/2ad68bd0e391a69163d0a.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@lMl10l"
)

CAPTION = f"**سرعة البنك:** {ms}\n المالك:『{ALIVE}』"


@JE313P.on(events.NewMessage(pattern="^/بنك"))
async def _(event):
    UMM = [[Button.url("السورس", "https://t.me/JEPTHON")]]
    await JE313P.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
