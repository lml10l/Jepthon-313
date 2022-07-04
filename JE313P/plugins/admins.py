import JE313P
from telethon import events, Button
from JE313P import JE313P
from JE313P.status import *
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

@JE313P.on(events.callbackquery.CallbackQuery(data="admin"))
async def _(event):

    await event.edit(ADMIN_TEXT, buttons=[[Button.inline("« رجوع", data="help")]])

@JE313P.on(events.callbackquery.CallbackQuery(data="play"))
async def _(event):

    await event.edit(PLAY_TEXT, buttons=[[Button.inline("« رجوع", data="help")]])

@JE313P.on(events.NewMessage(pattern="^[!?/]رفع ?(.*)"))
@is_admin
async def promote(event, perm):
    if event.is_private:
       await event.reply("يستخدم هذا الامر فقط في المجموعات")
       return

    if not perm.add_admins:
        await event.reply("يجب ان تكون لديك صلاحيات الحظر لتنفيذ هذا الامر")
        return
    input_str = event.pattern_match.group(1)
    user = await event.get_reply_message()
    if not input_str and not user:
        await event.reply("يجب عليك الرد على المستخدم لرفعه ")
        return
    sed = await JE313P(GetFullUserRequest(id=user.sender_id or input_str))
    await JE313P(EditAdminRequest(event.chat_id, user.sender_id or input_str, ChatAdminRights(
                    add_admins=False,
                    invite_users=True,
                    change_info=False,
                    ban_users=True,
                    delete_messages=True,
                    pin_messages=True), rank="Admin"))

    if not input_str:
        await event.reply(f"- تم بنجاح رفع [{sed.user.first_name}](tg://user?id={user.sender_id}) في {event.chat.title}!")
        return

    await event.reply(f"تم بنجاح رفع المستخدم {input_str} in {event.chat.title}")
 
@JE313P.on(events.NewMessage(pattern="^[!?/]تنزيل ?(.*)"))
@is_admin
async def promote(event, perm):
    if event.is_private:
       await event.reply("يستخدم هذا الامر فقط في المجموعات")
       return
    if not perm.add_admins:
        await event.reply("يجب ان تكون لديك صلاحيات الحظر لتنفيذ هذا الامر")
        return
    input_str = event.pattern_match.group(1)
    user = await event.get_reply_message()
    if not input_str and not user:
        await event.reply("يجب عليك الرد على المستخدم الذي تريد تنزيله")
        return
    sed = await JE313P(GetFullUserRequest(id=user.sender_id or input_str))
    await JE313P(EditAdminRequest(event.chat_id, user.sender_id or input_str, ChatAdminRights(
                    add_admins=False,
                    invite_users=None,
                    change_info=None,
                    ban_users=None,
                    delete_messages=None,
                    pin_messages=None), rank="Not Admin"))

    if not input_str:
        await event.reply(f"- تم بنجاح تنزيل[{sed.user.first_name}](tg://user?id={user.sender_id}) في {event.chat.title}!")
        return

    await event.reply(f"- تم بنجاح تنزيل {input_str} in {event.chat.title}")
 

@JE313P.on(events.NewMessage(pattern="^[!?/]الرابط"))
async def invitelink(event):

    if event.is_private:
       await event.reply("يستخدم هذا الامر فقط في المجموعات !")
       return
    link = await JE313P(ExportChatInviteRequest(event.chat_id))
    await event.reply(f"المجموعة {event.chat.title}الرابط: [اضغط هنا]({link.link})", link_preview=False)

ADMIN_TEXT = """
**✘ جميع اوامر الادمن تحتاج الى ان تكون مشرف**

!رفع
( لرفع المستخدم مشرف )

!تنزيل
( لتنزيل المستخدم من رتبة الاشراف بالرد عليه )

!الرابط
لجلب رابط المجموعه فقط ارسل الامر

!انهاء
لأنهاء التشغيل في المكالمه

!تخطي
لتخطي التشغيل الحالي

!ايقاف
لايقاف التشغيل مؤقتا

!استئناف
لاستئناف التشغيل في المكالمه

!مغادرة
لمغادرة المجموعة بشكل اجباري

!التشغيل
لعرض قائمى التشغيل الحالية في المجموعة
"""

PLAY_TEXT = """
**✘ اوامر المستخدمين العاديين!**

!تشغيل
لتشغيل المقطع الصوتي في المكالمه اكتب الامر 

"""
