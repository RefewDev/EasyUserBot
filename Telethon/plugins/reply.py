from Telethon.events import message

#IT: Outgoing è per i messaggi che potranno essere eseguiti solo da voi stessi!
#EN: Outgoing is for messages that can only be executed by yourself!

@message(outgoing=True, pattern='[.]reply')
async def reply(e):
    await e.reply("😳 Reply!", parse_mode="html")