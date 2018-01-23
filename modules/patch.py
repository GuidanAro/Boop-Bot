import requests, re
from bs4 import BeautifulSoup


async def main(message, args, client):
    res = requests.get('http://us.battle.net/heroes/en/blog/')
    c = res.content
    soup = BeautifulSoup(c, "html.parser")
    url = "http://us.battle.net/heroes/en/blog/"
    for a in soup.find_all("a", text=re.compile('PATCH NOTES', re.IGNORECASE)):
        url = "http://us.battle.net" + a['href']
        break
    await client.send_message(message.channel, str(url) + "\n")


async def help(message, args, client):
    await client.send_message(message.channel, "Use !patch to link the latest Heroes of the Storm patch")