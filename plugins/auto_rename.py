from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from helper.database import madflixbotz

@Client.on_message(filters.private & filters.command("autorename"))
async def auto_rename_command(client, message):
    user_id = message.from_user.id

    # Extract the format from the command
    format_template = message.text.split("/autorename", 1)[1].strip()

    # Check if the message has a video
    if message.video:
        caption = message.caption or ""
        
        # Extract the keyword from the caption
        keyword_value = None
        for line in caption.split("\n"):
            if format_template.lower() in line.lower():
                keyword_value = line.split("-", 1)[1].strip()
                break

        if keyword_value:
            # Here, you would update the filename or perform any action needed
            # For example, you might rename the file or update the metadata in your system
            await message.reply_text(f"**Auto Rename Format Updated Successfully!**\nExtracted {format_template}: {keyword_value} ✅")
        else:
            await message.reply_text(f"**Error:** Could not find the keyword '{format_template}' in the video caption.")
    else:
        await message.reply_text("**Error:** Please send a video with a caption to use this command.")

@Client.on_message(filters.private & filters.command("setmedia"))
async def set_media_command(client, message):
    user_id = message.from_user.id    
    media_type = message.text.split("/setmedia", 1)[1].strip().lower()

    # Save the preferred media type to the database
    await madflixbotz.set_media_preference(user_id, media_type)

    await message.reply_text(f"**Media Preference Set To :** {media_type} ✅")
