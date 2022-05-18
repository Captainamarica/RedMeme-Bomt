from pyrogram import Client
from functools import wraps
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant

force_subchannel = "Memehubtgsl"

CAPTION_BTN = InlineKeyboardMarkup([[
                 InlineKeyboardButton('Join Here - MemeHub Telegram 🇱🇰', url=f"https://t.me/{force_subchannel}")
                 ],
                 [
                 InlineKeyboardButton('🐞 ʀᴘᴏʀᴛ ʙᴜɢs 🐞', url=f"https://t.me/Imgishan")
                 ],
                 [
                 InlineKeyboardButton(text="♻️ Reload ♻️",callback_data="ref")
                 ]]
                  )

def FSub(func):
    @wraps(func)
    async def force(_, message):
        if force_subchannel:
           try:
               user = await bot.get_chat_member(force_subchannel, message.from_user.id)
               if user.status == "kicked out":
                   await message.reply_text("Ur Banned")
                   return 
           except UserNotParticipant:
               file_id = "CAADBQADOAcAAn_zKVSDCLfrLpxnhAI"
               await bot.send_sticker(message.chat.id, file_id)
               text = f"""**❌ Dear {message.from_user.mention}, Access Denied ❌**
Memehub eke nathuva Mokatada yako Botva Start Kare kkk😒😒
♻️Join and Try Again.♻️"""
               reply_markup = FORCESUB_BUTTONS
               await message.reply_text(
               text=text,
               reply_markup=reply_markup
               ) 
        return await func(_, message)    
    return force

@Client.on_callback_query()  
async def tgm(bot, update):  
    if update.data == "add": 
        await update.answer(
             text="♻️Adding Soon.....",
        )
    elif update.data == "bak":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=CLOSE_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="👻 ʙᴀᴍᴄᴋ 👻",
         )
    elif update.data == "bak":
         await update.message.delete()
         await bot.delete_message(update.chat.id, update.message.id)
    elif update.data == "hlp":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=CLOSE_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="👻 ʜᴇᴍʟᴘ 👻",
         )
    elif update.data == "cloc":
         await update.message.delete()
    elif update.data == "ref": 
        await update.answer(
             text="♻️Reloading.....♻️",
        )   
