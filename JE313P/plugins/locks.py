from telethon import events, Button, types
from JE313P import JE313P
from JE313P.status import *

LOCKS_HELP = """
**هذه هي اوامر القفل و الفتح  في الدردشة**

!قفل
لقفل شيء معين في الدردشة

!فتح 
لفتح الصلاحيات عن شيء معين

الصلاحيات
لعرض الصلاحيات التي يمكنك قفلها
"""

@JE313P.on(events.NewMessage(pattern="^[!?/]قفل ?(.*)"))
@is_admin
async def lock(event, perm):
    if not perm.change_info:
      await event.reply("تحتاج الى بعض صلاحيات المشرف لاستخدام هذا الامر")
      return
    input_str = event.pattern_match.group(1)
    if not input_str:
       await event.reply("يرجى تحديد شيء لقفله اولا")
       return
    if "الرسائل" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_messages=False)
       await event.reply("- تم قفل الرسائل")
    elif "الميديا" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_media=False)
       await event.reply("- تم قفل الوسائط")
    elif "الملصقات" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_stickers=False)
       await event.reply("- تم قفل الملصقات.")
    elif "المتحركة"in input_str:
       await JE313P.edit_permissions(event.chat_id, send_gifs=False)
       await event.reply("- تم قفل المتحركة")
    elif "التوجيه" in input_str:
       await JE313P.edit_permissions(event.chat_id, forwards=False)
       await event.reply("- تم قفل التوجيه")
    elif "الالعاب" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_games=False)
       await event.reply("- تم قفل الالعاب")
    elif "الانلاين" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_inline=False)
       await event.reply("- تم قفل الانلاين")
    elif "التصويت" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_polls=False)
       await event.reply("- تم قفل التصويت")
    elif "الروابط" in input_str:
       await JE313P.edit_permissions(event.chat_id, embed_link_previews=False)
       await event.reply("- تم قفل الروابط")
    elif "الكل" in input_str:
       await JE313P.edit_permissions(event.chat_id,
          send_messages=False, 
          send_media=False,
          send_stickers=False,
          send_gifs=False,
          send_games=False,
          send_inline=False,
          send_polls=False,
          embed_link_previews=False)
       await event.reply("- تم قفل الكل")


@JE313P.on(events.NewMessage(pattern="^[!?/]فتح ?(.*)"))
@is_admin
async def unlock(event, perm):
    if not perm.change_info:
      await event.reply("تحتاج الى بعض صلاحيات المشرف لاستخدام هذا")
      return
    input_str = event.pattern_match.group(1)
    if not input_str:
       await event.reply("يرجى تحديد شيء لالغاء قفله اولا")
       return
    if "الرسائل" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_messages=True)
       await event.reply("تم فتح الكتابة")
    elif "الميديا" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_media=True)
       await event.reply("تم فتح الوسائط")
    elif "الملصقات" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_stickers=True)
       await event.reply("تم فتح الملصقات")
    elif "المتحركة"in input_str:
       await JE313P.edit_permissions(event.chat_id, send_gifs=True)
       await event.reply("تم فتح المتحركة")
    elif "التوجيه" in input_str:
       await JE313P.edit_permissions(event.chat_id, forwards=True)
       await event.reply("تم فتح التوجيه")
    elif "الالعاب" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_games=True)
       await event.reply("تم فتح الالعاب")
    elif "الانلاين" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_inline=True)
       await event.reply("تم فتح الانلاين")
    elif "التصويت" in input_str:
       await JE313P.edit_permissions(event.chat_id, send_polls=True)
       await event.reply("تم فتح `التصويت")
    elif "الروابط" in input_str:
       await JE313P.edit_permissions(event.chat_id, embed_link_previews=True)
       await event.reply("تم فتح الروابط")
    elif "الكل" in input_str:
       await JE313P.edit_permissions(event.chat_id,
          send_messages=True, 
          send_media=True,
          send_stickers=True,
          send_gifs=True,
          send_games=True,
          send_inline=True,
          send_polls=True,
          embed_link_previews=True)
       await event.reply("تم فتح الكل")


@JE313P.on(events.NewMessage(pattern="^[!?/]الصلاحيات"))
async def locktypes(event):
    TEXT = """
**Locks:**

‣ الرسائل
‣ الميديا
‣ الملصقات
‣ المتحركة
‣ الروابط
‣ الالعاب
‣ الانلاين
‣ التوجيه
‣ التصويت
‣ الكل
"""
    await event.reply(TEXT)

@JE313P.on(events.callbackquery.CallbackQuery(data="locks"))
async def _(event):

    await event.edit(LOCKS_HELP, buttons=[[Button.inline("رجوع", data="help")]])
