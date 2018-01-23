async def main(message, client, reactions, reply):
    cont = message.content

    for response in reactions:  # checks reactions.json for things the bot should react to
        if response.lower() in cont.lower():
            print(reactions[response])
            await client.add_reaction(message, str(reactions[response]))
            break
    for rep in reply:  # checks reply.json for auto replies
        if rep.lower() in cont.lower():
            await client.send_message(message.channel, reply[rep])
            break
