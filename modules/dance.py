import os


async def main(message, args, client):
    print('that\'s a dancing cat...')
    cwd = os.getcwd()
    await client.send_file(message.channel, fp=cwd + "/images/dance.gif")


async def help(message, args, client):
    await client.send_message(message.channel, "you type !dance and a pusheen shows up. wtf this isn't hard")
