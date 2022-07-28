from Zaid import Zaid, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
ʜᴇʏᴀ! {}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Halo ! , Saya Adalah Mirc Music Bot. Siap Menemani Anda Memutar Music Dengan Mudah Di Voice Chat Groups.!
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ **ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ 🔘 ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ℹ️**.
"""

@Zaid.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍ Owner", "https://t.me/https://t.me/@riasyee")],
        [Button.url("🗣️ ꜱᴜᴘᴘᴏʀᴛ", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 ᴜᴘᴅᴀᴛᴇꜱ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", data="help")]])
       return

    if event.is_group:
       await event.reply("**Halo. Saya Aktif ✅**")
       return



@Zaid.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 Owner", "https://t.me/https://t.me/@riasyee")],
        [Button.url("🗣️ ꜱᴜᴘᴘᴏʀᴛ", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 ᴜᴘᴅᴀᴛᴇꜱ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", data="help")]])
       return
