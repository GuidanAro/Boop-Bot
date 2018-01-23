async def main(message, args, client):
    if len(args) > 1:
        del args[0]
        person = " ".join(args)
        await client.send_message(message.channel, person + " has been booped!", tts=True)
    else:
        await client.send_message(message.channel, "I have been booped!")


async def help(message, args, client):
    await client.send_message(message.channel, "Use !boop [person] to boop someone! Use !boop to boop me!")
