from telethon import events, Button
from JE313P import JE313P
from JE313P.status import *
import time

PR_HELP = """
**✘ هذه هي قائمة اوامر التنظيف الحاصة بي*

‣ `تنظيف`
بالرد على رسالة لحذف ما تحتها من الرسائل 

‣ `مسح`
بالرد على رسالة لحذفها

"""

@JE313P.on(events.NewMessage(pattern=r"^[?!]تنظيف"))
@is_admin
async def purge_messages(event, perm):
    if not perm.delete_messages:
         await event.reply("تحتاج الى صلاحيات الحذف اولا")
         return
    start = time.perf_counter()
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply(
            "يجب عليك الرد على الرسالة التي تريد حذف ما اسفلها")
        return
    messages = []
    message_id = reply_msg.id
    delete_to = event.message.id

    messages.append(event.reply_to_msg_id)
    for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []

    await event.client.delete_messages(event.chat_id, messages)
    time_ = time.perf_counter() - start
    text = f"تم التنظيف في {time_:0.2f} من الثواني"
    await event.respond(text, parse_mode='markdown')



@JE313P.on(events.NewMessage(pattern="^[!?/]مسح$"))
@is_admin
async def delete_messages(event, perm):
    if not perm.delete_messages:
       await event.reply("- تحتاج الى صلاحيات الحذف اولا")
       return
    msg = await event.get_reply_message()
    if not msg:
      await event.reply("يجب عليك الرد على الرسالة المراد حذفها")
      return

    await msg.delete()
    await event.delete()

@JE313P.on(events.callbackquery.CallbackQuery(data="purges"))
async def _(event):
    await event.edit(PR_HELP, buttons=[[Button.inline("رجوع", data="help")]])
