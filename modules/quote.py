import random


async def main(message, args, client):
    file = open('quote.txt', 'r', encoding="utf8")
    quotes = file.read().split(":")
    num = len(quotes)
    if len(args) > 1:
        try:
            quotenum = int(args[1])
        except:
            await client.send_message(message.channel,
                                      args[1] + " is not a number")
        if quotenum > num-1 or quotenum == 0:
            await client.send_message(message.channel, "That quote is out of range (there aren't that many quotes)")
        else:
            await client.send_message(message.channel, args[1] + ": " + quotes[quotenum])
    else:
        rand = random.randint(1, len(quotes)-1)
        await client.send_message(message.channel, "Quote number " + str(rand) + ": " + quotes[rand])
    file.close()


async def help(message, args, client):
    await client.send_message(message.channel, "Use !quote [number] to print a specific quote, no numbers to get a "
                                               "random quote")
