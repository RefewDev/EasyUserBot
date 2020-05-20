from Telethon.events import message

#IT: Outgoing è per i messaggi che potranno essere eseguiti solo da voi stessi!
#EN: Outgoing is for messages that can only be executed by yourself!

@message(outgoing=True, pattern='[.]chatid')
async def chatid(e):
    await e.edit("<b>Chat-ID</b>: " + str(e.chat_id), parse_mode="html")

@message(outgoing=False, pattern='[.]chatid')
async def chatid(e):
    await e.respond("<b>Chat-ID</b>: " + str(e.chat_id), parse_mode="html")
