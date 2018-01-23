async def main(message, args, client):
    if str(message.author) == "Guidan#2049":
        say = input("What should I say?: ")
        await client.send_typing(message.channel)
        await client.send_message(message.channel, say)
    else:
        await client.send_message(message.channel, "Only my master can tell me what to say " + message.author.mention
                                  + ".")


async def help(message, args, client):
    await client.send_message(message.channel, "Only The Head Panda can tell me what to say, this command is not for "
                                               "you")