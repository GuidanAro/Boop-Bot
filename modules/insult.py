import random

insults = [  # list of insults
    "You're a failed abortion whose birth certificate is an apology from the condom factory",
    "You must have been born on a highway, because that's where most accidents happen",
    "You're so ugly Hello Kitty said goodbye to you",
    "It looks like your face caught on fire and someone tried to put it out with a fork",
    "Your family tree is a cactus, because everybody on it is a prick",
    "We all sprang from apes, but you didn't spring far enough",
    "I would ask how old you are, but I know you can't count that high",
    "You must be the arithmetic man; you add trouble, subtract pleasure, divide attention, and multiply ignorance",
    "With a face like yours, I wish I was blind",
    "You know so little and know it fluently",
    "Your mother was a hamster, and your Father smelt of elderberries",
    "you're a fucking weeaboo"
]


async def main(message, args, client):
    del args[0]
    name = " ".join(args)
    print("insult sent to " + name)
    rand = random.randint(0, len(insults)-1)
    resp = insults[rand]
    await client.send_message(message.channel, resp + " " + name)
    if "boopy" == name.lower():
        await client.send_message(message.channel, ".....Hey that's me!")


async def help(message, args, client):
    await client.send_message(message.channel, "use !insult [name] to insult someone. The insults are mean so use "
                                               "them for evil, not good.")
