#  requires a quote.txt to be in the main directory


async def main(message, args, client):
    if message.server.roles[-1] not in message.author.roles:
        if ":" not in message.content:
            file = open('quote.txt', 'a', encoding="utf8")
            quotes = []
            del args[0]
            mes = " ".join(args)
            quotes.insert(len(quotes), ":")
            quotes.insert(len(quotes), mes)
            writ = " ".join(quotes)
            writ = writ.strip()
            file.write(writ)
            file.close()
            file = open('quote.txt', 'r', encoding="utf8")
            quotes = file.read().split(":")
            num = len(quotes)
            file.close()
            await client.send_message(message.channel, "quote " + str(num - 1) + " added!")
            print("added quote" + writ)
        else:
            await client.send_message(message.channel, "Please don't put colons in quotes. This breaks boopy.")
    else:
        await client.send_message(message.channel, "You are not allowed to make quotes")


async def help(message, args, client):
    await client.send_message(message.channel, "use !addquote [quote here] to add the quote to the list of quotes")

