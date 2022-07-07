from telethon import events, Button
from telethon.errors import ChatAdminRequiredError, UserAdminInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsAdmins, ChatBannedRights
from JE313P import JE313P
from JE313P.status import *


CLEANER_HELP = """
**هذه هي اوامر عرض وحذف الحسابات المحذوفة**
!المحذوفين
لعرض الحسابات المحذوفة في الدردشة

!المحذوفين تنظيف
لحذف و طرد الحسابات المحذوفة من لمجموعة
[𖠄 𝗝𝗲𝗽𝘁𝗵𝗼𝗻 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𖠄](https://t.me/JEPTHON)

"""


BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


@JE313P.on(events.NewMessage(pattern="^[!?/]المحذوفين ?(.*)"))
@is_admin
async def clean(event, perm):
    if not perm.ban_users:
      await event.reply("- ليست لديك صلاحيات كافية")
      return
    input_str = event.pattern_match.group(1)
    stats = "المجموعة نظيفة"
    deleted = 0

    if "clean" not in input_str:
      zombies = await event.respond("يتم البحث عن حسابات محذوفه او اخر ظهور لها قديم")
      async for user in event.client.iter_participants(event.chat_id):

            if user.deleted:
                deleted += 1
      if deleted > 0:
            stats = f"تم ايجاد **{deleted}** من المحذوفين هنا\
            \nلطردهم ارسل `/المحذوفين تنظييف`"
      await zombies.edit(stats)
      return

    cleaning_zombies = await event.respond("- جار طرد الحسابات المحذوفة انتظر قليلا")
    del_u = 0
    del_a = 0

    async for user in event.client.iter_participants(event.chat_id):
        if user.deleted:
            try:
                await event.client(
                    EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS)
                )
            except ChatAdminRequiredError:
                await cleaning_zombies.edit("- عذرا ليس لدي صلاحيات الحظر هنا")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await event.client(EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1

    if del_u > 0:
        stats = f"تم تنظيف`{del_u}` من الحسابات المحذوفة"

    if del_a > 0:
        stats = f"تم تنظيف`{del_u}` من الحسابات المحذوفة \
        \n`{del_a}` من حسابات المشرفين المحذوفة لم يتم طردهم"

    await cleaning_zombies.edit(stats)

@JE313P.on(events.callbackquery.CallbackQuery(data="zombies"))
async def _(event):
    await event.edit(CLEANER_HELP, buttons=[[Button.inline("رجوع", data="help")]])
