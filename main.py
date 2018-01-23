import logging, discord, builtins, sys, json
from os import listdir

loaded = {}
reactions = {}
reply = {}

logging.basicConfig(level=logging.INFO)

with open('reactions.json', encoding='utf8') as json_data_file:  # load reactions file
    reactions = json.load(json_data_file)
with open('reply.json') as json_data_file:  # load reply file
    reply = json.load(json_data_file, encoding='utf8')


def log(message, **optionalArgs):  # prints log stuff with optional Arg 'level'
    if 'level' in optionalArgs:

        if (type(optionalArgs['level']) is int):
            logLevel = optionalArgs['level']

        else:
            logLevel = 1

    else:
        logLevel = 1

    if (logLevel == 1):
        print("[LOW] " + message)

    elif (logLevel == 2):
        print("[MEDIUM] " + message)

    elif (logLevel == 3):
        print("[URGENT] " + message)


def listContains(listMain, test):  # Checks if a list object contains a certain object.

    for a in listMain:
        if a == test:
            return True
    return False


def loadAll():  # Loads everything at the start.

    builtins.log = log
    sys.path.append("modules")
    onlyfiles = listdir('modules')
    moduleList = []  # Create list to contain module names.

    for module in onlyfiles:
        modName = module.split(".")  # Get the first part of the module name, excluding the extension .py
        obj = __import__(modName[0])
        loaded[modName[0]] = obj  # Add module to the global variables.
        log("Loaded module with name: '" + modName[0] + "'", level=1)
        moduleList.insert(0, modName[0])
    client = discord.Client()  # Initialise new Discord client.
    return client, moduleList


async def runCommand(commTbl, message, ModuleList): # Define main command-processing function.

    if (commTbl[0] == "help"): # Checks if command specified is special module 'help'
        try:  # Attempt to run help for a specified command. If help does not exist, or the command does not exist,
            # or it errors, display that it has errored.
            if loaded[commTbl[1]] is not None:
                prog = loaded[commTbl[1]]
                await client.send_message(message.channel, "Help for " + commTbl[1] + ":")
                await prog.help(message, commTbl, client)
        except Exception:
            log("Error occured in " + commTbl[0], level=3)
            await client.send_message(message.channel, "Help for the command specified could not be found, "
                                      + message.author.mention + ".")

    elif (commTbl[0] in sys.modules): # Checks if command specified exists in modules loaded.
        log("Found module with name " + commTbl[0], level=1)
        prog = loaded[commTbl[0]]
        if prog is not None:
            try: # Attempt to run the command specified. If an error occurs, display that an error has occurred.
                await prog.main(message, commTbl, client)
            except Exception as ex:
                log("Error occured in " + commTbl[0] + ": " + str(ex), level=3)
        else:
            log("The command: " + commTbl[0] + " was not found.", level=2)
            await client.send_message(message.channel, "The command specified could not be found, "
                                      + message.author.mention + ".")


client, moduleList = loadAll()  # Run loadAll


@client.event
async def on_ready():
    log('I\'m ready to go!', level=1)


@client.event
async def on_message(message):  # On message. This tries to figure out if it is a command,
    #  and if so, uses runCommand on it. Else, runs auto module on it.
    if message.author.id != client.user.id:
        if message.content.startswith('!'): # If it is a command
                comm = message.content[1:] # Get rid of !
                comms = comm.split(" ") # Split the command into the parameters
                log(message.author.name + " attempted to run command: " + comms[0], level=1)
                await runCommand(comms, message, moduleList)
        else:
            await loaded['reaction'].main(message, client, reactions, reply)
            log("Ran reactions with text sent by " + message.author.name)

client.run("Key")

if not client.is_logged_in:
    log("Error logging in", level=3)
