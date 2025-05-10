from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("glink"))
async def generate_link(client, message):
    command_text = message.text.split(maxsplit=1)
    if len(command_text) < 2:
        await message.reply("Please provide the name for the movie!\n\nExample: `/glink game of thrones`", quote=True)
        return
    movie_name = command_text[1].replace(" ", "-")
    bot_username = "SagaXAnimeBot"  # Replace with your actual bot username
    link = f"https://telegram.me/{bot_username}?start=getfile-{movie_name}"
    
    await message.reply(
        text=f"Here is your link: {link}",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url={link}")]]
        ),
        quote=True
    )
