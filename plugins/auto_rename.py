from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from helper.database import madflixbotz
import re

@Client.on_message(filters.private & filters.command("autorename"))
async def auto_rename_command(client, message):
    user_id = message.from_user.id

    # Extract the format from the command
    format_template = message.text.split("/autorename", 1)[1].strip()

    # Save the format template to the database
    await madflixbotz.set_format_template(user_id, format_template)

    await message.reply_text("**Auto Rename Format Updated Successfully! ✅**")

@Client.on_message(filters.private & filters.command("setmedia"))
async def set_media_command(client, message):
    user_id = message.from_user.id    
    media_type = message.text.split("/setmedia", 1)[1].strip().lower()

    # Save the preferred media type to the database
    await madflixbotz.set_media_preference(user_id, media_type)

    await message.reply_text(f"**Media Preference Set To :** {media_type} ✅")

@Client.on_message(filters.media & filters.private)
async def handle_media(client, message):
    user_id = message.from_user.id
    
    # Retrieve format template from database
    format_template = await madflixbotz.get_format_template(user_id)
    
    if not format_template:
        await message.reply_text("**Error:** Auto rename format not set. Please use `/autorename <keyword>` to set it.")
        return
    
    # Get the media caption
    caption = message.caption
    
    if not caption:
        await message.reply_text("**Error:** No caption found with the media.")
        return
    
    # Extract keyword value from caption
    keyword_value = extract_keyword_value(caption, format_template)
    
    if not keyword_value:
        await message.reply_text("**Error:** Could not extract value from caption.")
        return
    
    # Generate new file name
    new_file_name = f"{keyword_value}.mp4"
    
    # Assume you have some function to rename the file here
    # e.g., rename_file(media_id, new_file_name)
    
    await message.reply_text(f"**File Renamed To:** {new_file_name} ✅")

def extract_keyword_value(caption, keyword):
    """
    Extract the value corresponding to the keyword from the caption.
    """
    # Regex to find the value associated with the keyword
    match = re.search(f"{re.escape(keyword)} - (\d+)", caption)
    if match:
        return match.group(1)
    return None
