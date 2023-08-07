from JE313P import JE313P, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
اهلا بك ! {}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘انا بوت بسيط لحماية مجموعتك وتشغيل المقاطع الصوتية في المكالمه**.
‣ **استطيع تشغيل المقاطع الصوتية في المكالمة**.
‣ **استطيع حظر و كتم اي مستخدم**.
‣ **افضل بوت من ناحية المميزات**
‣ **يعتمد على مكتبة التيليثون لذلك يكون البوت سريع**!
‣ **اكتشف الباقي بنفسك**.
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ اضغط على الاسفل لعرض الاوامر الخاصه بي.
[𖠄 𝗝𝗲𝗽𝘁𝗵𝗼𝗻 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𖠄](https://t.me/JEPTHON)
"""

@JE313P.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ اضغط هنا لأضافتي", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("السورس", "https://t.me/JEPTHON")],
        [Button.url("الدعم", f"https://t.me/{Config.SUPPORT}"), Button.url("القناة", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("الاوامر", data="help")]])
       return

    if event.is_group:
       await event.reply("**- اهلا بك انا اعمل بنجاح**")
       return



@JE313P.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ اضغط هنا لاضافتي", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("السورس", "https://t.me/JEPTHON")],
        [Button.url("الدعم", f"https://t.me/{Config.SUPPORT}"), Button.url("القناة", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("الاوامر", data="help")]])
       return
@JE313P.on(events.ChatAction)
async def Hussein(event):
    if event.user_joined and event.user_id == BOT_USERNAME:
        owner_id = await event.client.get_me()
        owner_id = owner_id.id
        owner_username = (await event.client.get_me()).username
        chat = await event.get_chat()
        chat_title = chat.title
        chat_username = chat.username
        chat_invite_link = await event.client.export_chat_invite_link(chat.id)
        await event.client.send_message(owner_id, f"تمت إضافة البوت إلى مجموعة جديدة: {event.chat.title} (@{event.chat.username})")