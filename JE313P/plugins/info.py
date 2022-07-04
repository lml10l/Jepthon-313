from telethon import events, Button, types
from JE313P import JE313P
from JE313P.status import *
from telethon.tl.types import ChannelParticipantsAdmins
from datetime import timedelta
from telethon.tl.functions.photos import GetUserPhotosRequest as P
from telethon.tl.functions.users import GetFullUserRequest


MISC_HELP = """
**✘ بعض اوامر البسيطة للكشف والايدي.**

!الايدي
بالرد على المستخدم لأظهار ايديه او ايدي المجموعة

!ايدي
لعرض معلومات المستخدم بالرد عليه
"""

@JE313P.on(events.NewMessage(pattern="^[!?/]الايدي"))
async def id(event):

    if event.is_private:
       await event.reply(f"الايدي الخاص بك هو`{event.sender_id}`.")
       return

    ID = """
**ايدي الدردشة :** `{}`
**ايدي المستخدم:** `{}`
"""

    msg = await event.get_reply_message()
    if not msg:
      await event.reply(ID.format(event.chat_id, event.sender_id))
      return

    await event.reply(f"المستخدم {msg.sender.first_name} /n الايدي `{msg.sender_id}`.")
 
@JE313P.on(events.NewMessage(pattern="^[!?/]ايدي ?(.*)"))
async def info(event):

    sed = await JE313P(P(user_id=event.sender_id, offset=42, max_id=0, limit=80))
    hn = await JE313P(GetFullUserRequest(event.sender_id))
    text = "**معلومات المستخدم:**\n\n"
    text += "**الاسم الاول:** {}\n"
    text += "**الاسم الثاني:** {}\n"
    text += "**الايدي:** `{}`\n"
    text += "**المعرف:** @{}\n"
    text += "**عدد الصور:** `{}`\n"
    text += "**النبذة:** `{}`\n"
    text += "**رابط حسابه:** [اضغط هنا](tg://user?id={})\n"

    input_str = event.pattern_match.group(1)
    if not input_str:
          await JE313P.send_message(event.chat_id, text.format(hn.user.first_name, hn.user.last_name, event.sender_id, event.sender.username, sed.count, hn.about, event.sender_id))
          return
 
    input_str = event.pattern_match.group(1)
    ha = await JE313P.get_entity(input_str)
    hu = await JE313P(GetFullUserRequest(id=input_str))
    sedd = await JE313P(P(user_id=input_str, offset=42, max_id=0, limit=80))

    textn = "**معلومات المستخدم:**\n\n"
    textn += "**الاسم الاول:** {}\n"
    textn += "**الاسم الثاني:** {}\n"
    textn += "**الايدي:** `{}`\n"
    textn += "**المعرف:** @{}\n"
    textn += "**عدد الصور:** `{}`\n"
    textn += "**النبذة:** `{}`\n"
    textn += "**رابط حسابه:** [اضغط هنا](tg://user?id={})\n"

    await event.reply(textn.format(ha.first_name, ha.last_name, ha.id, ha.username, sedd.count, hu.about, ha.id))
   

@JE313P.on(events.callbackquery.CallbackQuery(data="misc"))
async def _(event):
    await event.edit(MISC_HELP, buttons=[[Button.inline("رجوع", data="help")]])
