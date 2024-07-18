# btn : about and close change here

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>ŦrαfͥαlͣgͫαrŁαw</a>\n○ Cultured Channel : <a href='https://t.me/Cultured_Madness'>Cultured Madness</a>\n○ Anime Channel: <a href='https://t.me/Anime_Madness'>Anime Madness</a>\n○ ᴏngoing anime: <a href='https://t.me/Ongoing_Madness'>ongoing madness</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                        InlineKeyboardButton('🍁 Cultured', url='https://t.me/Cultured_Madness')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
