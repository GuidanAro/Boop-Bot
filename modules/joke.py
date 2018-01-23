import praw


async def main(message, args, client):
    r = praw.Reddit(client_id="2oY1zbvsePS4BQ", client_secret="rk7rO3yuSY-tG0xCOYIG0H1YseI", username="JTpcwarrior",
                    password="00404499", user_agent="boopy the discord bot")
    sub = r.subreddit('jokes')
    joke = sub.random()
    await client.send_message(message.channel, str(joke.title))
    await client.send_message(message.channel, joke.selftext)

async def help(message, args, client):
    await client.send_message(message.channel, "Pulls a joke from /r/jokes, no guarantees that they are good or "
                                               "politically correct. USAGE: !joke")

