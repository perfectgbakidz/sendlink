import asyncio
from telethon import TelegramClient, events
import os

# Replace these with your own values
api_id = '23864335'
api_hash = 'd87ed3740073395ede28a83218b46e4e'
phone_number = '+2348106277925'

# List of URLs to send
urls = [
    "google.com", "youtube.com", "tmall.com", "qq.com", "baidu.com", "facebook.com", "sohu.com", "login.tmall.com",
    "taobao.com", "yahoo.com", "jd.com", "wikipedia.org", "360.cn", "amazon.com", "sina.com.cn", "pages.tmall.com",
    "weibo.com", "live.com", "reddit.com", "vk.com", "okezone.com", "xinhuanet.com", "netflix.com", "blogspot.com",
    "csdn.net", "office.com", "alipay.com", "yahoo.co.jp", "instagram.com", "zhanqi.tv", "bongacams.com", 
    # ... (more URLs)
]

# Initialize the client
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage)  # This event handler listens for incoming messages
async def handle_new_message(event):
    # Get the sender's chat ID
    sender = await event.get_sender()
    sender_id = sender.id
    
    # Inform the sender that the bot is starting to send URLs
    await event.reply("You will receive a list of links shortly...")

    # Send each URL with a 3-second delay
    for url in urls:
        await client.send_message(sender_id, url)
        print(f'Sent: {url} to {sender_id}')
        await asyncio.sleep(3)  # Use await asyncio.sleep for non-blocking delay

async def main():
    # Start listening for incoming messages
    async with client:
        print("Bot is running and listening for incoming messages...")
        await client.run_until_disconnected()

if __name__ == '__main__':
    # Start the Telegram client and run the bot
    client.start(phone=phone_number)
    client.loop.run_until_complete(main())
