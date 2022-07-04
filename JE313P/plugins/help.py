from telethon import events, Button
from JE313P import JE313P, BOT_USERNAME

btn =[
    [Button.inline("الادمن", data="admin"),],
    [Button.inline("التثبيت", data="pins"), Button.inline("التنظيف", data="purges")],
    [Button.inline("التشغيل", data="play"), Button.inline("المحذوفين", data="zombies")],
    [Button.inline("القفل", data="locks"), Button.inline("اخرى", data="misc")],
    [Button.inline("الرئيسية", data="start")]]

HELP_TEXT = "اهلا بك في قائمة اوامر سورس جيبثون\n\nاضغط على الازرار من الاسفل:"


@JE313P.on(events.NewMessage(pattern="[!?/]الاوامر"))
async def help(event):

    if event.is_group:
       await event.reply("اضغط على الاسفل لعرض الاوامر", buttons=[
       [Button.url("اضغط هنا", "t.me/{}?start=help".format(BOT_USERNAME))]])
       return

    await event.reply(HELP_TEXT, buttons=btn)

@JE313P.on(events.NewMessage(pattern="^/start help"))
async def _(event):

    await event.reply(HELP_TEXT, buttons=btn)

@JE313P.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):

     await event.edit(HELP_TEXT, buttons=btn)
