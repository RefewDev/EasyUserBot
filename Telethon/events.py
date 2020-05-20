from telethon import events
from Telethon import clients

def message(**args):
    pattern = args.get('pattern', None)

    if pattern is not None and not pattern.startswith('(?i)'):
        args['pattern'] = '(?i)' + pattern

    def decorator(func):
        [client.add_event_handler(func, events.NewMessage(**args)) for client in clients]
        [client.add_event_handler(func, events.MessageEdited(**args)) for client in clients]
        return func

    return decorator
