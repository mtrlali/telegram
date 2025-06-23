
from telethon.sync import TelegramClient, events

api_id = 22875808
api_hash = 'd71991084fbdf8fa6e7e36f0c54d37e2'

# القنوات المصدر
source_channels = [-1001671680594, -1002107258481, -1001706065436]
# القناة الهدف
target_channel = -1001837588349

client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channels))
async def handler(event):
    try:
        if event.message.text:
            await client.send_message(target_channel, event.message.text)
        elif event.message.media:
            await client.send_file(target_channel, file=event.message.media, caption=event.message.text or "")
        print(f"✅ تم نسخ الرسالة من {event.chat_id}")
    except Exception as e:
        print(f"❌ خطأ: {e}")

print("🚀 السكربت شغال بنسخ الرسائل (وليس إعادة توجيه)...")
client.start()
client.run_until_disconnected()
