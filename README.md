<h1>Boopy</h1> 
 
Discord Bot written in python Use !help on commands to see their function. Modules are placed in the /modules folder Modules are made up using 2 functions, main and help, both using 3 arguments: message, args, client. Using these 3 allows the modules to import the message object from discord.py, the text of the message as a list (with ![command] being in the 0th spot), and the client to allow for control of the discord client. All modules are imported at the start of the bot, so any modules that are changed must be reimported by restarting boopy. 
<br /> 
 
Current list of modules: 
<ul> 
<li>8ball (gives an '8 ball' type response) 
<li>addquote 
<li>quote (reads quotes, requires a quote.txt file in /Boop-bot directory) 
<li>boop 
<li>help 
<li>dance 
<li>joke 
<li>patch (patch notes for Heroes of the Storm, pulled from their news page) 
<li>roll (rolls dice) 
<li>speak (allows for command line chat entry) 
<li>insult 
</ul> 

<b>REQUIREMENTS</b>
<ul>
<li>discord.py (duh)
<li>aiohttp
<li>websockets
<li>requests
<li>re
<li>BeautifulSoup4
<li>praw (if you don't want to set up a reddit bot, delete the joke.py file)
<li>dice
 
