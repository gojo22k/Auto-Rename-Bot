from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from helper.database import madflixbotz

@Client.on_message(filters.private & filters.command("autorename") & filters.video)
async def auto_rename_command(client, message):
    user_id = message.from_user.id
    
    # Check if the message has a caption
    if message.video.caption:
        # Extract the caption from the video message
        format_template = message.video.caption.strip()

        # Save the format template to the database
        await madflixbotz.set_format_template(user_id, format_template)

        await message.reply_text("**Auto Rename Format Updated Successfully! ✅**")
    else:
        await message.reply_text("**Error:** No caption found in the video message.")

@Client.on_message(filters.private & filters.command("setmedia"))
async def set_media_command(client, message):
    user_id = message.from_user.id    
    media_type = message.text.split("/setmedia", 1)[1].strip().lower()

    # Save the preferred media type to the database
    await madflixbotz.set_media_preference(user_id, media_type)

    await message.reply_text(f"**Media Preference Set To :** {media_type} ✅")
