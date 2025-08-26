from pyrogram import Client, filters
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
ADMIN_ID = 6672748094  # Your Telegram user ID

app = Client("storage_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# /start command
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "Hello 👋\n\n"
        "Main ek **Storage Bot** hoon.\n"
        "Tum jo bhi file bhejoge, main usse storage channel me save kar dunga ✅"
    )

# File handling
@app.on_message(filters.document | filters.video | filters.audio | filters.photo)
async def save_file(client, message):
    sent = await message.forward(CHANNEL_ID)
    file_link = f"https://t.me/{BOT_TOKEN.split(':')[0]}?start=mid{sent.id}"
    await message.reply_text(f"✅ File Saved!\n\n📂 [Open File Link]({file_link})", disable_web_page_preview=True)

# Broadcast command (only admin)
@app.on_message(filters.command("broadcast") & filters.user(ADMIN_ID))
async def broadcast(client, message):
    await message.reply_text("Broadcast feature is ready!")

app.run()
